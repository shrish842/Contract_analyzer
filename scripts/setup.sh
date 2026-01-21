#!/bin/bash
# Setup script for Contract Risk Analyzer

echo "Setting up Contract Risk Analyzer..."

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_sm

# Create necessary directories
mkdir -p logs
mkdir -p models

echo "Setup complete! Activate the virtual environment with: source venv/bin/activate"
