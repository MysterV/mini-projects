; Add a universal shortcut for opening apps

config_path := A_ScriptDir . "\config.ini"
default_config_path := "default_config.ini"

; ================================================================

#SingleInstance Force
#Persistent
#Include %A_ScriptDir%\config_loader.ahk
#Include %A_ScriptDir%\app_loader.ahk

app_configs := LoadConfig(config_path, default_config_path)  ; from config_loader.ahk

; Trigger/leader: [Win] + [F]
#f::  
    ; Wait for [Win] and [F] to be released
    KeyWait, LWin
    KeyWait, f

    BlockInput, On
    Input, key_pressed, L1 T1, {Esc}
    BlockInput, Off
    
    if (key_pressed) {
        LoadApp(key_pressed, app_configs)  ; from app_loader.ahk
    }
return

