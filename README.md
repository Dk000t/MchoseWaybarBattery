# MCHOSEWaybarBattery

This Python script automates the retrieval of the battery percentage for the MCHOSE mouse using Selenium and Chromium, allowing the value to be displayed on the Waybar in Linux.

<p></p>
<img width="229" height="39" alt="rounded_image" src="https://github.com/user-attachments/assets/3ec7ee24-ada0-4488-8729-21c21c19cde5" />
<p></p>

## Instructions
### Get the Vendor ID and Product ID of your mouse:
```bash
lsusb
```
### Create an udev rule
```bash
nano /etc/udev/rules.d/99-mouse-mchose.rules 
```
### Paste the following line into the file, making sure to include your specific mouse Vendor ID and Product ID:
```bash
KERNEL=="hidraw*", ATTRS{idVendor}=="3837", ATTRS{idProduct}=="100b", MODE="0666", TAG+="uaccess"
```
### Reload udev rules
```bash
udevadm control --reload && udevadm trigger
```
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
www.mchose.com.cn
```
### Copy the URL you see in the address bar for your mouse and edit it in the script (example from MCHOSE A7 V2 ULTRA):
```bash
https://www.mchose.com.cn/#/detail?deviceName=MCHOSE+A7+V2+Ultra
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
