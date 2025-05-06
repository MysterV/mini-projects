; A script to run apps with a hotkey

#SingleInstance Force

~#o::  ; Win + o (trigger/leader)
    Input, keySequence, L1 T1  ; Capture 1 key with a 1-second timeout
    ; QWERTY
    
    
    if (keySequence = "o") ; OBS
    {
        IfWinNotExist ahk_exe obs64.exe
            SetWorkingDir, A:\PlikiAplikacji\Apps\obs-studio\bin\64bit
            Run, obs64.exe
        WinWait ahk_exe obs64.exe
        WinActivate ahk_exe obs64.exe
    }
    else if (keySequence = "p") ; piano
    {
        IfWinNotExist ahk_exe Notion.exe
            run, "C:\Users\Myster\AppData\Local\Programs\Notion\Notion.exe"
        WinWait ahk_exe Notion.exe
        WinActivate ahk_exe Notion.exe
    }
    


    ; ASDFG
    else if (keySequence = "a") ; Audacity
    {
        IfWinNotExist ahk_exe Audacity.exe
            run, "C:\Program Files\Audacity\Audacity.exe"
        WinWait ahk_exe Audacity.exe
        WinActivate ahk_exe Audacity.exe
    }
    else if (keySequence = "d") ; Discord
    {
        IfWinNotExist ahk_exe Discord.exe
            run, "A:\PlikiAplikacji\Links\Communication\Discord.lnk"
        WinWait ahk_exe Discord.exe
        WinActivate ahk_exe Discord.exe
    }


    ; ZXCVB
    else if (keySequence = "z") ; Zen
    {
        IfWinNotExist ahk_exe zen.exe
            run, "A:\PlikiAplikacji\Apps\Zen Browser\zen.exe"
        WinWait ahk_exe zen.exe
        WinActivate ahk_exe zen.exe
    }
    else if (keySequence = "c") ; code
    {
        run, "explorer.exe" "A:\Docs\Courses\100 Codes"
    }
    else if (keySequence = "n") ; notes
    {
        IfWinNotExist ahk_exe obsidian.exe
            run, "A:\PlikiAplikacji\Apps\Obsidian\obsidian.exe"
        WinWait ahk_exe obsidian.exe
        WinActivate ahk_exe obsidian.exe
    }
    else if (keySequence = "m") ; musescore
    {
        IfWinNotExist ahk_exe MuseScore4.exe
            run, "A:\PlikiAplikacji\Apps\MuseScore 4\bin\MuseScore4.exe"
        WinWait ahk_exe MuseScore4.exe
        WinActivate ahk_exe MuseScore4.exe
    }
return



