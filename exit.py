import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime

# Ending the session
def sign_out():

    subprocess.Popen('C:\\Windows\\system32\\Taskmgr.exe')
    time.sleep(10)

    # Selecting the webex app 1

    terminate_1 =  pyautogui.locateCenterOnScreen('webex1.png')
    pyautogui.moveTo(terminate_1)
    pyautogui.click()
    pyautogui.click(button='right')

    # End task 1

    end_task = pyautogui.locateCenterOnScreen('end_task.png')
    pyautogui.moveTo(end_task)
    pyautogui.click()

    # Selecting the webex app 2

    terminate_1 =  pyautogui.locateCenterOnScreen('webex2.png')
    pyautogui.moveTo(terminate_1)
    pyautogui.click()
    pyautogui.click(button='right')

    # End task 2

    end_task = pyautogui.locateCenterOnScreen('end_task.png')
    pyautogui.moveTo(end_task)
    pyautogui.click()


# Reading the file
df = pd.read_csv('timings.csv')

while True:
    now = datetime.now().strftime("%H:%M")
    if now in str(df['end']):
        row = df.loc[df['end'] == now]
        sign_out()
        time.sleep(20)
        print('signed out')