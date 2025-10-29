import pyautogui
import time

im1=pyautogui.screenshot(region=(0,0,300,400))
im1.save('image2.png')
#(X,Y, horizonta, vertical)