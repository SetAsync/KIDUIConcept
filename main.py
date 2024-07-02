import tabs
import header
import auth
from utilities import load_asset
import tkinter as tk

# Globals
window = tk.Tk()
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

# App
window.geometry("324x487")
window.configure(bg="#ffffff")
window.title("Kinetic M-E-D")

# Tabs
header_obj = header.Header(canvas)
header_obj.draw(canvas)

# Main App
canvas.pack(fill="both", expand=True)

# Detect Cart Actions
def InteractCart(event):
    # x: 43 - 270
    # y: 155 - 450
    if header_obj.CurrentButton != header_obj.ButtonDrawer:
        return
    
    if (event.x >= 43) and (event.x <= 270) and (event.y >= 155) and (event.y <= 450):
        accessGranted = auth.AuthWindow().request_auth()
        if accessGranted:
            # Perform some action
            pass
    
canvas.bind("<Button-1>", InteractCart)

window.resizable(False, False)
window.mainloop()
