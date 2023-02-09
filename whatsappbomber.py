import pyautogui
import random
import time
import pyperclip

# Define a list of words
words = ["hello", "world", "goodbye", "python", "automation"]

# Press the "P" key
# pyautogui.press("p")
time.sleep(5)

while True:
    # Press the enter key
    pyautogui.press("enter")

    # Select a random word from the list
    word = random.choice(words)

    # Copy the selected word to the clipboard
    pyperclip.copy(word)
  

    # Paste the word at the current cursor location
    pyautogui.hotkey("ctrl", "v")

    # Check if the "S" key has been pressed
    if pyautogui.keyDown("s"):
        break