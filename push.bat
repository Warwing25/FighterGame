@echo off
REM Quick push script for FighterGame
REM Usage: push.bat "Your commit message here"

if "%~1"=="" (
    echo Usage: push.bat "commit message"
    exit /b 1
)

git add -A
git commit -m "%~1"
git push origin main

echo Pushed to GitHub successfully.
