import os
import sys
import tkinter as tk

def load_asset(path):
    base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    assets = os.path.join(base, "assets")
    return os.path.join(assets, path)

window = tk.Tk()
window.geometry("324x487")
window.configure(bg="#ffffff")
window.title("Untitled")

canvas = tk.Canvas(
    window,
    bg = "#ffffff",
    width = 324,
    height = 487,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x=0, y=0)

image_1 = tk.PhotoImage(file=load_asset("image_1.png"))

canvas.create_image(162, 243, image=image_1)

button_1_image = tk.PhotoImage(file=load_asset("2.png"))

button_1 = tk.Button(
    image=button_1_image,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 has been pressed!")
)

button_1.place(x=11, y=80, width=99, height=53)

button_2_image = tk.PhotoImage(file=load_asset("3.png"))

button_2 = tk.Button(
    image=button_2_image,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 has been pressed!")
)

button_2.place(x=110, y=80, width=99, height=53)

button_3_image = tk.PhotoImage(file=load_asset("4.png"))

button_3 = tk.Button(
    image=button_3_image,
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 has been pressed!")
)

button_3.place(x=209, y=80, width=99, height=53)

canvas.create_rectangle(11, 136, 309, 468, fill='#ffffff', outline="")

canvas.create_text(
    18,
    89,
    anchor="nw",
    text="Drawer",
    fill="#000000",
    font=("Lucida Sans", 18 * -1)
)

canvas.create_text(
    121,
    91,
    anchor="nw",
    text="Admin",
    fill="#000000",
    font=("Lucida Sans", 18 * -1)
)

canvas.create_text(
    229,
    90,
    anchor="nw",
    text="Logs",
    fill="#000000",
    font=("Lucida Sans", 18 * -1)
)

canvas.create_rectangle(45, 154, 272, 451, fill='#ffffff', outline="#1ba6df", width="4.0")

canvas.create_text(
    170,
    422,
    anchor="nw",
    text="Main Draw",
    fill="#1ba6df",
    font=("Lucida Sans", 18 * -1)
)

canvas.create_text(
    111,
    223,
    anchor="nw",
    text="CLOSED",
    fill="#1ba6df",
    font=("Lucida Sans", 18 * -1)
)

canvas.create_text(
    115,
    253,
    anchor="nw",
    text="Since 09:30",
    fill="#1ba6df",
    font=("Lucida Sans", 11 * -1)
)

window.resizable(False, False)
window.mainloop()
