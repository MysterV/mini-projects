param ([Parameter(Mandatory)][int]$minutes)
#creating object as WScript
$wshell = New-Object -ComObject Wscript.Shell -ErrorAction Stop

# warning with accounting for grammar
if ($minutes -eq 1){
#minute
$code = $wshell.Popup("One minute till forced pc hibernation.`nWould you like to hibernate now?",0,"This is your last warning",48+4)
}

else{
#minutes
$code = $wshell.Popup("$minutes minutes till force pc hibernation.`nWould you like to hibernate now?",0,"Sleep is imminent",48+4)
}

#Hibernation confirmation
# yes - 6, no - 7
if ($code -eq 6) {
    $code2 = $wshell.Popup("Are you sure you want to hibernate the computer now?",0,"WARNING",48+4)
    if ($code2 -eq 6){shutdown /h}
}


