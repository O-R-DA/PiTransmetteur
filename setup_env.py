import os
import subprocess
import sys

def install_packages():
    packages = [
        "paramiko",
        "pyqt5"
    ]
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    print("Installation des packages...")
    install_packages()
    print("Installation terminée.")

if __name__ == "__main__":
    main()
