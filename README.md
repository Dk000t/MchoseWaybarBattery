# MchoseWaybarBattery

This script is written in python and automates the acquisition of the battery percentage for the MCHOSE mouse through selenium and chromium in order to then display its value on the waybar on linux.

<p></p>
<img width="76" height="40" alt="battery" src="https://github.com/user-attachments/assets/e2bb43b7-c5e2-40e7-8dbe-b56c47b121be" />
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
