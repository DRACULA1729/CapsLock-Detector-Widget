#Not so Good design but good design.
#################################################Developed by Sushant Pandey########################################################


import tkinter as tk
import keyboard
from tkinter import Canvas

def create_rounded_rect(canvas, x1, y1, x2, y2, radius, **kwargs):
    """Draw a rounded rectangle on the canvas."""
    points = [
        (x1 + radius, y1), (x2 - radius, y1),
        (x2, y1, x2, y1 + radius), (x2, y2 - radius),
        (x2, y2, x2 - radius, y2), (x1 + radius, y2),
        (x1, y2, x1, y2 - radius), (x1, y1 + radius),
        (x1, y1, x1 + radius, y1)
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)

caps_lock_state = False  # Track Caps Lock state manually

def toggle_caps_lock():
    global caps_lock_state
    caps_lock_state = not caps_lock_state
    update_label()

def update_label():
    label.config(text="Caps Lock: ON" if caps_lock_state else "Caps Lock: OFF")
    canvas.itemconfig(bg_rect, fill="#FFB6C1" if caps_lock_state else "#ADD8E6")
    label.config(fg="#333333" if caps_lock_state else "#222222")

# Initialize GUI
root = tk.Tk()
root.title("Caps Lock Indicator")
root.geometry("200x100")  # Decreased window size
root.resizable(False, False)
root.attributes("-topmost", True)  # Keep the window always on top
root.configure(bg="#ADD8E6")  # Light blue gradient background

# Position window in the top right corner
screen_width = root.winfo_screenwidth()
root.geometry(f"200x100+{screen_width - 210}+10")

# Create a canvas for rounded corners and gradient effect
canvas = Canvas(root, width=200, height=100, highlightthickness=0, bg="#ADD8E6")
canvas.pack(fill="both", expand=True)

# Create a rounded rectangle with shadow effect
shadow = create_rounded_rect(canvas, 10, 10, 190, 90, radius=15, fill="#A9C9FF", outline="")
bg_rect = create_rounded_rect(canvas, 5, 5, 185, 85, radius=15, fill="#ADD8E6", outline="")

# Create label with custom font and better styling
try:
    label_font = ("Crustaceans Signature DEMO", 14, "bold")
except:
    label_font = ("Arial", 14, "bold")  # Fallback if the font isn't available

label = tk.Label(root, text="Caps Lock: OFF", font=label_font, fg="#222222", bg="#ADD8E6")
label.place(relx=0.5, rely=0.5, anchor="center")

keyboard.on_press_key("caps lock", lambda event: toggle_caps_lock())  # Detect Caps Lock key press

root.mainloop()
