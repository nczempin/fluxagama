#!/bin/bash

# Fluxagama Setup Script for Ubuntu
# This script installs Python 3, pip, and game dependencies

set -e  # Exit on error

echo "=== Fluxagama Setup Script for Ubuntu ==="
echo

# Check if Python 3 is installed
if command -v python3 &> /dev/null; then
    echo "✓ Python 3 is already installed ($(python3 --version))"
else
    echo "Installing Python 3..."
    sudo apt-get update
    sudo apt-get install -y python3 python3-dev
fi

# Check if pip is installed
if command -v pip3 &> /dev/null; then
    echo "✓ pip is already installed ($(pip3 --version))"
else
    echo "Installing pip..."
    sudo apt-get install -y python3-pip
fi

# Check if pygame system dependencies are installed
if dpkg -l | grep -q libsdl2-dev; then
    echo "✓ SDL dependencies are already installed"
else
    echo "Installing SDL dependencies for pygame..."
    sudo apt-get install -y python3-pygame libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev
fi

# Check if virtual environment exists
if [ -d "venv" ]; then
    echo "✓ Virtual environment already exists"
else
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment and install/update dependencies
echo "Checking Python dependencies..."
source venv/bin/activate

# Check if fluxagama is installed
if pip show fluxagama &> /dev/null; then
    echo "✓ fluxagama is already installed"
    echo "  To update dependencies, run: pip install -r requirements.txt --upgrade"
else
    echo "Installing Python dependencies..."
    pip install --upgrade pip
    pip install -r requirements.txt
    
    # Install the package in development mode
    echo "Installing fluxagama in development mode..."
    pip install -e .
fi

echo
echo "=== Setup Complete! ==="
echo
echo "To run the game:"
echo "  source venv/bin/activate  # Activate virtual environment"
echo "  python -m fluxagama.fluxagama"
echo
echo "Or without virtual environment:"
echo "  python3 -m fluxagama.fluxagama"