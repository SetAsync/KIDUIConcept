from utilities import *
import cart

import tkinter as tk

class Tab:
    def __init__(self):
        self.__elements = []
        
    def element(self, newElement):
        self.__elements.append(newElement)
        
    def close(self):
        for v in self.__elements:
            self.canvas.delete(v)
        self.__elements = []
        
    def draw(self, canvas):
        pass

class Drawer(Tab):
    def __init__(self, canvas):
        self.canvas = canvas
        super().__init__()

    def draw(self, canvas):
        self.element(canvas.create_rectangle(11, 136, 309, 468, fill='#ffffff', outline=""))

        self.element(canvas.create_rectangle(45, 154, 272, 451, fill='#ffffff', outline="#1ba6df", width="4.0"))

        self.element(canvas.create_text(
            140,
            422,
            anchor="nw",
            text="Lock V1",
            fill="#1ba6df",
            font=("Lucida Sans", 18)
        ))

        self.element(canvas.create_text(
            111,
            223,
            anchor="nw",
            text="CLOSED",
            fill="#1ba6df",
            font=("Lucida Sans", 18)
        ))

        self.element(canvas.create_text(
            115,
            253,
            anchor="nw",
            text="Since 09:30",
            fill="#1ba6df",
            font=("Lucida Sans", 11)
        ))

class Admin(Tab):
    def __init__(self, canvas):
        super().__init__()
        self.canvas = canvas
        
    def draw(self, canvas):
        self.element(canvas.create_rectangle(11, 166, 309, 322, fill='#ffffff', outline="#35cc63", width="2.0"))

        self.element(canvas.create_rectangle(21, 180, 300, 232, fill='#1da5e0', outline=""))

        self.element(canvas.create_rectangle(20, 248, 299, 300, fill='#1da5e0', outline=""))

        self.element(canvas.create_text(
            107,
            192,
            anchor="nw",
            text="View Users",
            fill="#ffffff",
            font=("Mplus 1p Bold", 19 * -1)
        ))

        self.element(canvas.create_text(
            107,
            260,
            anchor="nw",
            text="Create User",
            fill="#ffffff",
            font=("Mplus 1p Bold", 19 * -1)
        ))
        
class Logs(Tab):
    def __init__(self, canvas):
        super().__init__()
        self.canvas = canvas