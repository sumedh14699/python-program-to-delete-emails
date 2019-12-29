import pyautogui
import keyboard
from pykeyboard import PyKeyboard
import time


while True:
 if keyboard.is_pressed('e'): 
    while True:
 #click on location 1192, 286 for 50 times and then hit f5 once and again do it
          for p in range(1,51):
                pyautogui.click(1193, 384)
                #print("clicked")
                time.sleep(2)
                if keyboard.is_pressed('p'):
                      break
          print("1st 50 deleted and refreshing...")
          #pyautogui.press('f5') 

          if keyboard.is_pressed('q'):
             break
 elif keyboard.is_pressed('t'):
             break
