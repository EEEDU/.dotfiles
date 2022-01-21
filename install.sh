#!/bin/bash
 
actualizar(){
    sudo pacman -Syu
}

instalar(){
    sudo pacman -S python-pip exa unzip wget zsh
}

fuentes(){
    sudo mkdir /usr/share/fonts/ttf
    # Hack Nerd Font
    wget https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/Hack.zip
    unzip Hack.zip 
    rm -rf Hack.zip
    sudo mv Hack* /usr/share/fonts/ttf/
    # JetBrainsMono Nerd Font
    wget https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/JetBrainsMono.zip
    unzip JetBrainsMono.zip
    rm -rf JetBrainsMono.zip
    sudo mv JetBrains* /usr/share/fonts/ttf/

}

zsh(){
    # omz
    sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
    # tema
    git clone https://github.com/romkatv/powerlevel10k.git $ZSH_CUSTOM/themes/powerlevel10k
    # plugins
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
    git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
}

pycritty(){
    pip install pycritty
    pip install --install-option="--themes=onedark,dracula,nord" pycritty
    export PATH=$HOME/.local/bin:$PATH
    pycritty --font Hack --size 14 --opacity 0.8 
    pycritty install -t https://raw.githubusercontent.com/antoniosarosi/pycritty/master/config/themes/material-darker.yaml
    pycritty -t material-darker
    pycritty save Configuracion1
    pycritty load Configuracion1
}

qtile(){
    
}

 
 
# actualizar
# instalar
# fuentes
# zsh
pycritty

