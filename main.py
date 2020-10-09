import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime

def sign_in(meetingid, pswd):

    subprocess.Popen('C:\\Program Files (x86)\\Webex\\Webex\\Applications\\ptoneclk.exe')

    time.sleep(10)

    # Type the meeting ID

    meeting_id_btn =  pyautogui.locateCenterOnScreen('id.png')
    pyautogui.moveTo(meeting_id_btn)
    pyautogui.click()
    pyautogui.write(meetingid)
    pyautogui.press('enter')


    # Hits the join button
    join_btn = pyautogui.locateCenterOnScreen('join.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    time.sleep(10)

    #Types the password and hits enter
    meeting_pswd_btn = pyautogui.locateCenterOnScreen('pass.png')
    pyautogui.moveTo(meeting_pswd_btn)
    pyautogui.click()
    pyautogui.write(pswd)
    pyautogui.press('enter')

    # Hits the join meeting button
    join_btn = pyautogui.locateAllOnScreen('join_meeting.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
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
