@echo off
title 365-Day Health Poster Studio - India
cd /d "%~dp0"
echo ========================================================
echo   365-Day Health Poster Studio - India (Doctor's PWA)
echo ========================================================
echo.
echo Launching local server and auto-detecting open port...

where python >nul 2>nul
if %ERRORLEVEL% equ 0 (
    python serve.py
    goto finish
)

where py >nul 2>nul
if %ERRORLEVEL% equ 0 (
    py serve.py
    goto finish
)

echo.
echo [ERROR] Python was not found in your system PATH.
echo You can still view the app by opening index.html directly or running a local server.
echo.
pause

:finish

