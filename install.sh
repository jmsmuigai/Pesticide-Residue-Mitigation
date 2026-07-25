#!/bin/bash
set -e

echo "=== SafePlate Kenya v2 Automated Installer ==="
if [ ! -d ".venv" ]; then
  echo "Creating Virtual Environment (.venv)..."
  python3 -m venv .venv
fi

source .venv/bin/activate

echo "Installing safeplate_platform package locally..."
pip install --no-deps -e . 2>/dev/null || python3 setup.py develop

echo ""
echo "Running byte-identical self-tests..."
python3 safeplate_platform/hydrology.py
python3 safeplate_platform/washing.py
python3 safeplate_platform/gemini_agent.py

echo ""
echo "✅ SafePlate Kenya v2 installed and verified successfully!"
echo "Run 'make serve' for FastAPI docs, 'make dashboard' for Streamlit, 'make web' for web portal."
