#!/bin/bash

rm ~/.config/alacritty
rm ~/.config/dunst
rm ~/.config/hypr
rm ~/.config/neofetch
rm ~/.config/nvim
rm ~/.config/kitty
rm ~/.config/waybar


ln -s ~/dotfiles/.config/alacritty ~/.config/alacritty
ln -s ~/dotfiles/.config/dunst     ~/.config/dunst
ln -s ~/dotfiles/.config/hypr      ~/.config/hypr
ln -s ~/dotfiles/.config/neofetch  ~/.config/neofetch
ln -s ~/dotfiles/.config/nvim      ~/.config/nvim
ln -s ~/dotfiles/.config/kitty     ~/.config/kitty
ln -s ~/dotfiles/.config/waybar    ~/.config/waybar
