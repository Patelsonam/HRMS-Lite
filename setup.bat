@echo off
echo ======================================
echo HRMS Lite - Quick Start Script (Windows)
echo ======================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo X Python is not installed. Please install Python 3.9 or higher.
    pause
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo X Node.js is not installed. Please install Node.js 16 or higher.
    pause
    exit /b 1
)

echo + Prerequisites check passed!
echo.

REM Backend Setup
echo Setting up Backend...
cd backend

REM Create virtual environment
if not exist "venv" (
    echo Creating Python virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

REM Install dependencies
echo Installing Python dependencies...
pip install -r requirements.txt

REM Create .env if it doesn't exist
if not exist ".env" (
    echo Creating .env file...
    copy .env.example .env
    echo.
    echo IMPORTANT: Edit backend\.env and set your DATABASE_URL
    echo Example: DATABASE_URL=postgresql://username:password@localhost:5432/hrms_lite
    echo.
)

cd ..

REM Frontend Setup
echo.
echo Setting up Frontend...
cd frontend

REM Install dependencies
echo Installing Node.js dependencies...
call npm install

REM Create .env if it doesn't exist
if not exist ".env" (
    echo Creating .env file...
    copy .env.example .env
)

cd ..

echo.
echo ======================================
echo + Setup Complete!
echo ======================================
echo.
echo Next steps:
echo.
echo 1. Configure Backend Database:
echo    Edit backend\.env and set DATABASE_URL
echo.
echo 2. Create PostgreSQL Database:
echo    Open pgAdmin or use psql
echo    CREATE DATABASE hrms_lite;
echo.
echo 3. Start Backend Server:
echo    cd backend
echo    venv\Scripts\activate
echo    uvicorn app.main:app --reload
echo.
echo 4. In a new terminal, Start Frontend:
echo    cd frontend
echo    npm run dev
echo.
echo 5. Open browser:
echo    http://localhost:3000
echo.
echo ======================================
pause
