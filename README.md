# MchoseWaybarBattery

This script is written in python and automates the acquisition of the battery percentage for the MCHOSE mouse through selenium and chromium in order to then display its value on the waybar on linux.

<p></p>
<img width="69" height="25" alt="battery" src="https://github.com/user-attachments/assets/cd9d8a6b-1ca9-4e6f-bcde-44c5ce8bdbe8" />
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
