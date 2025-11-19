@echo off
REM Setup script for Rebonato-Denev Bayesian Networks (Windows)
REM ============================================================

setlocal enabledelayedexpansion

REM Banner
echo.
echo ================================================================
echo   Rebonato-Denev Bayesian Networks Setup (Windows)
echo   Black Swan Event Modeling for Portfolio Management
echo ================================================================
echo.

REM Check for Python
echo [INFO] Checking for Python installation...
where python >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python not found! Please install Python 3.8 or higher.
    echo Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Get Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo [SUCCESS] Found Python %PYTHON_VERSION%
echo.

REM Check Python version is 3.8+
python -c "import sys; exit(0 if sys.version_info >= (3, 8) else 1)"
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python 3.8 or higher is required. Found Python %PYTHON_VERSION%
    pause
    exit /b 1
)

REM Ask for installation type
echo [INFO] Select installation type:
echo   1) Minimal (required packages only)
echo   2) Full (includes Jupyter, visualization tools)
echo   3) Development (full + dev tools)
echo.
set /p INSTALL_TYPE="Enter choice [1-3]: "

if "%INSTALL_TYPE%"=="1" (
    set REQUIREMENTS_FILE=requirements-minimal.txt
    echo [INFO] Installing minimal requirements...
) else if "%INSTALL_TYPE%"=="2" (
    set REQUIREMENTS_FILE=requirements.txt
    echo [INFO] Installing full requirements...
) else if "%INSTALL_TYPE%"=="3" (
    set REQUIREMENTS_FILE=requirements.txt
    set DEV_INSTALL=true
    echo [INFO] Installing full requirements with dev tools...
) else (
    echo [WARNING] Invalid choice. Using minimal installation.
    set REQUIREMENTS_FILE=requirements-minimal.txt
)
echo.

REM Ask about virtual environment
set /p CREATE_VENV="Create virtual environment? [y/N]: "

if /i "%CREATE_VENV%"=="y" (
    echo [INFO] Creating virtual environment...
    
    if exist venv (
        echo [WARNING] Virtual environment already exists.
        set /p RECREATE_VENV="Remove and recreate? [y/N]: "
        if /i "!RECREATE_VENV!"=="y" (
            rmdir /s /q venv
            python -m venv venv
            echo [SUCCESS] Virtual environment recreated
        )
    ) else (
        python -m venv venv
        echo [SUCCESS] Virtual environment created
    )
    
    REM Activate virtual environment
    echo [INFO] Activating virtual environment...
    call venv\Scripts\activate.bat
    echo [SUCCESS] Virtual environment activated
    
    REM Upgrade pip
    echo [INFO] Upgrading pip...
    python -m pip install --upgrade pip >nul 2>&1
    echo [SUCCESS] pip upgraded
)
echo.

REM Install requirements
echo [INFO] Installing Python packages from %REQUIREMENTS_FILE%...

if not exist "%REQUIREMENTS_FILE%" (
    echo [ERROR] Requirements file not found: %REQUIREMENTS_FILE%
    pause
    exit /b 1
)

python -m pip install -r %REQUIREMENTS_FILE%
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Package installation failed
    pause
    exit /b 1
)
echo [SUCCESS] Python packages installed successfully
echo.

REM Install development tools if requested
if "%DEV_INSTALL%"=="true" (
    echo [INFO] Installing development tools...
    python -m pip install pytest black flake8 mypy >nul 2>&1
    echo [SUCCESS] Development tools installed
    echo.
)

REM Verify installation
echo [INFO] Verifying installation...
set VERIFICATION_FAILED=0

REM Check numpy
python -c "import numpy" 2>nul
if %ERRORLEVEL% EQU 0 (
    for /f "delims=" %%i in ('python -c "import numpy; print(numpy.__version__)"') do set NUMPY_VER=%%i
    echo [SUCCESS] NumPy !NUMPY_VER! installed
) else (
    echo [ERROR] NumPy installation failed
    set VERIFICATION_FAILED=1
)

REM Check networkx
python -c "import networkx" 2>nul
if %ERRORLEVEL% EQU 0 (
    for /f "delims=" %%i in ('python -c "import networkx; print(networkx.__version__)"') do set NX_VER=%%i
    echo [SUCCESS] NetworkX !NX_VER! installed
) else (
    echo [ERROR] NetworkX installation failed
    set VERIFICATION_FAILED=1
)

REM Check matplotlib
python -c "import matplotlib" 2>nul
if %ERRORLEVEL% EQU 0 (
    for /f "delims=" %%i in ('python -c "import matplotlib; print(matplotlib.__version__)"') do set MPL_VER=%%i
    echo [SUCCESS] Matplotlib !MPL_VER! installed
) else (
    echo [ERROR] Matplotlib installation failed
    set VERIFICATION_FAILED=1
)

if %VERIFICATION_FAILED% EQU 1 (
    echo.
    echo [ERROR] Installation verification failed. Please check error messages above.
    pause
    exit /b 1
)
echo.

REM Run quick test
echo [INFO] Running quick test...
python -c "import numpy as np; import networkx as nx; import matplotlib.pyplot as plt; print('All imports successful')" 2>nul
if %ERRORLEVEL% EQU 0 (
    echo [SUCCESS] Quick test passed
) else (
    echo [ERROR] Quick test failed
    pause
    exit /b 1
)
echo.

REM Display summary
echo ================================================================
echo   SETUP COMPLETE!
echo ================================================================
echo.
echo [SUCCESS] Environment is ready to use
echo.
echo Next steps:
echo.
echo 1. Run the Eurozone model:
echo    python rebonato_denev_eurozone_crisis.py
echo.
echo 2. Run the Trump Tariffs 2025 model:
echo    python trump_tariffs_2025_blackswan.py
echo.
echo 3. Open the interactive tutorial:
echo    jupyter notebook rebonato_denev_tutorial.ipynb
echo.

if /i "%CREATE_VENV%"=="y" (
    echo Note: Virtual environment is activated. To deactivate, run:
    echo    deactivate
    echo.
)

echo Documentation:
echo   * Quick Start: QUICK_START.md
echo   * Trump Tariffs Analysis: TRUMP_TARIFFS_2025_ANALYSIS.md
echo   * Complete Index: MASTER_INDEX.md
echo.
echo [SUCCESS] Happy modeling!
echo.
pause
