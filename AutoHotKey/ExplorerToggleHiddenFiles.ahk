; Pressing CTRL + H while Windows Explorer is focused toggles visibility of all hidden files



#SingleInstance Force

#IfWinActive ahk_class CabinetWClass ahk_exe explorer.exe

; CTRL + H
^h::

RegRead, hidden, HKCU, Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced, Hidden  ; Get If Files Hidden Or Shown

If hidden contains 1  ; IF Files NOT Hidden
{
    RegWrite, REG_DWORD, HKCU, Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced, Hidden, 2  ; Hide Hidden Files
}

Else  ; ELSE Files Hidden
{
    RegWrite, REG_DWORD, HKCU, Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced, Hidden, 1  ; Show Hidden Files
}

WinGet, windows, List, ahk_exe explorer.exe  ; Get List Explorer Windows
Loop, %windows%
{
    id := windows%A_Index%  ; id
    WinGetTitle, title, ahk_id %id%  ; title
    WinGetClass, class, ahk_id %id%  ; class
    WinGet, exe, ProcessName, ahk_id %id%  ; exe
    ControlSend, DirectUIHWND2, {F5}, %title% ahk_class %class% ahk_exe %exe%  ; Refresh All Explorer Windows
}
Return

#IfWinActive