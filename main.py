import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime

#Starting the session
def sign_in(meetingid, pswd):

    subprocess.Popen('C:\\Program Files (x86)\\Webex\\Webex\\Applications\\ptoneclk.exe')

    time.sleep(10)

    # Type the meeting ID

    meeting_id_btn =  pyautogui.locateCenterOnScreen('alt_join2.png')
    pyautogui.moveTo(meeting_id_btn)
    pyautogui.click()
    time.sleep(2)

    # Clearing the old ID

    pyautogui.press('backspace', presses=11)
    
    # Entering the ID
    
    pyautogui.write(meetingid)
    pyautogui.press('enter')


    # Hits the join button
    #join_btn = pyautogui.locateCenterOnScreen('join.png')
    #pyautogui.moveTo(join_btn)
    #pyautogui.click()
    time.sleep(10)

    #Types the password and hits enter
    meeting_pswd_btn = pyautogui.locateCenterOnScreen('pass.png')
    pyautogui.moveTo(meeting_pswd_btn)
    pyautogui.click()
    pyautogui.write(pswd)
    pyautogui.press('enter')


    time.sleep(15)
    # Hits the join meeting button

    #join_btn = pyautogui.locateAllOnScreen('join_meeting.png')
    #pyautogui.moveTo(join_btn)
    #pyautogui.click()
    pyautogui.press('enter')

# Ending the session
def sign_out():

    #subprocess.Popen('C:\\Windows\\system32\\Taskmgr.exe')
    #time.sleep(10)

    # Selecting the webex app 1

    #terminate_1 =  pyautogui.locateCenterOnScreen('webex1.png')
    #pyautogui.moveTo(terminate_1)
    #pyautogui.click()
    #pyautogui.click(button='right')

    # End task 1

    #end_task = pyautogui.locateCenterOnScreen('end_task.png')
    #pyautogui.moveTo(end_task)
    #pyautogui.click()

    # Selecting the webex app 2

    #terminate_1 =  pyautogui.locateCenterOnScreen('webex2.png')
    #pyautogui.moveTo(terminate_1)
    #pyautogui.click()
    #pyautogui.click(button='right')

    # End task 2

    #end_task = pyautogui.locateCenterOnScreen('end_task.png')
    #pyautogui.moveTo(end_task)
    #pyautogui.click()

    exit_btn =  pyautogui.locateOnScreen('exit.png')
    pyautogui.moveTo(exit_btn)
    pyautogui.click()
    time.sleep(2)
    pyautogui.press('enter')

# Reading the file
df = pd.read_csv('timings.csv')

while True:
    # checking of the current time exists in the csv file
    now = datetime.now().strftime("%H:%M")
    if now in str(df['timings']):

       row = df.loc[df['timings'] == now]
       m_id = str(row.iloc[0,1])
       m_pswd = str(row.iloc[0,2])

       sign_in(m_id, m_pswd)
       time.sleep(40)
       print('signed in')

    if now in str(df['end']):
        row = df.loc[df['end'] == now]
        sign_out()
        time.sleep(20)
        print('signed out')









