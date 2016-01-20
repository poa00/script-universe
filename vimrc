set nocompatible
source $VIMRUNTIME/vimrc_example.vim
source $VIMRUNTIME/mswin.vim
behave mswin


map #1 0vwhxi<tab><esc>j
map #2 0vwhxi<tab><tab><esc>j
map #3 0vwhxi<tab><tab><tab><esc>j
map #4 0vwhxi<tab><tab><tab><tab><esc>j

set expandtab
set tabstop=4
set shiftwidth=4
set ai
set showmatch
" ic -> ignorecase
set ic
set incsearch
set showmatch
set hlsearch
set autochdir

nunmap <C-A>
" http://vim.wikia.com/wiki/Increasing_or_decreasing_numbers

"colorscheme elflord
colorscheme desert
syntax on
filetype on
filetype plugin on
filetype indent on

" set relativenumber
set number
set undofile




