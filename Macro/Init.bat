@echo off
echo Installing necessary libraries for macro.py...

REM Ensure pip is up-to-date
python -m pip install --upgrade pip

REM Install required libraries
pip install pyautogui
pip install keyboard
pip install json

echo Libraries installed successfully.
pause