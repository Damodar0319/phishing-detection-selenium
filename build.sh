#!/usr/bin/env bash
# Exit on error
set -o errexit

echo "Installing pip requirements..."
pip install --upgrade pip
pip install -r requirements.txt

# Since we are not using Docker, we must explicitly ensure the system 
# caches the Chromium binaries correctly via Playwright's dependency manager
# (Render's internal OS allows Playwright to install system Chrome dependencies)
echo "Installing browser dependencies..."
pip install playwright
playwright install chromium
playwright install-deps chromium

echo "Build complete!"
