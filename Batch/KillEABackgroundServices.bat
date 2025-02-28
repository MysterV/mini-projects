@echo off
tasklist /fi "ImageName eq EABackgroundService.exe" /fo csv 2>NUL | find /I "EABackgroundService.exe">NUL
if "%ERRORLEVEL%"=="0" (
	echo. && echo EA Background Services is running
	taskkill /f /t /IM EABackgroundService.exe
	echo. && echo Got rid of EA Background Services for you
) else (
	echo. && echo Seems that EA Background Services isn't running, quitting
)
timeout 20