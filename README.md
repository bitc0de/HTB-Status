# HTB-Status for Polybar

Is a polybar module that will show you your progress in Hack The Box indicating your current rank, global rank, points and respect (highly customizable).

![image](https://user-images.githubusercontent.com/19918951/132131908-d9b4d1c4-1649-4d0d-8933-0de0337b420e.png) 

## Installation
· Copy htbstatus.sh and htbstatus.py files to ~/.config/bin
· Change the user ID (ID_USUARIO) in htbstatus.py (the profile must be public):
· Copy this at bar section of ~/.config/polybar/current.ini:

```bash
[bar/htbstatus]
inherit = bar/main
width = 20%
height = 40
offset-x = 36.3% #change horizontal position if you need
offset-y = 0
background = ${color.bg}
foreground = ${color.white}
bottom = false
padding = 1
;padding-top = 2
module-margin-left = 0
module-margin-right = 0
;modules-left = date sep mpd
modules-center = htbstatus
wm-restack = bspwm
```

·Copy this at same file but on module section:

```bash
[module/htbstatus]
type = custom/script
interval = 20
exec = ~/.config/bin/htbstatus.sh
```

·Add this line at ~/.config/polybar/launch.sh file:
```bash
polybar htbstatus -c ~/.config/polybar/current.ini &
```

·Add this line at ~/.config/bspwm/bspwm
```bash
python3 ~/.config/bin/htbstatus.py
```
You may need to restart or sign out. Wait a few minutes for your statuses to update.

---

If you want you can make a pull request. The stars are appreciated :)
