# VQE H2 Simulator - PowerShell Startup Script

Write-Host ""
Write-Host "╔════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║   VQE H₂ Simulator - Streamlit Application    ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Activate virtual environment
if (Test-Path -Path ".\venv\Scripts\Activate.ps1") {
    & ".\venv\Scripts\Activate.ps1"
    Write-Host "Virtual environment activated." -ForegroundColor Green
} else {
    Write-Host "ERROR: Virtual environment not found!" -ForegroundColor Red
    Write-Host "Please run: python -m venv venv" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Run Streamlit app
Write-Host ""
Write-Host "Starting Streamlit application..." -ForegroundColor Yellow
Write-Host "Browser will open automatically at http://localhost:8501" -ForegroundColor Green
Write-Host ""
Write-Host "To stop the server, press Ctrl+C" -ForegroundColor Yellow
Write-Host ""

streamlit run app.py

Read-Host "Press Enter to exit"
