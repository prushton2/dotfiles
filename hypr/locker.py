#!/bin/bython

import subprocess
import time

out = None
out = subprocess.check_output(["hyprctl", "monitors"]);
monitors = len(str(out).split("Monitor"))-1

for i in range(monitors) {
    
    subprocess.check_output(["hyprctl", "dispatch", "focusmonitor", str(i)])
    subprocess.check_output(["hyprctl", "dispatch", "workspace", str(99-i)])
    subprocess.check_output(["kitty", "/home/prushton/dotfiles/hypr/pipes.sh", "--detach"])
}

time.sleep(3)

for i in range(monitors) {
    subprocess.check_output(["hyprctl", "dispatch", "workspace", str(99-i)])
    subprocess.check_output(["hyprctl", "dispatch", "killactive"])
}
