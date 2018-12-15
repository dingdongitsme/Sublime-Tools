if [%1]==[] (exit /B 1) else (set name=%1) 
:begin
cls	
@echo off
rustc -A dead_code -A unused_variables %name%
echo %ERRORLEVEL%
pause
if %ERRORLEVEL% == 0 (exit %ERRORLEVEL%) else (goto begin)
