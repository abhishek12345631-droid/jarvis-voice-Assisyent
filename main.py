"""
JARVIS — Full Build v8
Face security + Unknown visitor + Whisper voice + System tray + Hotkey
"""

import threading
import tkinter as tk
import time
from jarvis.listener import listen
from jarvis.speaker import speak
from jarvis.commands import handle_command
from jarvis.utils import get_greeting
from jarvis.hud import JarvisHUD
from jarvis.jarvis_face import JarvisFace

root = None
hud = None
face = None
_active = True


def update_hud(fn, *args):
    try:
        if root:
            root.after(0, lambda: fn(*args))
    except:
        pass


def update_face(speaking: bool):
    try:
        if face and root:
            root.after(0, lambda: face.set_speaking(speaking))
    except:
        pass


def _handle_with_hud(command):
    import jarvis.speaker as spk
    original = spk.speak

    def patched(text):
        update_face(True)
        original(text)
        update_face(False)
        update_hud(hud.add_jarvis_message, text)

    spk.speak = patched
    handle_command(command)
    spk.speak = original


def jarvis_loop():
    time.sleep(1.5)

    # ── Face security scan ──
    try:
        from jarvis.face_security import verify_and_greet
        update_hud(hud.add_system_message, "Running security scan...")
        update_hud(hud.set_status, "SCANNING", "#ffaa00")
        name = verify_and_greet(speak, listen)
        if name and name != "Unknown":
            greeting = f"Welcome {name}! {get_greeting()}"
        else:
            greeting = get_greeting()
        update_hud(hud.add_system_message, f"User: {name}")
    except Exception as e:
        print(f"Security scan skipped: {e}")
        greeting = get_greeting()
        speak(greeting)

    update_hud(hud.add_system_message, "Ready! Speak your command...")
    update_hud(hud.set_status, "ONLINE", "#00ff88")

    while _active:
        try:
            update_hud(hud.set_mode, "LISTENING")
            update_hud(hud.set_status, "ONLINE", "#00ff88")

            command = listen()
            if not command:
                continue

            update_hud(hud.add_user_message, command)
            update_hud(hud.set_mode, "THINKING...")
            update_hud(hud.set_status, "PROCESSING", "#00d4ff")

            if any(w in command for w in ["exit", "goodbye", "shut down", "shutdown"]):
                speak("Goodbye! Shutting down.")
                update_hud(hud.add_jarvis_message, "Goodbye!")
                root.after(1500, root.quit)
                break

            _handle_with_hud(command)

        except Exception as e:
            print(f"Loop error: {e}")
            continue


def run():
    global root, hud, face

    root = tk.Tk()
    root.withdraw()

    hud = JarvisHUD()
    face = JarvisFace()
    face.root.geometry("520x640+860+30")

    hud.root.protocol("WM_DELETE_WINDOW", root.quit)
    face.root.protocol("WM_DELETE_WINDOW", root.quit)

    # ── System tray ──
    try:
        from jarvis.tray import setup_tray, setup_hotkey
        def on_activate():
            hud.root.deiconify()
            face.root.deiconify()
        def on_quit():
            root.quit()
        setup_tray(on_activate, on_quit)
        setup_hotkey(on_activate)
    except Exception as e:
        print(f"Tray setup skipped: {e}")

    t = threading.Thread(target=jarvis_loop, daemon=True)
    t.start()

    root.mainloop()


if __name__ == "__main__":
    run()
