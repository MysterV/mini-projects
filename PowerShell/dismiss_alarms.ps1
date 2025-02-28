[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] | Out-Null
$ToastHistory = [Windows.UI.Notifications.ToastNotificationManager]::History
$ToastHistory.Clear('Microsoft.WindowsAlarms_8wekyb3d8bbwe!App')