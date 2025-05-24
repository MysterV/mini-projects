# I suggest making a backup just in case

import os
import win32com.client
import time
import pylnk3


# ===== CONFIG =====
FOLDER_PATHS = [r".", r"D:\Writable\Links", r"G:\Writable\Links", r"%sw%\Links"]
REPLACEMENTS = {
    r"%sw%": [r"A:\PlikiAplikacji", r"D:\PlikiAplikacji", r"G:\PlikiAplikacji", r"%PlikiAplikacji%", r"%MyAppData%"],
    r"%AppData%": [r"C:\Users\Myster\AppData\Roaming", r"%userprofile%\AppData\Roaming"],
    r"%LocalAppData%": [r"C:\Users\Myster\AppData\Local", r"%userprofile%\AppData\Local"],
    r"%userprofile%": [r"C:\Users\User", r"C:\Users\Myster"]
}
SHOW_UNCHANGED = False

# Convert environment variables to actual paths
# WARNING: Irreversible, converts ALL environmental variables to paths, not just the ones configured above
EXPAND_VARS = False


# ===== CODE =====


# read target path, preserving env vars (Windows API won't work as it expands all variables)
def get_target_path(lnk_path):
    with open(lnk_path, 'rb') as f:
        lnk = pylnk3.parse(f)

    extra = lnk.extra_data.blocks
    for block in extra:
        if block._signature == 0xA0000001:  # if block == ExtraDataBlock
            if block.target_unicode:
                return block.target_unicode
    return None


# Initialize COM shell
shell = win32com.client.Dispatch("WScript.Shell")

start_time = time.time()
all_mod_counts = []
all_file_counts = []
for FOLDER in FOLDER_PATHS:
    FOLDER = os.path.expandvars(FOLDER)
    print(f'Starting conversion in "{FOLDER}"')
    mod_count = 0
    file_count = 0
    local_start_time = time.time()
    for root, _, files in os.walk(FOLDER):
        for filename in files:
            if filename.lower().endswith(".lnk"):
                file_count += 1
                shortcut_path = os.path.join(root, filename)
                shortcut = shell.CreateShortcut(shortcut_path)
                # save original paths for comparison
                unexpanded_target = get_target_path(shortcut_path)
                if unexpanded_target: target = unexpanded_target
                else: target = shortcut.TargetPath
                # print(target)
                start = shortcut.WorkingDirectory
                

                # Target path
                mod_target = False
                new_target = ''
                for replacement, old_prefixes in REPLACEMENTS.items():
                    for prefix in old_prefixes:
                        if target.upper().startswith(prefix.upper()):
                            # replace
                            new_target = target.replace(prefix, replacement, 1)
                            # write changes
                            shortcut.TargetPath = new_target
                            mod_target = True
                            break
                    if mod_target: break

                # Working directory (aka "start in") path
                mod_start = False
                new_start = ''
                for replacement, old_prefixes in REPLACEMENTS.items():
                    for prefix in old_prefixes:
                        if start.upper().startswith(prefix.upper()):
                            # replace
                            new_start = start.replace(prefix, replacement, 1)
                            # write changes
                            shortcut.WorkingDirectory = new_start
                            mod_start = True
                            break
                    if mod_start: break
                
                # Expand variables globally, regardless of whether they were modified
                if EXPAND_VARS:
                    if not new_target: new_target = target
                    if not new_start: new_start = start
                    expanded_target = os.path.expandvars(shortcut.TargetPath)
                    expanded_start = os.path.expandvars(shortcut.WorkingDirectory)
                    
                    if expanded_target != new_target:
                        shortcut.TargetPath = expanded_target
                        mod_target = True
                    if expanded_start != new_start:
                        shortcut.WorkingDirectory = expanded_start 
                        mod_start = True

                if mod_target or mod_start:
                    shortcut.Save()
                    mod_count += 1
                    print(f"\n[Updated] {shortcut_path}")
                    if mod_target:
                        print(f'target: {target} --> {new_target}')
                    if mod_start:
                        print(f'start in: {start} --> {new_start}')
                    print()  # newline
                elif SHOW_UNCHANGED:
                    print(f"[Unchanged] {shortcut_path}")
    all_mod_counts.append(mod_count)
    all_file_counts.append(file_count)

    print(f'Modified {mod_count}/{file_count} links found in "{FOLDER}"\nTime: {(time.time() - local_start_time):.6f}s\n')
print(f'\nDone! Modified {sum(all_mod_counts)}/{sum(all_file_counts)} links found in total across:')
for dir in range(len(FOLDER_PATHS)):
    print(f'{FOLDER_PATHS[dir]} ({all_mod_counts[dir]}/{all_file_counts[dir]})')
print(f'Total time: {(time.time() - start_time):.6f}s')
