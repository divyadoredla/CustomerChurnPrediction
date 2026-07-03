@echo off
echo ====================================
echo Installing Dependencies
echo ====================================

echo.
echo Upgrading pip...
python -m pip install --upgrade pip

echo.
echo Installing requirements...
pip install -r requirements.txt

echo.
echo Verifying installation...
python -c "import pandas; import numpy; import sklearn; import xgboost; import streamlit; print('SUCCESS: All packages installed correctly!')"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ====================================
    echo Installation Complete!
    echo ====================================
    echo.
    echo To run the training pipeline: python main.py
    echo To launch the dashboard: streamlit run app.py
) else (
    echo.
    echo ====================================
    echo Installation Failed!
    echo ====================================
    echo Try using: pip install -r requirements_locked.txt
)

pause
