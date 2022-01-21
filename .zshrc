

# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# Theme
ZSH_THEME="powerlevel10k/powerlevel10k"

# Plugins
plugins=(git
	zsh-syntax-highlighting 
	zsh-autosuggestions
 	sudo 
	copydir
	copyfile
	dirhistory
	z
	)				

# Source
source $ZSH/oh-my-zsh.sh

# Alias
alias zshconfig="mate ~/.zshrc"

# Exa
if [ -x "$(command -v exa)" ]; then
    alias ls="exa --icons"
    alias la="exa --long --all --group --icons"
fi
