load_module() {
  if [ -n "$ABORTED" ]; then
    return
  fi

  module="$1"
  if [ -f "$module" ]; then
    source $module

    if [ "$?" != "0" ]; then
      echo "Module $module failed to load. Exiting."
      export ABORTED=1
      return
    fi
  fi
}

load_module  ~/.zsh/aliases.zsh
load_module  ~/.zsh/functions.zsh
load_module  ~/.zsh/bindkey.zsh
load_module  ~/.zsh/nvm.zsh
load_module  ~/.zsh/wsl.zsh
#load_module  ~/.zsh/starship.zsh

ZSH_THEME="agnoster"

export ZSH="$HOME/.oh-my-zsh"

plugins=(git)

source $ZSH/oh-my-zsh.sh