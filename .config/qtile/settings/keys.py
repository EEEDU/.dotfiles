# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile keybindings

from libqtile.config import Key
from libqtile.command import lazy


mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Cambiar de ventana
    ([mod], "Right", lazy.layout.right()),
    ([mod], "Down", lazy.layout.down()),
    ([mod], "Left", lazy.layout.left()),
    ([mod], "Up", lazy.layout.up()),

    ([mod], "space", lazy.layout.next()),

    # Mover ventana
    ([mod, "shift"], "Left", lazy.layout.shuffle_left()),
    ([mod, "shift"], "Right", lazy.layout.shuffle_right()),
    ([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    ([mod, "shift"], "Up", lazy.layout.shuffle_up()),

    # Crecer ventana
    ([mod, "control"], "Left", lazy.layout.grow_left()),
    ([mod, "control"], "Right", lazy.layout.grow_right()),
    ([mod, "control"], "Down", lazy.layout.grow_down()),
    ([mod, "control"], "Up", lazy.layout.grow_up()),
    
    ([mod], "n", lazy.layout.normalize()),

    # Ventana flotante
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Layout
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Matar ventana
    ([mod], "BackSpace", lazy.window.kill()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    # ------------ Aplicaciones ------------

    # Menu
    ([mod], "m", lazy.spawn("rofi -show drun")),

    # Windows
    ([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Buscador
    ([mod], "b", lazy.spawn("firefox")),

    # Explorador de archivos
    ([mod], "e", lazy.spawn("pcmanfm")),

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),

    # Redshift
    ([mod], "r", lazy.spawn("redshift -O 2400")),
    ([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Imprimir pantalla
    ([mod], "s", lazy.spawn("scrot")),
    ([mod, "shift"], "s", lazy.spawn("scrot -s")),

    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]
