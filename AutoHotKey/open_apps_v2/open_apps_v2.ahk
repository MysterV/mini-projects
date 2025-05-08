; Add a universal shortcut for opening apps

iniPath := A_ScriptDir . "\config.ini"

; ================================================================

#SingleInstance Force
#Persistent
#Include %A_ScriptDir%\config_loader.ahk

appConfigs := LoadINI(iniPath)


#f::  ; Trigger/leader: Win + f
    BlockInput, On
    Input, keyPressed, L1 T1  ; Capture 1 key with a 1s timeout
    BlockInput, Off
    
    FindApp(keyPressed, appConfigs)
    
return


FindApp(keybind, appConfigs) {
    ; Loop through the app configurations
    for index, app in appConfigs {
        if (keybind = app.key) {
            appExe = % app.exe
            appPath = % app.path
            
            ; set working directory
            if (app.workDir) {
                SetWorkingDir, % app.workDir
            }
            
            ; directly start new instance
            if (app.justRun = true) {
                if (app.args) {
                    appArgs = app.args
                    Run, %appPath% %appArgs%
                } else {
                    Run, %appPath%
                }
            
            ; focus window if it's running, start if not
            } else {
                IfWinNotExist, ahk_exe %appExe%
                {
                    if (app.args) {
                        Run, %appPath% %appArgs%
                    } else {
                        Run, %appPath%
                    }
                }
                if (app.exe) {
                    WinWait, ahk_exe %appExe%
                    WinActivate, ahk_exe %appExe%
                }
            }
            break
        }
    }
    return
}
