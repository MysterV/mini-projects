import time
import os
import threading
import subprocess
from datetime import datetime, timedelta
from ctypes import cast, POINTER, windll, Structure, c_int, c_uint, byref
from comtypes import CLSCTX_ALL, CoInitialize
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from pynput import mouse, keyboard
import screen_brightness_control as sbc

# ===== CONFIG =====
DEBUG_MODE = True  # Set to True for 1-minute debug version
RESOLUTION_STEPS = [(1920, 1080), (1680, 1050), (1440, 900), (1280, 720), (1024, 576), (854, 480)]
# RESOLUTION_STEPS = [(1920, 1200), (1680, 1050), (1440, 900), (1280, 720), (1024, 576), (854, 480)]

# Timings
TIME_MULTIPLIER = 60 if DEBUG_MODE else 1
TIMESTAMP = "23:00"  # HH:MM, time to finish shut down at
# Everything below in seconds
BACK_FROM_AFK_DELAY = 60 * 60 / TIME_MULTIPLIER
TIME_TO_WAIT_IF_AFK = 60 * 10 / TIME_MULTIPLIER
DURATION_TOTAL = 60 * 60 / TIME_MULTIPLIER
DURATION_VOLUME = 60 * 50 / TIME_MULTIPLIER
DURATION_DESATURATE = 60 * 40 / TIME_MULTIPLIER
DURATION_RESOLUTION = 60 * 10 / TIME_MULTIPLIER
DURATION_BRIGHTNESS = 60 * 5 / TIME_MULTIPLIER

# TODO: do we even need this???
TRIGGER_VOLUME = timedelta(seconds=DURATION_VOLUME)
TRIGGER_DESATURATE = timedelta(seconds=DURATION_DESATURATE)
TRIGGER_RESOLUTION = timedelta(seconds=DURATION_RESOLUTION)
TRIGGER_BRIGHTNESS = timedelta(seconds=DURATION_BRIGHTNESS)

# ===== CODE =====

VOLUME_STEPS = 100
BRIGHTNESS_STEPS = 100

# Global state
original_volume = None
original_brightness = None
original_resolution = None
volume_locked = False
shutdown_active = False

class DEVMODE(Structure):
    _fields_ = [
        ('dmDeviceName', c_uint * 32),
        ('dmSpecVersion', c_uint),
        ('dmDriverVersion', c_uint),
        ('dmSize', c_uint),
        ('dmDriverExtra', c_uint),
        ('dmFields', c_uint),
        ('dmPositionX', c_int),
        ('dmPositionY', c_int),
        ('dmDisplayOrientation', c_uint),
        ('dmDisplayFixedOutput', c_uint),
        ('dmColor', c_uint),
        ('dmDuplex', c_uint),
        ('dmYResolution', c_uint),
        ('dmTTOption', c_uint),
        ('dmCollate', c_uint),
        ('dmFormName', c_uint * 32),
        ('dmLogPixels', c_uint),
        ('dmBitsPerPel', c_uint),
        ('dmPelsWidth', c_uint),
        ('dmPelsHeight', c_uint),
        ('dmDisplayFlags', c_uint),
        ('dmDisplayFrequency', c_uint),
        ('dmICMMethod', c_uint),
        ('dmICMIntent', c_uint),
        ('dmMediaType', c_uint),
        ('dmDitherType', c_uint),
        ('dmReserved1', c_uint),
        ('dmReserved2', c_uint),
        ('dmPanningWidth', c_uint),
        ('dmPanningHeight', c_uint)
    ]

class ActivityMonitor:
    def __init__(self):
        self.active = False
        self.last_activity = datetime.now()
        self.mouse_listener = None
        self.keyboard_listener = None
        
    def on_activity(self):
        self.active = True
        self.last_activity = datetime.now()
        
    def on_move(self, x, y): self.on_activity()
    def on_click(self, x, y, button, pressed): self.on_activity()
    def on_scroll(self, x, y, dx, dy): self.on_activity()
    def on_press(self, key): self.on_activity()
    def on_release(self, key): self.on_activity()
    
    def start_monitoring(self):
        self.mouse_listener = mouse.Listener(
            on_move=self.on_move, 
            on_click=self.on_click, 
            on_scroll=self.on_scroll
        )
        self.keyboard_listener = keyboard.Listener(
            on_press=self.on_press, 
            on_release=self.on_release
        )
        self.mouse_listener.start()
        self.keyboard_listener.start()
        
    def stop_monitoring(self):
        if self.mouse_listener: self.mouse_listener.stop()
        if self.keyboard_listener: self.keyboard_listener.stop()
        
    def is_afk(self, minutes=5):
        return (datetime.now() - self.last_activity).seconds > minutes * 60

