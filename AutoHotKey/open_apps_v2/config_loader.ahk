; INI config loader, made with help of Claude

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


LoadConfig(file_path, default_config_path) {
    configs := []

    ; read config file
    if !FileExist(file_path) {
        FileCopy, %default_config_path%, %file_path%
    }
    IniRead, sections, %file_path%
    
    Loop, Parse, sections, `n
    {
        section := A_LoopField
        IniRead, key, %file_path%, %section%, key, ERROR
        If (key = "ERROR")
            continue
            
        config := {key: key}
        IniRead, app_path, %file_path%, %section%, path
        IniRead, app_exe, %file_path%, %section%, exe, ERROR
        IniRead, work_dir, %file_path%, %section%, workDir, ERROR
        IniRead, app_args, %file_path%, %section%, args, ERROR
        IniRead, just_run, %file_path%, %section%, justRun, false
        
        app_path := ParseEnvVars(app_path)
        work_dir := ParseEnvVars(work_dir)

        ; add optional arguments if they exist, fetch from path otherwise
        ; exe
        If (app_exe = "ERROR")
            RegExMatch(app_path, "([^\\]+)$", app_exe)
        
        ; working directory
        If (work_dir = "ERROR")
            RegExMatch(app_path, ".*\\", work_dir)
        
        ; combine config into an object
        config.exe := app_exe
        If (app_args != "ERROR")
            config.args := app_args  ; arguments/parameters
        config.path := ParseEnvVars(app_path)
        config.workDir := ParseEnvVars(work_dir)
        config.justRun := (just_run = "true")  ; just_run
        
        configs.Push(config)
    }
    return configs
}

; Read values of environmental variables in paths
ParseEnvVars(path) {
    RegExMatch(path, "%(\w+)%", match)
    If (match)
        EnvGet, env, %match1%  ; (\w+)
        return (env != "") ? StrReplace(path, "%" match1 "%", env) : path
    return path
}
