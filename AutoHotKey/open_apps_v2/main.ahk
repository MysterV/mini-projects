; Add a universal shortcut for opening apps

iniPath := A_ScriptDir . "\config.ini"

; ================================================================

#SingleInstance Force
#Persistent
#Include %A_ScriptDir%\config_loader.ahk
#Include %A_ScriptDir%\app_loader.ahk

appConfigs := LoadINI(iniPath)  ; from config_loader.ahk

; Trigger/leader: [Win] + [F]
#f::  
    ; Wait for [Win] and [F] to be released
    KeyWait, LWin
    KeyWait, f

    BlockInput, On
    Input, keyPressed, L1 T1, {Esc}
    BlockInput, Off
    
    if (keyPressed) {
        FindApp(keyPressed, appConfigs)  ; from app_loader.ahk
    }
return

