
# Insta Follower Bot

**Insta Follower Bot** is an automation script in python that follows a given Instagram profile.

## Prerequisites

- Python must be installed on your targets machine.

## Usage

1. Download the repository containing the `Insta_follower_bot.pyw` script and the `instagram_link.ini` configuration file.
2. Open the `instagram_link.ini` configuration file in a text editor and replace `https://www.instagram.com/YOUR_PROFILE` with the link to the Instagram profile you want your target to follow.
3. If your Instagram profile does not have a profile picture, open the `Insta_follower_bot.pyw` script in a text editor and set the `Profile_picture` variable to `False`.
4. (Optional) For advanced users: If you prefer not to use a configuration file, you can edit the `Insta_follower_bot.pyw` script directly and adjust the `INSTAGRAM_LINK` variable. Ensure to add a delay (`time.sleep(3)`) after `webbrowser.open(INSTAGRAM_LINK)`.
5. Run the script on the target's machine.
6. Profit.

## Unique Features
- The script will delete itself after execution, or in case of an error. 
- Our Deletion Bypass method leaves no trace of the script behind, not even in the Recycle Bin.
- Follow method variably, depending on the elements of the profile. 

## Changelog
The full Changelog can be found [here](https://github.com/UnitedPenguin/Insta-Follower-Bot/blob/main/Changelog.md).

## Disclaimer

This tool is meant for research purposes only. The developer and contributors are not responsible for any misuse or for any damages that you may cause. You agree that you use this software at your own risk. Interactions with platforms like Instagram can violate their terms of service. Use this script responsibly and ethically.

## License

This project is licensed under the MIT License. This license does not imply any guarantee or warranty of any kind.
