import tkinter as tk
from tkinter import messagebox
import threading

def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    window.geometry(f'{window_width}x{window_height}+{x}+{y}')

def clicked():
    global count
    count += 1
    Label1.config(text=f"Times Pressed: {count}")

def upgrade():
    global count
    if count >= 100:
        messagebox.showinfo(title="Upgrade", message="Upgrade successfully purchased")
        # Startet den Timer für die automatische Erhöhung
        threading.Timer(1.0, upgrade_per_second).start()
    else:
        messagebox.showinfo(title="Upgrade", message="Not enough presses")

def upgrade_per_second():
    global count
    count += 1
    Label1.config(text=f"Times Pressed: {count}")
    # Startet den Timer für die nächste automatische Erhöhung
    threading.Timer(1.0, upgrade_per_second).start()

count = 0

root = tk.Tk()
root.title("Counter")
root.geometry("400x300")

Label1 = tk.Label(root, text=f"Times Pressed: {count}", bg="gray", fg="white", pady=5, font=(None, 10), height=1, width=20)
Label1.place(relx=0.5, rely=0.6, anchor="center")

Button1 = tk.Button(root, text="Press Here", command=clicked)
Button1.place(relx=0.5, rely=0.5, anchor="center")

Button2 = tk.Button(root, text="1 Press / sec.", command=upgrade)
Button2.place(relx=0.5, rely=0.2, anchor="center")

center_window(root)
root.mainloop()
