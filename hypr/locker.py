#!/bin/bython

import subprocess
import time

def main() {
    try {
        subprocess.check_output(["pidof", "hyprlock"])
        return
    }
    except { 
        pass
    }

    out = subprocess.check_output(["hyprctl", "monitors"])
    monitors = len(str(out).split("Monitor"))-1

    for i in range(monitors) {
        subprocess.check_output(["hyprctl", "dispatch", "focusmonitor", str(i)])
        subprocess.check_output(["hyprctl", "dispatch", "workspace", str(99-i)])
        subprocess.Popen(["kitty", "/home/prushton/dotfiles/hypr/pipes.sh"])
        time.sleep(0.2)
    }
    
    subprocess.run(["dunstctl", "set-paused", "true"])
    subprocess.run(["killall", "waybar"])
    
    subprocess.run(["hyprlock"])
    
    subprocess.run(["dunstctl", "set-paused", "false"])
    subprocess.Popen(["waybar"])
    

    for i in range(monitors) {
        subprocess.check_output(["hyprctl", "dispatch", "focusmonitor", str(i)])
        subprocess.check_output(["hyprctl", "dispatch", "workspace", str(i+1)])
    }
    subprocess.run(["killall", "kitty"])
}

if __name__ == "__main__" {
        main();
}
