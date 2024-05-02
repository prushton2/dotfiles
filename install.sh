#!/bin/bash

declare -a __config_files
__config_files=( 
	".config/alacritty" 
	".config/dunst" 
	".config/hypr" 
	".config/neofetch" 
	".config/nvim" 
	".config/kitty" 
	".config/waybar" 
	".bashrc" 
	".gnupg"
)

declare -a __remove_queue

echo -e "\033[31;1;1mThe following directories will be removed\033[0m"

for dir in "${!__config_files[@]}" 
do
	__remove_queue[dir]="${HOME}/${__config_files[dir]}"
	echo "${__remove_queue[dir]}"
done

echo ""
echo -n "Confirm the deletion of the directories [Y/n] "
read confirm

if [ $confirm = "y" ]; then
	
	for dir in "${!__config_files[@]}" 
	do
		rm -rf "${__remove_queue[dir]}"
		ln -s "${HOME}/dotfiles/${__config_files[dir]}" "${HOME}/${__config_files[dir]}"
	done
	echo "dotfiles installed"

else
	echo "denied"
fi

