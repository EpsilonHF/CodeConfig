set nocompatible              " be iMproved, required
filetype off                  " required
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'Lokaltog/vim-powerline'
Plugin 'yggdroot/indentline'
Plugin 'jiangmiao/auto-pairs'
Plugin 'psf/black'

call vundle#end()
filetype plugin indent on

set number
set showcmd
syntax on
set showmatch

set autoindent
set smartindent

set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab
set smarttab
set autoread

set ignorecase
set incsearch
set hidden
set autochdir
set hlsearch
set noerrorbells
set bufhidden=hide
set cursorline
set ruler
set cmdheight=1
set laststatus=2
"set statusline=\ %<%F[%1*%M%*%n%R%H]%=\ %y\ %0(%{&fileformat}\ %{&encoding}\ Ln\ %l,\ Col\ %c/%L%)

set cindent
set completeopt=longest,menu
set autowrite
set fileencodings=utf-8,gbk,ucs-bom,cp936