import tkinter as tk
import tabs
from utilities import load_asset
import auth

class Tab:
    def __init__(self):
        pass

    def draw(self, canvas):
        pass

class Header(Tab):
    def __init__(self, canvas):
        super().__init__()
        self.canvas = canvas
        self.CurrentTab = None
        self.CurrentButton = None
        self.load_images()

    def load_images(self):
        self.image_1 = tk.PhotoImage(file=load_asset("image_1.png"))

    def show_tab(self, button):
        tab = None
        if button == self.ButtonDrawer:
            tab = tabs.Drawer
        elif button == self.ButtonAdmin:
            if auth.AuthWindow().request_auth():
                tab = tabs.Admin
        elif button == self.ButtonLogs:
            tab = tabs.Logs
            
        if tab:
            if self.CurrentTab:
                self.CurrentTab.close()
            self.CurrentTab = tab(self.canvas)
            self.CurrentTab.draw(self.canvas)
        
    def refresh_highlight(self):
        for v in [self.ButtonAdmin, self.ButtonDrawer, self.ButtonLogs]:
            if self.CurrentButton == v:
                v.config(bd=2)
                self.show_tab(v)
            else:
                v.config(bd=0)
    
    def select_button(self, button):
        self.CurrentButton = button
        self.refresh_highlight()

    def draw(self, canvas):
        canvas.create_image(162, 243, image=self.image_1)

        self.ButtonDrawer = tk.Button(
            canvas,
            text="Drawer",
            bd=0,
            bg="#ffffff",
            font="Arial",
            highlightcolor="#e5e5e5"
        )
        self.ButtonDrawer.place(x=11, y=80, width=98, height=53)
        
        self.ButtonAdmin = tk.Button(
            canvas,
            text="Admin",
            bd=0,
            bg="#ffffff",
            font="Arial",
            highlightcolor="#e5e5e5"
        )
        self.ButtonAdmin.place(x=110, y=80, width=98, height=53)
        
        self.ButtonLogs = tk.Button(
            canvas,
            text="Logs",
            bd=0,
            bg="#ffffff",
            font="Arial",
            highlightcolor="#e5e5e5"
        )
        self.ButtonLogs.place(x=210, y=80, width=98, height=53)
        
        for button in [self.ButtonAdmin, self.ButtonDrawer, self.ButtonLogs]:
            button.config(command=lambda b=button: self.select_button(b))
            
        self.CurrentButton = self.ButtonDrawer
        self.refresh_highlight()
