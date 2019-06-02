export ZSH="/home/vertexportus/.oh-my-zsh"
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# theme
ZSH_THEME="pmuse"
# general configs
ENABLE_CORRECTION="true"
# plugins
plugins=(git command-not-found composer common-aliases copyfile docker encode64 jsontools lol mix ng npm sudo systemd urltools web-search)

# keychain
eval $(keychain --eval --quick --quiet --confhost --noask)

# oh-my-zsh
source $ZSH/oh-my-zsh.sh

# alias
alias ll="ls -la"

# vars and profile
export EDITOR=/usr/bin/vim
emulate sh -c '. ~/.profile'
