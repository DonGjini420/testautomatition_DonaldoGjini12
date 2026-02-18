@echo off
REM ============================================================================
REM k6 Load Test Runner Script
REM ============================================================================
REM Denna fil låter dig köra k6 load tests enkelt
REM Användning: k6_run.bat [test_fil]
REM Exempel: k6_run.bat k6/load_test.js

setlocal enabledelayedexpansion

set K6_EXE=C:\Users\User\k6\k6-v0.50.0-windows-amd64\k6.exe

if "%1"=="" (
    echo.
    echo ============================================
    echo k6 Load Test Runner
    echo ============================================
    echo.
    echo Användning: k6_run.bat [test_fil]
    echo Exempel: k6_run.bat k6/load_test.js
    echo.
    exit /b 1
)

echo.
echo ============================================
echo k6 Load Test - Soderbröder Loan Lab
echo ============================================
echo Test fil: %1
echo.
echo Starting load test...
echo.

%K6_EXE% run %1

pause
