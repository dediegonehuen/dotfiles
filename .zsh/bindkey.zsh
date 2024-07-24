# Bindkey
# ---
#
# General
bindkey -e
bindkey "\e[3~" delete-char
bindkey '\e[1~' beginning-of-line
bindkey '\e[4~' end-of-line
## Ctrl and delete
bindkey '^H' backward-kill-word
bindkey '5~' kill-word
## Crtl and Arrows
bindkey "^[[1;5C" forward-word
bindkey "^[[1;5D" backward-word
