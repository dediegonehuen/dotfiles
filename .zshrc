load_module() {
  if [ -n "$ABORTED" ]; then
    return
  fi

  module="$1"
  if [ -f "$module" ]; then
    source $module

    if [ "$?" != "0" ]; then
      echo "Failed to load zsh module $module"
      export ABORTED=1
      return
    fi
  fi
}

load_module  ~/.config/zsh/aliases.zsh
load_module  ~/.config/zsh/functions.zsh
load_module  ~/.config/zsh/keybinds.zsh
load_module  ~/.config/zsh/nvm.zsh
load_module  ~/.config/zsh/wsl.zsh

ZSH_THEME="agnoster"

export ZSH="$HOME/.oh-my-zsh"

export PATH="$HOME/bin:$PATH"

plugins=(git)

eval "$(starship init zsh)"
