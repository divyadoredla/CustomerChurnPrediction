@echo off
REM Quick training script for Windows

echo ========================================
echo Customer Churn Prediction - Training
echo ========================================
echo.

echo Checking Python installation...
python --version
if errorlevel 1 (
    echo ERROR: Python not found!
    pause
    exit /b 1
)

echo.
echo Starting training pipeline...
echo.

python main.py

echo.
echo ========================================
echo Training completed!
echo Check artifacts/ directory for results
echo ========================================
echo.

pause
