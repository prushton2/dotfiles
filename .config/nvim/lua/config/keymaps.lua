-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here
-- use `vim.keymap.set` instead
local map = vim.keymap.set

vim.keymap.del({ "n", "v" }, "s")
--vim.keymap.del("n", "<C-;>")
-- vim.keymap.del("n", "<C-/>")

-- string|string[] modes, string command, Object options
map({ "n", "v" }, "s", "x<Left>a", { desc = "Substitute" })
map("n", "<C-n>", ":Neotree<cr>")
map("n", "<C-;>", ":ToggleTerm<cr>")
