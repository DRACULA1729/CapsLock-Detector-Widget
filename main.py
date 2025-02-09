#Basic design but robust script
#################################################Developed by Sushant Pandey########################################################

import tkinter as tk
import keyboard

caps_lock_state = False  # Track Caps Lock state manually

def toggle_caps_lock():
    global caps_lock_state
    caps_lock_state = not caps_lock_state
    update_label()

def update_label():
    label.config(text="Caps Lock: ON" if caps_lock_state else "Caps Lock: OFF", fg="red" if caps_lock_state else "green")

# Initialize GUI
root = tk.Tk()
root.title("Caps Lock Indicator")
root.geometry("200x50")
root.resizable(False, False)
root.attributes("-topmost",True)  # Keep window on top


label = tk.Label(root, text="Caps Lock: OFF", font=("Arial", 14))
label.pack(expand=True)

keyboard.on_press_key("caps lock", lambda event: toggle_caps_lock())  # Detect Caps Lock key press

root.mainloop()
