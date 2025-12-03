#!/usr/bin/env python
import os
import subprocess
import sys

print("=" * 50)
print("Starting build process...")
print("=" * 50)
print()

print("Current directory:")
print(os.getcwd())
print()

print("Directory structure:")
os.system("ls -la")
print()

print("Checking if Healthify/static exists:")
if os.path.exists("Healthify/static"):
    print("✓ Healthify/static directory found")
    os.system("ls -la Healthify/static/")
else:
    print("✗ Healthify/static directory NOT found")
print()

print("=" * 50)
print("Collecting static files...")
print("=" * 50)
result = subprocess.run(
    ["python", "manage.py", "collectstatic", "--noinput", "--clear", "--verbosity", "2"],
    capture_output=False
)
print()

print("=" * 50)
print("Static files collected!")
print("=" * 50)
print()

print("Checking staticfiles directory:")
if os.path.exists("staticfiles"):
    print("✓ staticfiles directory created")
    print()
    print("Contents of staticfiles:")
    os.system("ls -la staticfiles/")
    print()
    
    if os.path.exists("staticfiles/login"):
        print("✓ staticfiles/login exists")
        os.system("ls -la staticfiles/login/")
    else:
        print("✗ staticfiles/login NOT found")
    print()
    
    print("Total size of staticfiles:")
    os.system("du -sh staticfiles/")
else:
    print("✗ staticfiles directory NOT created")
print()

print("=" * 50)
print("Build completed successfully!")
print("=" * 50)

sys.exit(result.returncode)