def get_current_volume():
    try:
        CoInitialize()
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        return volume.GetMasterVolumeLevelScalar()
    except:
        return 0.0

def set_volume(level):
    try:
        CoInitialize()
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))

        volume.SetMasterVolumeLevelScalar((level/100), None)
        return True
    except Exception as e:
        print(f"Volume error: {e}")
        return False

def volume_guard(target_volume_percent):
    """Continuously enforces target volume level"""
    global volume_locked, shutdown_active
    
    target_scalar = target_volume_percent / 100.0  # Convert to 0-1 range
    
    while volume_locked and not shutdown_active:
        try:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            
            current_scalar = volume.GetMasterVolumeLevelScalar()
            if abs(current_scalar - target_scalar) > 0.01:
                volume.SetMasterVolumeScalar(target_scalar, None)
        except:
            pass
        time.sleep(0.1)

def get_current_resolution():
    try:
        dm = DEVMODE()
        dm.dmSize = 220  # sizeof(DEVMODE)
        windll.user32.EnumDisplaySettingsW(None, -1, byref(dm))  # ENUM_CURRENT_SETTINGS
        return (dm.dmPelsWidth, dm.dmPelsHeight)
    except:
        return (1920, 1080)

def set_resolution(width, height):
    # TODO: this function does absolutely nothing
    try:
        dm = DEVMODE()
        dm.dmSize = 220
        dm.dmPelsWidth = width
        dm.dmPelsHeight = height
        dm.dmFields = 0x00080000 | 0x00100000  # DM_PELSWIDTH | DM_PELSHEIGHT
        result = windll.user32.ChangeDisplaySettingsW(byref(dm), 0)
        return result == 0  # DISP_CHANGE_SUCCESSFUL
    except Exception as e:
        print(f"Resolution error: {e}")
        return False

def set_brightness(level):
    try:
        sbc.set_brightness(level)
        return True
    except Exception as e:
        print(f"Brightness error: {e}")
        return False

def get_current_brightness():
    try:
        return sbc.get_brightness()[0]
    except:
        return 100

def apply_color_filter(saturation_percent):
    """Apply grayscale filter using Windows built-in color filters"""
    try:
        # This uses Windows 10+ built-in color filters
        # Registry path: HKEY_CURRENT_USER\Software\Microsoft\ColorFiltering
        import winreg
        key_path = r"Software\Microsoft\ColorFiltering"
        
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path) as key:
            # Enable color filtering
            winreg.SetValueEx(key, "Active", 0, winreg.REG_DWORD, 1)
            # Set to grayscale (type 1)
            winreg.SetValueEx(key, "FilterType", 0, winreg.REG_DWORD, 1)
            
        # Notify system of registry change
        windll.user32.SendMessageW(0xFFFF, 0x001A, 0, 0)  # WM_SETTINGCHANGE
        return True
    except Exception as e:
        print(f"Color filter error: {e}")
        return False

def remove_color_filter():
    try:
        import winreg
        key_path = r"Software\Microsoft\ColorFiltering"
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path) as key:
            winreg.SetValueEx(key, "Active", 0, winreg.REG_DWORD, 0)
        windll.user32.SendMessageW(0xFFFF, 0x001A, 0, 0)
        return True
    except:
        return False

def store_original_settings():
    global original_volume, original_brightness, original_resolution
    original_volume = get_current_volume()
    original_brightness = get_current_brightness()
    original_resolution = get_current_resolution()

def restore_original_settings():
    global original_volume, original_brightness, original_resolution
    if original_resolution:
        set_resolution(*original_resolution)
    if original_brightness:
        set_brightness(original_brightness)
    if original_volume:
        # Convert dB back to percentage for restoration
        percent = max(0, min(100, (original_volume + 65.25) / 0.6525))
        set_volume(percent)
    remove_color_filter()

def shutdown_computer():
    global shutdown_active
    shutdown_active = True
    restore_original_settings()
    time.sleep(2)  # Allow restoration to complete
    # os.system("shutdown /f /t 0")
    print("smiley shutdown")

