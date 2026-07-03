@echo off
REM Quick launch script for Streamlit app (Windows)

echo ========================================
echo Customer Churn Prediction - Dashboard
echo ========================================
echo.

echo Launching Streamlit dashboard...
echo Dashboard will open at: http://localhost:8501
echo.

streamlit run app.py

pause
