import pyautogui
import time
from datetime import datetime

def your_code():
    #boxed page reload
    pyautogui.click(102,62)
    time.sleep(3)

    #boxed rewards
    pyautogui.click(1772,308)
    pyautogui.click(1772,308)
    time.sleep(3)


#boxed chat
    pyautogui.click(1780,978)
    #pyautogui.write("use code GNARLY pretty plssss")
    #pyautogui.press('enter')
    #time.sleep(3)

    

    #epic pull tab
    pyautogui.click(366,20)
    time.sleep(2)

    #epic pull reload
    pyautogui.click(158,303)
    pyautogui.click(158,303)
    time.sleep(10)

    #epic pull chat button
    pyautogui.click(31,988)
    time.sleep(3)

    #epic pull collect rewards
    pyautogui.click(147,288)
    pyautogui.click(147,280)
    pyautogui.click(147,300)
    time.sleep(3)

    #twitch tab
    pyautogui.click(2005,20)
    time.sleep(1)

    #reload twitch
    pyautogui.click(2017,59)
    time.sleep(5)

    #twitch to 0
    pyautogui.click(1998,888)
    time.sleep(3)

    #back to boxed
    pyautogui.click(97,15)
    time.sleep(2)

    #all while doing it at the 28m and 58m mark

def wait():
    while True:
        now = datetime.now()
        if now.minute in [28, 58] and now.second == 0:  # Check for 28 or 58 minutes on the hour
            return
        time.sleep(1)

# Main loop
while True:
    wait()
    your_code()


