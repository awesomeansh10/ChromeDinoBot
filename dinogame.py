import pyautogui
from PIL import Image, ImageChops
import time 
import keyboard

offsetx = 400 
offsety = 660
increase = 1.15
time.sleep(1)
with pyautogui.hold("ctrl"):
    pyautogui.press("r")
pyautogui.press("space")

fourtysecondtime = time.time()
while True:
    pyautogui.keyUp("space")
    last = Image.open("last.png")
    current = pyautogui.screenshot("first.png",region=(offsetx,offsety, 200, 10))
    difference = ImageChops.difference(current, last)
    if difference.getbbox():
        pyautogui.keyDown("space")
        difference.save("lastdif.png")
    if keyboard.is_pressed('b'):
        break

    offsetx += increase
    if(fourtysecondtime - time.time() >=40):
        offsetx += 25 #speed increase
        increase += 0.02
        fourtysecondtime = time.time()
    current.save("last.png")