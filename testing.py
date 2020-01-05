import pyautogui
import time

try:
    while True:
        pixelColor = pyautogui.screenshot().getpixel((491, 256))
        if pixelColor[0]==83:
        	pyautogui.press('up')
        
except KeyboardInterrupt:
    print("\nDone...")