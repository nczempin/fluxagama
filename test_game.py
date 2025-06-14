#!/usr/bin/env python3
"""
Simple test script to verify that the fluxagama game can be imported and started.
This script will start the game for a few seconds and then exit.
"""

import os
import sys
import signal
import time
import subprocess

def test_game_import():
    """Test that the game can be imported without errors."""
    try:
        import fluxagama.fluxagama
        print("✓ Game module imported successfully")
        return True
    except ImportError as e:
        print(f"✗ Failed to import game module: {e}")
        return False

def test_game_startup():
    """Test that the game can start without immediate crashes."""
    try:
        # Start the game process
        process = subprocess.Popen(
            [sys.executable, "-m", "fluxagama.fluxagama"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Let it run for 2 seconds
        time.sleep(2)
        
        # Terminate the process
        process.terminate()
        
        # Wait for it to finish and get output
        stdout, stderr = process.communicate(timeout=5)
        
        # Check if it started successfully (should load images)
        if "Loading image" in stdout or "Loading image" in stderr:
            print("✓ Game started successfully and loaded assets")
            return True
        else:
            print(f"✗ Game may not have started properly")
            print(f"stdout: {stdout}")
            print(f"stderr: {stderr}")
            return False
            
    except Exception as e:
        print(f"✗ Failed to start game: {e}")
        return False

if __name__ == "__main__":
    print("Testing Fluxagama game...")
    print()
    
    # Test import
    import_success = test_game_import()
    
    # Test startup
    startup_success = test_game_startup()
    
    print()
    if import_success and startup_success:
        print("🎉 All tests passed! The game is working correctly.")
        sys.exit(0)
    else:
        print("❌ Some tests failed.")
        sys.exit(1)