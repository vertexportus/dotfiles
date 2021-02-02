export ZSH="/home/vertexportus/.oh-my-zsh"

# theme
ZSH_THEME="pmuse"
# general configs
ENABLE_CORRECTION="false"
# plugins
plugins=(git composer common-aliases copyfile docker encode64 jsontools lol mix ng npm sudo systemd urltools web-search)

# keychain
eval $(keychain --eval --quick --quiet --confhost --noask)

# oh-my-zsh
source $ZSH/oh-my-zsh.sh

# alias
alias ls="exa"
alias ll="exa -la"

# vars and profile
export EDITOR=/usr/bin/vim
emulate sh -c '. ~/.profile'
if [ -f /usr/share/nvm/init-nvm.sh ]; then
    source /usr/share/nvm/init-nvm.sh
fi
if [ -d ~/.asdf ]; then
    export PATH="$HOME/.asdf/bin:$HOME/.asdf/shims:$PATH"
    $HOME/.asdf/completions/asdf.bash
fi

# direnv
eval "$(direnv hook zsh)"

if [ -f "/usr/share/nvm/init-nvm.sh" ]; then
	source /usr/share/nvm/init-nvm.sh
fi

# zsh highlighting
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
