is_active=$(systemctl status hypridle --user | grep 'Active: ' | sed -e 's/     Active: //' | sed -e 's/ (.*//')

echo $is_active >~/.config/waybar/lastout

if [[ $1 == "-s" ]]; then
	if [[ $is_active = "active" ]]; then
		systemctl stop hypridle --user
	else
		systemctl start hypridle --user
	fi
	sleep 1
	kill -s SIGRTMIN+1 $(pidof waybar)
fi

if [[ $1 == "-r" ]]; then
	if [[ $is_active = "active" ]]; then
		echo '{"percentage": 100}'
	else
		echo '{"percentage": 0}'
	fi
fi
