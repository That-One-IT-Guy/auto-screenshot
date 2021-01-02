import pyautogui
import time
import keyboard

stpat = 'C:/Users/thech/Pictures/French book output/'
mainid = "Image#"
strtnum = 0
ext = ".png"

input("Ready! Press enter to start (and 5 second wait")
time.sleep(5)
while True:
    strtnum = strtnum + 1
    outptlc = stpat + mainid + str(strtnum) + ext
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(outptlc)
    keyboard.press_and_release('right_arrow')
    print("On page: " + str(strtnum))
    time.sleep(1)
