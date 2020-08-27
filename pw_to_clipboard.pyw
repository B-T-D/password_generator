"""Generates a password of 10 random characters and copies it to the system
clipboard. Quick one-click script intended for ease of use."""

import pw_main as pwm
from tkinter import Tk
import win32clipboard as w32cb

def copy_to_clipboard(password):
    """Copy to clipboard using pywin32."""
    w32cb.OpenClipboard()
    w32cb.EmptyClipboard()
    w32cb.SetClipboardText(password)
    w32cb.CloseClipboard()

def main():
    characters = pwm.get_chars()
    password = pwm.generate_pw(10, characters)
    copy_to_clipboard(password)

if __name__ == '__main__':
    main()
