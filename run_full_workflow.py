#!/usr/bin/env python3
"""
Complete workflow: Run tests, generate dashboard, and open in browser
"""

import subprocess
import sys
import time
import webbrowser

def run_full_workflow():
    print("🚀 Starting Complete Playwright Test Workflow")
    print("=" * 60)
    
    # Step 1: Run the comprehensive tests
    print("\n📊 Step 1: Running Playwright Tests...")
    print("-" * 40)
    
    try:
        # Import and run the test suite
        import leaderboard_comprehensive_tests
        leaderboard_comprehensive_tests.run_comprehensive_tests()
        print("✅ Tests completed successfully!")
    except ImportError:
        print("❌ Could not find leaderboard_comprehensive_tests.py")
        print("💡 Make sure the test file is in the same directory")
        return
    except Exception as e:
        print(f"❌ Error running tests: {e}")
        return
    
    time.sleep(1)
    
    # Step 2: Launch the dashboard
    print("\n📈 Step 2: Launching Dashboard...")
    print("-" * 40)
    
    try:
        import test_dashboard
        test_dashboard.run_dashboard()
    except ImportError:
        print("❌ Could not find test_dashboard.py")
        return
    except Exception as e:
        print(f"❌ Error launching dashboard: {e}")
        return

if __name__ == "__main__":
    run_full_workflow()