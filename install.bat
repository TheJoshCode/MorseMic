@echo off

python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo Installing Python...
    winget install --exact --id=Python.Python
)

python -m venv venv
venv\Scripts\activate

pip install kivy torch torchvision scikit-learn speechrecognition

deactivate
