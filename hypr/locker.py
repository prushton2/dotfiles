#!/bin/bython

import subprocess
import time

out = subprocess.check_output(["hyprctl", "monitors"]);
monitors = len(str(out).split("Monitor"))-1

for i in range(monitors) {
    subprocess.check_output(["hyprctl", "dispatch", "focusmonitor", str(i)])
    subprocess.check_output(["hyprctl", "dispatch", "workspace", str(99-i)])
    subprocess.Popen(["kitty", "/home/prushton/dotfiles/hypr/pipes.sh"])
    time.sleep(0.2)
    subprocess.check_output(["hyprctl", "dispatch", "fullscreen"])
}

subprocess.run(["hyprlock"])

for i in range(monitors) {
    subprocess.check_output(["hyprctl", "dispatch", "focusmonitor", str(i)])
    subprocess.check_output(["hyprctl", "dispatch", "killactive"])
    time.sleep(0.2)
    subprocess.check_output(["hyprctl", "dispatch", "workspace", str(i+1)])
}
