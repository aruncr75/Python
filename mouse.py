import pyautogui
import time

recording = False
movements = []

print("Press 'p' to start recording, 's' to stop, 'r' to replay and 'm' to print recorded movements")

while True:
    key = input()
    if key == 'p':
        recording = True
        print("Recording started.")
    elif key == 's':
        recording = False
        print("Recording stopped.")
    elif key == 'r':
        print("Replaying...")
        for x, y in movements:
                pyautogui.moveTo(x, y)
    elif key == 'm':
     if len(movements)==0:
        print("No movements recorded yet")
    else:
     print("Recorded Movements:")
    for x, y in movements:
        print(f"X: {x}, Y: {y}")
    if recording:
        x, y = pyautogui.position()
        movements.append((x, y))
        time.sleep(0.1)