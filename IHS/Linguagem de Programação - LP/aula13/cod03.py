import pyautogui
import time

time.sleep(5)
im1=pyautogui.screenshot(region=((49, 34, 315, 523)))
im1.save('image3.png')
#(X,Y, horizonta, vertical)