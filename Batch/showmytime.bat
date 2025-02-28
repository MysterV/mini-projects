set MTIME=%time::=-%
(
time /t 
echo %random%
) >> "log_%MTIME:,=-%.txt"

15-28