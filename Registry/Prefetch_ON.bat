@echo off
:: Prefetch: Monitors and caches app and boot data to load the OS and apps faster.
:: SysMain (Superfetch): Manages RAM and predicts when an app will be ran to preload the cached data into RAM before you even open the app.
:: On HDDs they're very useful and speed up OS and app load times, but on SSDs they have little to no effect, just add an unnecessary background service
:: This script turns them ON

:: If you only run software from SSD drives
::    Turning off Prefetch is mostly cosmetics (stops the OS from creating prefetch files (~40KB each) for every app)
::    Turning off SysMain reduces idle RAM usage when no (or few) apps are open, and can reduce random CPU/drive usage spikes


:: Check if running as admin (try reading OS drive's dirty bit, which requires admin rights)
fsutil dirty query %systemdrive% >nul
if %errorLevel% neq 0 (
    echo Failure: Run this script as administrator.
    pause
    exit
)


:: Enable Prefetch - registry
echo Turning on EnablePrefetcher...
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters" /v EnablePrefetcher /t REG_DWORD /d 3 /f
echo Turning on EnableSuperfetch...
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters" /v EnableSuperfetch /t REG_DWORD /d 3 /f


:: Enable SysMain (Superfetch) - services.msc
sc config SysMain start= auto
net start SysMain


echo.
:: echo Prefetch and SysMain (Superfetch) enabled successfully.
pause
