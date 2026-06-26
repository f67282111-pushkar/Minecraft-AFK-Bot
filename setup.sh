#!/bin/bash

# Aternos 24/7 AFK Bot Setup Script for BloodstealSMP

echo "================================"
echo "🤖 AFK Bot Setup - BloodstealSMP"
echo "================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.7 or higher."
    exit 1
fi

echo "✓ Python is installed"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✓ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo ""
echo "================================"
echo "✅ Setup Complete!"
echo "================================"
echo ""
echo "To start the bot, run:"
echo "  python afk_bot.py"
echo ""
echo "Configuration:"
echo "  Server: BloodstealSMP-Fewe.aternos.me:18611"
echo "  Username: f67282111"
echo ""
echo "To stop the bot, press Ctrl+C"
echo ""
