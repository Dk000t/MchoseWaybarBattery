# MchoseWaybarBattery

This script is written in python and automates the acquisition of the battery percentage for the MCHOSE mouse through selenium and chromium in order to then display its value on the waybar on linux.

<p></p>
<img width="229" height="39" alt="rounded_image" src="https://github.com/user-attachments/assets/3ec7ee24-ada0-4488-8729-21c21c19cde5" />
<p></p>

Waybar config:
```
  "custom/mouse": {
    "format": "{}",
    "exec": "python ~/.config/waybar/scripts/Battery.py",
    "interval": 1800,
    "tooltip": false
  }
```
