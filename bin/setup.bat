#!/bin/bash
@echo off
echo "****************************************"
echo " Setting up Capstone Environment"
echo "****************************************"


echo "Checking the Python version..."
python --version

echo "Creating a Python virtual environment"
python -m venv backend-Bot-venv

echo "Installing Python depenencies..."
call backend-Bot-venv/Scripts/activate.bat
call backend-Bot-venv/Scripts/activate
pip install -r requirements.txt

echo "****************************************"
echo " Capstone Environment Setup Complete"
echo "****************************************"
echo ""
echo "Use 'exit' to close this terminal and open a new one to initialize the environment"
echo ""
flask --app app --debug run 