# MCHOSEWaybarBattery

This Python script automates the retrieval of the battery percentage for the MCHOSE mouse using Selenium and Chromium, allowing the value to be displayed on the Waybar in Linux.

<p></p>
<img width="229" height="39" alt="rounded_image" src="https://github.com/user-attachments/assets/3ec7ee24-ada0-4488-8729-21c21c19cde5" />
<p></p>

## Instructions

### Create the chromium user directory:
```bash
mkdir -p $HOME/.config/chromium_battery
```
### Start Chromium using the created user directory:
```bash
chromium --user-data-dir=$HOME/.config/chromium_battery
```
### Open the MCHOSE webdriver website and pair your mouse:
```bash
https://www.mchose.com.cn/#/home
```
### Create the folder for the script and copy the script inside:
```bash
mkdir -p $HOME/.config/waybar/scripts
```
### Make the script executable:
```bash
chmod +x $HOME/.config/waybar/scripts/Battery.py
```
### Add configuration to waybar:
```
  "custom/mouse": {
    "format": "{}",
    "exec": "python ~/.config/waybar/scripts/Battery.py",
    "interval": 1800,
    "tooltip": false
  }
```
