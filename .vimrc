set backspace=indent,eol,start
set history=500
set wildmode=list:longest,full
set autoindent
set smartindent
set number
set nowrap
set nobackup
set ruler
set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab
set smarttab
set showmatch
set noexpandtab
set expandtab
set hlsearch
set ai

" See if you can alter the color and width of this
set colorcolumn=99
syntax enable

" SOLARIZED
set background=light
colorscheme solarized

" Dealing with whitespace
highlight ExtraWhitespace ctermbg=grey guibg=grey
match ExtraWhitespace /\s\+$/

fun! <SID>StripTrailingWhitespaces()
	let l = line(".")
	let c = col(".")
	%s/\s\+$//e
	call cursor(l, c)
endfun

autocmd FileType c,cpp,java,php,ruby,python,javascript,html autocmd BufWritePre <buffer> :call <SID>StripTrailingWhitespaces()

