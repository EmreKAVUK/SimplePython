import pyautogui as auto
import time
msg = input("Enter Your Message")
time.sleep(4)
while True:
    auto.write(msg)
    auto.press('enter')
    time.sleep(0.77)
