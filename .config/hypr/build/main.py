#!/bin/bython

import subprocess 
import time 

def main ():
    processes =[]
    try :
        subprocess .check_output (["pidof","hyprlock"])
        return 
        
    
    except :
        pass 
        
    
    
    out =subprocess .check_output (["hyprctl","monitors"])
    monitors =len (str (out ).split ("Monitor"))-1
    for i in range (monitors ):
        time .sleep (0.2)
        processes .append (
        [subprocess .Popen ("alacritty --hold -e /home/prushton/dotfiles/pipes.sh",shell =True ),i ]
        )
        if (i ==0):
            processes .append (
            [subprocess .Popen ("alacritty -e /bin/python /home/prushton/dotfiles/clockterm/dist/main.py",shell =True ),0]
            )
            processes .append (
            [subprocess .Popen ("alacritty -e /bin/python /home/prushton/dotfiles/batterm/dist/main.py",shell =True ),0]
            )
            
        
        subprocess .check_output (["hyprctl","dispatch","focusmonitor",str (i )])
        subprocess .check_output (["hyprctl","dispatch","workspace",str (99-i )])
        
    
    time .sleep (0.2)
    for process in processes :
        print (process [0].pid ,"is moving to workspace",99-process [1])
        subprocess .call ("hyprctl dispatch movetoworkspacesilent "+str (99-process [1])+",pid:"+str (process [0].pid ),shell =True )
        
    
    
    # subprocess.run(["dunstctl", "set-paused", "true"])
    # subprocess.run(["killall", "waybar"])
    # 
    # subprocess.run(["hyprlock"])
    # 
    # subprocess.run(["dunstctl", "set-paused", "false"])
    # subprocess.Popen(["waybar"])
    
    #for i in processes {
    #print(i.pid)
    #i.kill()
    #}
    
    # for i in range(monitors) {
    #     subprocess.check_output(["hyprctl", "dispatch", "focusmonitor", str(i)])
    #     subprocess.check_output(["hyprctl", "dispatch", "workspace", str(i+1)])
    # }
    


if __name__ =="__main__":
    main ();
    

