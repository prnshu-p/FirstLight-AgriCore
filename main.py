"""
FirstLight-AgriCore - Core System Entrypoint
Project First Light
"""

import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def banner():
    print("=" * 60)
    print("  [FIRST LIGHT] AGRICORE ENGINE v0.1.0")
    print("  Satellite-Powered Agricultural Intelligence System")
    print("=" * 60)

def health_check():
    print("\n[INFO] Performing subsystem diagnostics...")
    
    # Check for upcoming modules
    modules = {
        "NASA API Telemetry": "nasa_api",
        "NDVI Mathematical Models": "ndvi_calc",
    }
    
    for name, module in modules.items():
        try:
            __import__(module)
            print(f"  [+] {name}: CONNECTED")
        except ImportError:
            print(f"  [-] {name}: PENDING INTEGRATION (Awaiting Phase 1 PR)")

    print("\n[STATUS] FirstLight-AgriCore core infrastructure is ONLINE.\n")

def main():
    banner()
    health_check()

if __name__ == "__main__":
    main()
