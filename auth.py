import os
import sys
import tkinter as tk
from utilities import *

class AuthWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.result = tk.StringVar(value="")
        self.window.geometry("341x306")
        self.window.configure(bg="#ffffff")
        self.window.title("Untitled")
        self._setup_ui()

    def _setup_ui(self):
        self.canvas = tk.Canvas(
            self.window,
            bg="#ffffff",
            width=341,
            height=306,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.canvas.create_rectangle(0, 50, 341, 306, fill='#1ba6df', outline="")

        self.canvas.create_text(
            24,
            69,
            anchor="nw",
            text="Authentication Required",
            fill="#ffffff",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            21,
            98,
            anchor="nw",
            text="You are attempting to access a secured feature!",
            fill="#ffffff",
            font=("Inter", 13 * -1)
        )

        self.canvas.create_text(
            45,
            132,
            anchor="nw",
            text="How would you like to authenticate?",
            fill="#ffffff",
            font=("Inter", 14 * -1)
        )

        self.image_1 = tk.PhotoImage(file=load_asset("logo.png", assetArea="auth"))
        self.canvas.create_image(170, 24, image=self.image_1)

        self.button_1_image = tk.PhotoImage(file=load_asset("ButtonPin.png", assetArea="auth"))
        self.button_1 = tk.Button(
            image=self.button_1_image,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._on_button_press("button_1", assetArea="auth")
        )
        self.button_1.place(x=29, y=163, width=279, height=34)

        self.button_2_image = tk.PhotoImage(file=load_asset("ButtonKeycard.png", assetArea="auth"))
        self.button_2 = tk.Button(
            image=self.button_2_image,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._on_button_press("button_2", assetArea="auth")
        )
        self.button_2.place(x=29, y=208, width=279, height=34)

        self.button_3_image = tk.PhotoImage(file=load_asset("ButtonCancel.png", assetArea="auth"))
        self.button_3 = tk.Button(
            image=self.button_3_image,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._on_button_press("button_3")
        )
        self.button_3.place(x=29, y=253, width=279, height=34)

        self.window.resizable(False, False)

    def _on_button_press(self, button_id):
        self.result.set(button_id)
        self.window.destroy()

    def request_auth(self):
        self.window.wait_variable(self.result)
        return self.result.get() != "button_3"

if __name__ == "__main__":
    auth_window = AuthWindow()
    print(auth_window.request_auth())
