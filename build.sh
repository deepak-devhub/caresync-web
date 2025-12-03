#!/bin/bash
set -e

echo "================================"
echo "Starting build process..."
echo "================================"

echo ""
echo "Current directory:"
pwd

echo ""
echo "Directory structure:"
ls -la

echo ""
echo "Checking if Healthify/static exists:"
if [ -d "Healthify/static" ]; then
    echo "✓ Healthify/static directory found"
    ls -la Healthify/static/
else
    echo "✗ Healthify/static directory NOT found"
fi

echo ""
echo "================================"
echo "Installing dependencies..."
echo "================================"
pip install -r requirements.txt

echo ""
echo "================================"
echo "Collecting static files..."
echo "================================"
python manage.py collectstatic --noinput --clear --verbosity 2

echo ""
echo "================================"
echo "Static files collected!"
echo "================================"

echo ""
echo "Checking staticfiles directory:"
if [ -d "staticfiles" ]; then
    echo "✓ staticfiles directory created"
    echo ""
    echo "Contents of staticfiles:"
    ls -la staticfiles/
    
    echo ""
    echo "Checking for login static files:"
    if [ -d "staticfiles/login" ]; then
        echo "✓ staticfiles/login exists"
        ls -la staticfiles/login/
    else
        echo "✗ staticfiles/login NOT found"
    fi
    
    echo ""
    echo "Total size of staticfiles:"
    du -sh staticfiles/
else
    echo "✗ staticfiles directory NOT created"
fi

echo ""
echo "================================"
echo "Build completed successfully!"
echo "================================"
