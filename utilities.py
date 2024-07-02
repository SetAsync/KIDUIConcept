import os
import winsound
import sys

def load_asset(path, assetArea = "assets"):
    # base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    # assets = os.path.join(base, "assets")
    # return os.path.join(assets, path)
    return assetArea+"\\"+path

def play_beep():
    frequency = 2500  # Set frequency (in Hz)
    duration = 100  # Set duration (in milliseconds)
    winsound.Beep(frequency, duration)