while [ 1 -eq 1 ]; do
	sleep 1
	tput reset
	echo $(systemctl status hypridle --user | grep "Active: ")
	cat lastout
done
