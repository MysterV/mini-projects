# MY CODE
import time

BRIGHTNESS_SPEED = 5  # values 0.01+

def return_to_normal():
    set_brightness(100)
    set_resolution(1920, 1080)









# ===== WIP CODE =====

#TODO _ctypes.COMError: (-2147024809, 'Parametr jest niepoprawny.', (None, None, None, 0, None))
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def set_volume(level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(level, None)


from PIL import ImageGrab, ImageEnhance

#TODO THIS CHANGES AN IMAGE, BUT HOW TO APPLY IT?
def desaturate_screen():
    screen = ImageGrab.grab()
    enhancer = ImageEnhance.Color(screen)
    return enhancer.enhance(0.5)  # 0.0 is grayscale, 1.0 is original


#TODO THIS NOT WORKING
import win32api
import win32con
import pywintypes

def set_resolution(width, height):
    devmode = pywintypes.DEVMODEType()
    devmode.PelsWidth = width
    devmode.PelsHeight = height
    devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
    win32api.ChangeDisplaySettings(devmode, 0)


import screen_brightness_control as sbc

def set_brightness(level):
    sbc.set_brightness(level)
    return


from pynput import mouse, keyboard

class ActivityMonitor:
    def __init__(self): self.active = False
    def on_move(self, x, y): self.active = True
    def on_click(self, x, y, button, pressed): self.active = True
    def on_scroll(self, x, y, dx, dy): self.active = True
    def on_press(self, key): self.active = True
    def on_release(self, key): self.active = True

    def start_monitoring(self):
        #TODO THIS NOT WORKING
        with mouse.Listener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll) as listener:
            listener.start()
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.start()



mouse_tracker = ActivityMonitor()
# mouse_tracker.start_monitoring()

for i in range(10000, -1, int(-100*BRIGHTNESS_SPEED)):
    set_brightness(i/100)
    set_volume(int(i/10000))
    time.sleep(0.01)
    print(i/100)
    # if mouse_tracker.active:
    #     print('I see you.')
        

set_resolution(1024, 720)

time.sleep(3)
return_to_normal()



import time
from datetime import datetime, timedelta

def main():
    timestamp = "23:00"  # Example timestamp
    target_time = datetime.strptime(timestamp, "%H:%M")
    current_time = datetime.now()

    if current_time > target_time:
        target_time += timedelta(days=1)

    while True:
        current_time = datetime.now()
        if current_time >= target_time - timedelta(hours=1):
            set_volume(-65.25)  # Mute system volume
        if current_time >= target_time - timedelta(minutes=15):
            desaturate_screen()
        if current_time >= target_time - timedelta(minutes=5):
            set_resolution(1280, 720)
        if current_time >= target_time - timedelta(minutes=1):
            set_brightness(10)
        if current_time >= target_time:
            shutdown_computer()
            break
        if not ActivityMonitor().active:
            time.sleep(60)  # Wait for 1 minute before checking again
        time.sleep(1)

def shutdown_computer():
    import os
    # os.system("shutdown /f")
    print('SHUTDOWN INITIATED')
