import os
import sys
import tkinter as tk
import winsound  # Import winsound module for playing beep sound

def load_asset(path):
    base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    assets = os.path.join(base, "assets")
    return os.path.join(assets, path)

# Function to play beep sound
def play_beep():
    frequency = 2500  # Set frequency (in Hz)
    duration = 100  # Set duration (in milliseconds)
    winsound.Beep(frequency, duration)

window = tk.Tk()
window.geometry("324x487")
window.configure(bg="#ffffff")
window.title("Untitled")

canvas = tk.Canvas(
    window,
    bg="#ffffff",
    width=324,
    height=487,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_1 = tk.PhotoImage(file=load_asset("image_1.png"))
canvas.create_image(162, 243, image=image_1)

# Create text labels above the buttons
drawer_label = tk.Label(window, text="Drawer", bg="#ffffff", fg="#000000", font=("Lucida Sans", 18))
drawer_label.place(x=17, y=50)

admin_label = tk.Label(window, text="Admin", bg="#ffffff", fg="#000000", font=("Lucida Sans", 18))
admin_label.place(x=121, y=50)

logs_label = tk.Label(window, text="Logs", bg="#ffffff", fg="#000000", font=("Lucida Sans", 18))
logs_label.place(x=229, y=50)

main_draw_label = tk.Label(window, text="Main Draw", bg="#ffffff", fg="#1ba6df", font=("Lucida Sans", 18))
main_draw_label.place(x=135, y=340)

closed_label = tk.Label(window, text="CLOSED", bg="#ffffff", fg="#1ba6df", font=("Lucida Sans", 18))
closed_label.place(x=111, y=160)

since_label = tk.Label(window, text="Since 09:30", bg="#ffffff", fg="#1ba6df", font=("Lucida Sans", 11))
since_label.place(x=115, y=190)

button_1_image = tk.PhotoImage(file=load_asset("2.png"))
button_1 = tk.Button(
    window,
    image=button_1_image,
    text="Button 1",
    compound=tk.TOP,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: play_beep()
)
button_1.place(x=11, y=80, width=99, height=53)

button_2_image = tk.PhotoImage(file=load_asset("3.png"))
button_2 = tk.Button(
    window,
    image=button_2_image,
    text="Button 2",
    compound=tk.TOP,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: play_beep()
)
button_2.place(x=110, y=80, width=99, height=53)

button_3_image = tk.PhotoImage(file=load_asset("4.png"))
button_3 = tk.Button(
    window,
    image=button_3_image,
    text="Button 3",
    compound=tk.TOP,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: play_beep()
)
button_3.place(x=209, y=80, width=99, height=53)

canvas.create_rectangle(11, 136, 309, 468, fill='#ffffff', outline="")
canvas.create_rectangle(45, 154, 272, 451, fill='#ffffff', outline="#1ba6df", width="4.0")

window.resizable(False, False)
window.mainloop()
