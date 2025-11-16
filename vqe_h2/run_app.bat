@echo off
REM VQE H2 Simulator - Windows Startup Script

echo.
echo ╔════════════════════════════════════════════════╗
echo ║   VQE H₂ Simulator - Streamlit Application    ║
echo ╚════════════════════════════════════════════════╝
echo.

REM Activate virtual environment
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
    echo Virtual environment activated.
) else (
    echo ERROR: Virtual environment not found!
    echo Please run: python -m venv venv
    pause
    exit /b 1
)

REM Run Streamlit app
echo.
echo Starting Streamlit application...
echo Browser will open automatically at http://localhost:8501
echo.
echo To stop the server, press Ctrl+C
echo.

streamlit run app.py

pause