def main():
    global volume_locked, shutdown_active
    
    if DEBUG_MODE:
        # Debug mode: start immediately, 1 minute total duration
        target_time = datetime.now() + timedelta(seconds=DURATION_TOTAL)
        print(f"DEBUG MODE: {DURATION_TOTAL}s shutdown test starting now")
        print(f"""Timeline:
    {DURATION_TOTAL}s - start,
    {DURATION_VOLUME}s - volume,
    {DURATION_DESATURATE}s - desaturate,
    {DURATION_RESOLUTION}s - resolution,
    {DURATION_BRIGHTNESS}s - dim""")
    else:
        # Parse target time
        target_time = datetime.strptime(TIMESTAMP, "%H:%M").replace(
            year=datetime.now().year,
            month=datetime.now().month,
            day=datetime.now().day
        )
        
        # If time already passed today, schedule for tomorrow
        # if datetime.now() > target_time:
        #     target_time += timedelta(days=1)
    
    print(f"Shutdown scheduled for: {target_time}")
    
    # Initialize activity monitoring
    monitor = ActivityMonitor()
    monitor.start_monitoring()
    
    # Store original settings
    store_original_settings()
    
    volume_guard_thread = None
    desaturation_active = False

    
    try:
        process_start = False
        while not shutdown_active:
            current_time = datetime.now()
            time_until_shutdown = target_time - current_time
            elapsed = (DURATION_TOTAL - time_until_shutdown.total_seconds())
            print(f'{elapsed:.1f} {time_until_shutdown.total_seconds():.1f}')
            
            # AFK check - pause if user inactive (skip in debug mode)
            if not process_start:
                if monitor.is_afk(5):
                    print("User AFK - pausing shutdown procedure")
                    time.sleep(TIME_TO_WAIT_IF_AFK)
                    continue
                else:
                    print('Beginning the process...')
                    process_start = True

            
            # If user becomes active during procedure, add time (skip in debug mode)
            if not process_start and monitor.active and time_until_shutdown < TRIGGER_VOLUME:
                target_time += timedelta(seconds=BACK_FROM_AFK_DELAY)
                monitor.active = False
                print(f"User activity detected - shutdown delayed to: {target_time}")
                continue
            
            # Volume reduction phase
            if time_until_shutdown <= TRIGGER_VOLUME:
                # Calculate gradual volume reduction
                volume_percent = int(max(0, 100 - (elapsed / DURATION_VOLUME * 100)))
                
                if not volume_locked:
                    print(f"Starting volume reduction ({DURATION_VOLUME} remaining)")
                    volume_locked = True
                    if volume_guard_thread is None:
                        volume_guard_thread = threading.Thread(target=volume_guard, args=(volume_percent,), daemon=True)
                        volume_guard_thread.start()
                set_volume(volume_percent)
            
            # Desaturation phase
            if time_until_shutdown <= TRIGGER_DESATURATE and not desaturation_active:
                print(f"Starting screen desaturation ({DURATION_DESATURATE} remaining)")
                apply_color_filter(0)  # TODO: the heck is this logic, where is the gradual change???
                desaturation_active = True
            
            # Resolution reduction phase
            if time_until_shutdown <= TRIGGER_RESOLUTION:
                resolution_index = min(int((elapsed / DURATION_RESOLUTION) * len(RESOLUTION_STEPS)), len(RESOLUTION_STEPS) - 1)
                
                if resolution_index >= 0 and resolution_index < len(RESOLUTION_STEPS):
                    width, height = RESOLUTION_STEPS[resolution_index]
                    if (width, height) != get_current_resolution():
                        set_resolution(width, height)
                        print(f"Resolution changed to {width}x{height}")
            
            # Brightness dimming phase
            if time_until_shutdown <= TRIGGER_BRIGHTNESS:
                # TODO: make it gradual
                brightness_percent = max(1, int((DURATION_BRIGHTNESS - elapsed/DURATION_BRIGHTNESS) * 100))
                set_brightness(brightness_percent)
            
            # Shutdown time reached
            if time_until_shutdown <= timedelta(0):
                print("Initiating shutdown...")
                shutdown_computer()
                break
                
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nShutdown cancelled by user")
        shutdown_active = True
        restore_original_settings()
    finally:
        monitor.stop_monitoring()
        if volume_guard_thread:
            volume_locked = False

if __name__ == "__main__":
    main()