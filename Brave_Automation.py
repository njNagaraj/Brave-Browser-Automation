''' It is a brave browser automation for earning BAT(Basic Attention Token) Cryptocurrency provided by
brave browser for seeing adds while using the browser we can only see ads if we use the browser.
So here i have created a automation that do several tasks that automatically use the browser by
running the script without the help of us.

Done on 27-06-2022 by Nagaraj'''

#start

import pyautogui
import random
import time
import subprocess
import psutil

print("Script Executing")

# My browser path and opening of browser, if you are using replace it with your path
software_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
opening = subprocess.Popen(software_path)

# Find the screen width and height
screen_width, screen_height = pyautogui.size()

# wait time for the browser to open
time.sleep(10)

# For the first movement
pyautogui.moveTo(500, 500, duration=0.5)

while True:

    #checking weather the browser is closed if closed open the browser
    if opening.poll() is None:
        pass
    else:
        opening = subprocess.Popen(software_path)

    # identify battery percentage if battery percentage if <=10 the stop executing the script
    battery = psutil.sensors_battery()
    percentage = battery.percent
    if percentage <= 10:
        exit()

    # Time gap of 4 minutes before moving again
    time.sleep(240)

    # Open a new tab (because new tab gives BAT by seeing promotion on new tab)
    pyautogui.hotkey("ctrl", "t")

    # shifting to previous tab
    pyautogui.hotkey("ctrl", "shift", "tab")

    # Close the previous tab
    pyautogui.hotkey("ctrl", "w")

    # For doing the random movement 3 times
    for _ in range(3):
        # Generate random coordinates within the screen size
        random_x = random.randint(100, screen_width)
        random_y = random.randint(100, screen_height)

        # Move the mouse to the random coordinates
        pyautogui.moveTo(random_x, random_y, duration=0.5)

#end