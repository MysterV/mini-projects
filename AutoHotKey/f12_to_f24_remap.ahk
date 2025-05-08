; Remaps function keys F1-F12 to F13-F24
; only after [Win] + [Insert] is pressed

sequenceTriggered := false

; ================================================================

#SingleInstance Force
#Persistent

; Trigger/leader: [Win] + [Insert]
#Insert::
    ; Wait for trigger to be released
    KeyWait, LWin
    KeyWait, Insert
    sequenceTriggered := true
    SetTimer, ResetSequence, -1000  ; Reset after 1 second if no key is pressed
return


#If sequenceTriggered
F1::F24Remap(1)
F2::F24Remap(2)
F3::F24Remap(3)
F4::F24Remap(4)
F5::F24Remap(5)
F6::F24Remap(6)
F7::F24Remap(7)
F8::F24Remap(8)
F9::F24Remap(9)
F10::F24Remap(10)
F11::F24Remap(11)
F12::F24Remap(12)

#If  ; End conditional hotkey

ResetSequence:  ; Reset sequence if no key pressed after 1 second
    sequenceTriggered := false
return

F24Remap(key) {
    global sequenceTriggered
    sequenceTriggered := false  ; Reset sequence
    newKey := key + 12
    Send, {F%newKey%}
    return
}
