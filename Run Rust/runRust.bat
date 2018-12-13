if [%1]==[] (exit /B 1) else (set name=%1) 
cls	
@echo off
rustc -A dead_code -A unused_variables %name%
pause
exit /B %ERRORLEVEL%