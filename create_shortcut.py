"""
create_shortcut.py — Creates a desktop shortcut to launch Jarvis
Run this ONCE to set up the shortcut.
"""

import os
import sys


def create_desktop_shortcut():
    try:
        import winshell
        from win32com.client import Dispatch

        desktop = winshell.desktop()
        jarvis_dir = os.path.dirname(os.path.abspath(__file__))
        main_py = os.path.join(jarvis_dir, "main.py")
        python_exe = sys.executable

        shortcut_path = os.path.join(desktop, "Jarvis.lnk")

        shell = Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.Targetpath = python_exe
        shortcut.Arguments = f'"{main_py}"'
        shortcut.WorkingDirectory = jarvis_dir
        shortcut.IconLocation = python_exe
        shortcut.Description = "Launch J.A.R.V.I.S"
        shortcut.save()

        print(f"✅ Desktop shortcut created: {shortcut_path}")
        print("You can now double-click 'Jarvis' on your desktop to launch!")

    except ImportError:
        print("Installing required packages...")
        os.system("pip install winshell pywin32")
        print("Please run this script again after installation.")
    except Exception as e:
        # Fallback — create a .bat file on desktop
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        jarvis_dir = os.path.dirname(os.path.abspath(__file__))
        main_py = os.path.join(jarvis_dir, "main.py")
        python_exe = sys.executable

        bat_path = os.path.join(desktop, "Launch Jarvis.bat")
        with open(bat_path, "w") as f:
            f.write(f'@echo off\n')
            f.write(f'cd /d "{jarvis_dir}"\n')
            f.write(f'"{python_exe}" main.py\n')
            f.write(f'pause\n')

        print(f"✅ Launcher created on Desktop: {bat_path}")
        print("Double-click 'Launch Jarvis' on your desktop to start!")


if __name__ == "__main__":
    create_desktop_shortcut()
