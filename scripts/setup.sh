#!/bin/bash

# Fluxagama Setup Script for Ubuntu
# This script installs Python 3, pip, and game dependencies

set -e  # Exit on error

echo "=== Fluxagama Setup Script for Ubuntu ==="
echo

# Update package list
echo "Updating package list..."
sudo apt-get update

# Install Python 3 and pip
echo "Installing Python 3 and pip..."
sudo apt-get install -y python3 python3-pip python3-dev

# Install SDL dependencies for pygame
echo "Installing SDL dependencies for pygame..."
sudo apt-get install -y python3-pygame libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev

# Create virtual environment (optional but recommended)
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment and install dependencies
echo "Installing Python dependencies..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Install the package in development mode
echo "Installing fluxagama in development mode..."
pip install -e .

echo
echo "=== Setup Complete! ==="
echo
echo "To run the game:"
echo "  source venv/bin/activate  # Activate virtual environment"
echo "  python -m fluxagama.fluxagama"
echo
echo "Or without virtual environment:"
echo "  python3 -m fluxagama.fluxagama"