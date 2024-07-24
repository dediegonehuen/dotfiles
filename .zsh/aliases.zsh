# Alias
# ---
#
# Shortcut
alias k="kubectl"
alias h="helm"
alias tf="terraform"
alias a="ansible"
alias ap="ansible-playbook"

# Visual studio code
alias code="open -a 'Visual Studio Code'"

## General propouse
alias dns-prune-cache="sudo systemctl restart systemd-resolved"

## Ls aliases
alias ll='ls -l'
alias la='ls -A'
alias l='ls -CF'
alias grep='grep --color=auto'
if [ -f /usr/bin/batcat ]; then
  alias cat='batcat --style=plain --paging=never'
elif [ -f /usr/bin/bat ]; then
  alias cat='bat --style=plain --paging=never'
fi
if [ -f /usr/bin/exa ]; then
  alias ls='exa --group-directories-first'
  alias tree='exa -T'
else
  alias ls="ls --color=auto"
fi

# Wsl aliases
if [ -f "/proc/sys/fs/binfmt_misc/WSLInterop" ]; then
  alias ssh="ssh.exe"
fi
