; INI config loader, made with help of Claude

LoadINI(filePath) {
    configs := []
    IniRead, sections, %filePath%
    
    Loop, Parse, sections, `n
    {
        section := A_LoopField
        IniRead, key, %filePath%, %section%, key, ERROR
        if (key = "ERROR")
            continue
            
        config := {key: key}
        IniRead, configPath, %filePath%, %section%, path, 
        IniRead, configExe, %filePath%, %section%, customExe, ERROR
        IniRead, configWorkDir, %filePath%, %section%, workDir, ERROR
        IniRead, configArgs, %filePath%, %section%, args, ERROR
        IniRead, configJustRun, %filePath%, %section%, justRun, false

        config.path := configPath

        ; add optional arguments if they exist, fetch from path otherwise
        ; exe
        if (configExe = "ERROR") {
            RegExMatch(configPath, "([^\\]+)$", configExe)
        }
        config.exe := configExe

        ; working directory
        if (configWorkDir = "ERROR") {
            RegExMatch(configPath, ".*\\", configWorkDir)
        }
        config.workDir := configWorkDir

        ; parameters
        if (configArgs != "ERROR"){
            config.args := configArgs
        }
        ; justRun
        config.justRun := (configJustRun = "true")
        
        configs.Push(config)
    }
    return configs
}

; LoadAppConfigs(iniPath) {
;     global iniPath
;     if (FileExist(iniPath)) {
;         configs := LoadINI(iniPath)
;     } else {
;         MsgBox, No configuration files found!
;         configs := []
;     }
;     return configs
; }
