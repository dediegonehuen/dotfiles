# Dotfiles

🏠 Personal dotfiles.

## Installation

### 👉 Installation:

- **`Install dotfiles:`**

  - Go to your your home directory:

    ```shell
    cd ~
    ```

  - Clone the repository:

    ```shell
    git clone https://github.com/dediegonehuen/dotfiles .dotfiles
    ```

- **`Install dotbot:`**

  > [dotbot](https://github.com/anishathalye/dotbot) is a tool that bootstraps your dotfiles

  - Go to dotfiles directory:

    ```shell
    cd ~/.dotfiles
    ```

  - Install dotbot as submodule:

    ```shell
    git submodule add https://github.com/anishathalye/dotbot
    ```

  - Ignore dirty commits in the submodule

    ```shell
    git config -f .gitmodules submodule.dotbot.ignore dirty
    ```

  - Make install script executable

    ```shell
    sudo chmod +x install.sh
    ```

  - Run the install script

    ```shell
    ./install.sh
    ```

### 🛠️ Configuration:

### 🔰 Credits:

- [q3aql](https://gitlab.com/dediegonehuen/dotfiles)
- [Antonio Sarosi](https://github.com/antoniosarosi/dotfiles/)
- [Derek Taylor](https://gitlab.com/dwt1/dotfiles/)
- [TWB0109](https://github.com/TWB0109/PDots)
- [Dotbot](https://github.com/anishathalye/dotbot)
- [ChristianLempa](https://github.com/ChristianLempa/dotfiles)
