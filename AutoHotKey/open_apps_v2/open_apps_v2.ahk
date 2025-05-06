; Add a universal shortcut for opening apps, refactored by Claude to simplify the process


configFilePath := A_ScriptDir . "\config.ini"

; =======================================================================================

#SingleInstance Force
#Persistent

appConfigs := LoadAppConfigs(configFilePath)


#f::  ; Trigger/leader: Win + f
    BlockInput, On
    Input, keyPressed, L1 T1  ; Capture 1 key with a 1s timeout
    BlockInput, Off
    
    FindApp(keyPressed, appConfigs)
    
return


LoadAppConfigs(filePath) {
    configs := []
    IniRead, sections, %filePath%
    
    Loop, Parse, sections, `n
    {
        section := A_LoopField
        IniRead, key, %filePath%, %section%, key, ERROR
        if (key = "ERROR")
            continue
            
        config := {key: key}
        IniRead, configExe, %filePath%, %section%, exe, 
        IniRead, configPath, %filePath%, %section%, path, 
        IniRead, configWorkDir, %filePath%, %section%, workDir, ERROR
        IniRead, configArgs, %filePath%, %section%, args, ERROR
        IniRead, configJustRun, %filePath%, %section%, justRun, false

        config.exe := configExe
        config.path := configPath
        config.justRun := %configJustRun%
        if (configWorkDir != "ERROR")
            config.workDir := configWorkDir
        if (configArgs != "ERROR")
            config.args := configArgs
        
        configs.Push(config)
    }
    return configs
}


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
}
