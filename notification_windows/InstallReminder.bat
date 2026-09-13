@echo off

title Mental Math Challenge - Daily Workout

echo ==========================================
echo   Mental Math Challenge
echo   Installing Daily Workout Reminder
echo ==========================================
echo.


REM ============================================================
REM FIND DAILY REMINDER
REM ============================================================

set "REMINDER=%~dp0DailyReminder.exe"


REM ============================================================
REM CHECK FILE
REM ============================================================

if not exist "%REMINDER%" (
    echo ERROR:
    echo DailyReminder.exe was not found.
    echo.
    pause
    exit /b 1
)


REM ============================================================
REM CREATE DAILY TASK
REM ============================================================

schtasks /Create ^
 /TN "Mental Math Challenge - Daily Workout" ^
 /TR "\"%REMINDER%\"" ^
 /SC DAILY ^
 /ST 07:00 ^
 /F


REM ============================================================
REM CHECK RESULT
REM ============================================================

if %ERRORLEVEL% EQU 0 (

    echo.
    echo ==========================================
    echo   Daily Workout installed successfully!
    echo ==========================================
    echo.
    echo Reminder time: 07:00
    echo.
    echo The reminder will run every day.
    echo.

) else (

    echo.
    echo ==========================================
    echo   ERROR: Could not create Task
    echo ==========================================
    echo.
)


pause