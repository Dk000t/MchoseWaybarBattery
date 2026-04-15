# MchoseWaybarBattery

This script is written in python and automates the acquisition of the battery percentage for the MCHOSE mouse through selenium and chromium in order to then display its value on the waybar on linux.

<p></p>
<img width="76" height="40" alt="output-onlinepngtools" src="https://github.com/user-attachments/assets/a7b53894-4079-4eb9-a3eb-78367b7c1dd4" />
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
