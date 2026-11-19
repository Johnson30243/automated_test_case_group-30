@echo off
cd /d "%~dp0"
py main.py
if errorlevel 1 (
  echo.
  echo Could not start the application. Confirm Python and Tkinter are installed.
  pause
)
