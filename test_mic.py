import speech_recognition as sr
import time

r = sr.Recognizer()
r.dynamic_energy_threshold = False

with sr.Microphone(device_index=0) as source:
    print("Calibrating... stay quiet for 2 seconds")
    r.adjust_for_ambient_noise(source, duration=2)
    print(f"Ambient noise level: {r.energy_threshold}")
    print("Now SPEAK and press Ctrl+C when done")
    while True:
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=5)
            text = r.recognize_google(audio, language="en-IN")
            print(f"Heard: {text}")
        except sr.WaitTimeoutError:
            print("...")
        except sr.UnknownValueError:
            print("Could not understand")
        except KeyboardInterrupt:
            break