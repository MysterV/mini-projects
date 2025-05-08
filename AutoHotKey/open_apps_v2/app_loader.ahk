LoadApp(keybind, appConfigs) {
    ; Loop through the app configurations
    for index, app in appConfigs {
        ; if found a match for pressed key in the configs
        if (keybind = app.key) {
            appPath := app.path
            appExe := app.exe
            appArgs := app.args
            appWorkDir := app.workDir
            ; MsgBox %appPath% %appExe% %appArgs% %appWorkDir%

            ; set working directory
            ; if workDir was set to empty or unset, and path is just filename, e.g. cmd.exe, it's set to the script's directory
            SetWorkingDir, %appWorkDir%
            
            ; if justRun=true, skip checks and start new instance
            if (app.justRun = true) {
                Run, %appPath% %appArgs%
            
            ; focus window if it's running, start if not
            ; TODO: debug explorer special treatment
            } else if (appExe = "explorer.exe") {
                foundExplorer := false
                for window in ComObjCreate("Shell.Application").Windows
                    if (InStr(window.FullName, "explorer.exe")) {
                        WinGetTitle, winTitle, % "ahk_id " window.hwnd
                        ; Check if the title matches the path
                        if (InStr(winTitle, appPath)) {
                            WinActivate, % "ahk_id " window.hwnd
                            foundExplorer := true
                            break
                        }
                    }
                if (!foundExplorer) {
                    Run, explorer.exe %appArgs%
                    WinWait, ahk_class CabinetWClass
                    WinActivate, ahk_class CabinetWClass
                }
            ; other apps - focus window if running, start if not
            } else {
                IfWinNotExist, ahk_exe %appExe%
                    Run, %appPath% %appArgs%
                WinWait, ahk_exe %appExe%
                WinActivate, ahk_exe %appExe%
            }
            break
        }
    }
    return
}
