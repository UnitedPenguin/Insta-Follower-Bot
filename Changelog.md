## Changelog

### V1.2.0

1. **Enhanced Script Deletion**: The script now has added functionality to delete itself using the bypass method if it encounters any errors during its operation. This ensures that the script doesn't remain on the system even if it crashes or doesn't complete its intended tasks.
2. **Updated Tabbing Movements**: After extensive testing with over 10 browsers, including the most popular ones, it was confirmed that all of them required 13 tab movements. Therefore, the script has been updated to use 13 tab presses as the default setting.
3. **Fixed Import Issues**: Addressed and fixed bugs related to the `webbrowser` module not being imported correctly.

### V1.1.0

1. **Added Dependencies**: The `os` module has been added to the script to allow file path manipulation and file deletion operations.
2. **Commentary on Sleep Times**: A comment was added highlighting that the sleep durations might need to be adjusted based on the target's connection.
3. **Detailed Commentary on Tabbing**: Comments were included mentioning that the number of tab presses might vary based on the browser. Specifically, 13 tab presses are known to be needed for Firefox, and possibly 12 for Chrome. Further testing is necessary.
4. **Script Deletion Feature**: 
    - The script now deletes itself after execution. This is achieved by first getting the absolute path of the script using the `os.path.abspath()` function.
    - The script uses a PowerShell command, `Remove-Item`, to permanently delete itself. The `-Force` flag ensures that the file bypasses the Recycle Bin.
5. **Added Sleep Before Deletion**: A 3-second delay (`time.sleep(3)`) was added before the script attempts to delete itself. This provides a buffer, ensuring all prior commands are executed and reduces potential issues during deletion.

### V1.0.0

1. **Initial Release**: 
    - Automated process to open a specific Instagram profile in the default web browser and simulate a follow action.
2. **Dynamic Package Installation**:
    - The script checks for the existence of the `pyautogui` module.
    - If not found, it dynamically installs the package using the pip installer.
3. **Web Browser Interaction**:
    - Uses `webbrowser.open()` to launch the web browser to the Instagram profile.
    - Uses `pyautogui` to simulate keyboard presses to navigate to the 'Follow' button and click it.
    - Ends by simulating the ALT+F4 key combination to close the browser.
4. **Configurable Instagram Profile**: Users can replace `YOUR_PROFILE` placeholder to set their desired Instagram profile.
