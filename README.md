# MchoseWaybarBattery

This script is written in python and automates the acquisition of the battery percentage for the MCHOSE mouse through selenium and chromium in order to then display its value on the waybar on linux.

<p></p>
<img width="229" height="39" alt="rounded_image" src="https://github.com/user-attachments/assets/3ec7ee24-ada0-4488-8729-21c21c19cde5" />
<p></p>

Before running this script for the first time, you need to create a separate Chromium user directory and bind your mouse to MCHOSE webdriver website.

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
