# General
bindkey -e
bindkey "\e[3~" delete-char
bindkey '\e[1~' beginning-of-line
bindkey '\e[4~' end-of-line

# Up arrow:
bindkey '\e[A' history-substring-search-up
bindkey '\eOA' history-substring-search-up

# Down arrow:
bindkey '\e[B' history-substring-search-down
bindkey '\eOB' history-substring-search-down

# Vanilla behavior is to move by characters
bindkey -M viins '^b' backward-word
bindkey -M viins '^f' forward-word

# Ctrl and delete
bindkey '^H' backward-kill-word
bindkey '5~' kill-word

# Crtl and Arrows
bindkey "^[[1;5C" forward-word
bindkey "^[[1;5D" backward-word

# Other conveniences
bindkey -M viins '^a' beginning-of-line
bindkey -M viins '^d' push-line-or-edit

