import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime

def sign_in(meetingid, pswd):
    #Opens up the zoom app
    #change the path specific to your computer
    
    #If on windows use below line for opening zoom
    #subprocess.call('C:\\myprogram.exe')
    
    #If on mac / Linux use below line for opening zoom
    subprocess.call(r"C:\Users\user\AppData\Roaming\Zoom\bin\Zoom.exe")

    time.sleep(5)
    
    #clicks the join button
    join_btn = pyautogui.locateCenterOnScreen('join_btn.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    print("join")
    time.sleep(7)

    # Type the meeting ID
    #meeting_id_btn =  pyautogui.locateCenterOnScreen('meeting_id1.png')
    #pyautogui.moveTo(meeting_id_btn)
    #pyautogui.click()
    pyautogui.write(meetingid)
    pyautogui.press('enter')
    time.sleep(1)
    print("mid")
    

    # Disables both the camera and the mic
    media_btn = pyautogui.locateAllOnScreen('media_btn.png')
    for btn in media_btn:
        pyautogui.moveTo(btn)
        pyautogui.click()
        time.sleep(2)
        print("radio")
        

    # Hits the join button
    join_btn = pyautogui.locateCenterOnScreen('join1_btn.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    
    time.sleep(5)
    #Types the password and hits enter
    meeting_pswd_btn = pyautogui.locateCenterOnScreen('meeting_pswd.png')
    pyautogui.moveTo(meeting_pswd_btn)
    pyautogui.click()
    pyautogui.write(pswd)
    pyautogui.press('enter')

sign_in("9942769143"," 9lZFLp")

