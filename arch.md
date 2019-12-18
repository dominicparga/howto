# Arch Linux

There are plenty of help-pages, so this md-page just collects some useful snippets or links, but __IS NOT A COMPLETE GUIDE__.

Good pages to start

- [Arch installation guide][www_arch_install_guide]
- as orientation: [Arch - steps after installation][www_arch_steps_after_install]
- [Package-group overview][www_arch_group_overview]

## Table of Contents <a name="toc"></a>

1. [General snippets and interesting stuff](#general)
    1. [Add a user](#add-a-user)
    1. [Check colors in terminal](#check-colors-in-terminal)
    1. [Mouse-polling-rate](#mouse-polling-rate)
    1. [Random-number-generator](#random-number-generator)
    1. [Install printer](#install-printer)
    1. [LaTeX or TeX Live](#latex)
1. [Bootloader rEFInd](#refind)
1. [GNOME](#gnome)
1. [Display-Server (xorg, wayland)](#xorg-wayland)
1. [KDE-Plasma5](#kde)
    1. [Desktop-Environment itself](#desktop-env)
    1. [Login-Manager](#login-mgr)
    1. [Wayland](#wayland)
    1. [Applications](#applications)
1. [Cool themes and icons](#themes-and-icons)
1. [Fonts](#fonts)
1. [Troubleshooting](#troubleshooting)
    1. [Logging](#logging)
    1. [Unrecognized external HDD or tools or whatever](#unrecognized-hdd)

## General snippets and interesting stuff <a name="general"></a>

### Add a user <a name="add-a-user"></a>

```zsh
useradd -m -G wheel -s /usr/bin/zsh USERNAME
passwd USERNAME
visudo # for wheel-user-group
```

### Check colors in terminal <a name="check-colors-in-terminal"></a>

From [stackoverflow][www_stackoverflow_color_test]

```zsh
msgcat --color=test
```

### Mouse-polling-rate <a name="mouse-polling-rate"></a>

Check with [`sudo evhz`][www_arch_mouse_polling_rate]

### Random-number-generator <a name="random-number-generator"></a>

```zsh
yay -S haveged
```

### Install printer <a name="install-printer"></a>

```zsh
yay -S cups cups-pdf
yay -S hplip
```

Then enter `http://localhost:631/admin` and add a new printer.
In my case, the printer is `HP_Color_LaserJet_MFP_M277dw`, so I have added the respective PDD-file from [`hplib`][www_aur_hplip] at `/usr/share/ppd/HP/hp-color_laserjet_pro_mfp_m277-ps.ppd.gz`
If your printer needs a plugin (execute `hp-plugin` after installing `hplip`), you will find it [at hp][www_hp_printer_plugin_list].

### LaTeX or TeX Live <a name="latex"></a>

Install the packages mentioned in the ArchWiki-page.

## Bootloader rEFInd <a name="refind"></a>

- [rEFInd installation guide for Arch][www_arch_refind]
- [theme: rEFInd-minimal][www_refind_theme_minimal]

## GNOME <a name="gnome"></a>

## Display-Server (xorg, wayland) <a name="xorg-wayland"></a>

```zsh
sudo pacman -S xorg-server xorg-xinit
sudo pacman -S xf86-video-amdgpu
```

## KDE-Plasma5 <a name="kde"></a>

Repeadingly removes my home-directory when trying to uninstall a color-theme.
Hence goodbye KDE-Plasma, hello GNOME.

### Desktop-Environment itself <a name="desktop-env"></a>

```zsh
sudo pacman -S plasma-meta

sudo pacman -S kdebase-meta
sudo pacman -S kdegraphics-meta
sudo pacman -S kdeutils-meta
sudo pacman -S kdeadmin-meta
sudo pacman -S kdegames-meta
sudo pacman -S kde-gtk-config
```

### Login-Manager <a name="login-mgr"></a>

KDE uses sddm (`sudo pacman -S sddm sddm-kcm` according to ).
Based on Google Images, the theme `breeze` is the same as `Manjaro` is using.

Changing keyboard-layout for login with `SDDM` (a display-manager for `KDE`) can be done in the file `/usr/share/sddm/scripts/Xsetup`.
Add the line

```zsh
setxkbmap de,us
```

to enable a selection.
More information from [askubuntu - Wrong language displayed by SDDM on login Kubuntu 18.04][www_askubuntu_sddm_wrong_lang] or [US keyboard layout always used][www_gentoo_sddm_us_keyboard_layout] or [ArchLinux Forum SDDM Keyboard Selection][www_archlinux_sddm_keyboard_selection].

### Wayland <a name="wayland"></a>

- `sudo pacman -S plasma-wayland-session`
- [crashes with `RX 5700 XT`][www_kde_bug]

### Applications <a name="applications"></a>

If discover shows `No application back-ends found, please report to your distribution.`, then install `package-qt5` according to [this doc][www_discover_no_backends].

## Cool themes and icons <a name="themes-and-icons"></a>

- `aur/nordic-theme-git` (dark version)
- `aur/nordic-polar-theme-git` (light version)
- `ant-dracula-gtk-theme`
- `community/materia-gtk-theme`
- `community/arc-gtk-theme`

- `community/arc-icon-theme`
- `community/papirus-icon-theme`
- `aur/zafiro-icon-theme`

## Fonts <a name="fonts"></a>

Some cool monospace-fonts

- `Cascadia Code` via [github][www_github_cascadia_code] or [AUR][www_aur_cascadia_code]
- `Fira Code` via [github][www_github_fira_code] or [AUR][www_aur_fira_code]
- `Inconsolata` via AUR

More useful fonts/fonts-pkgs can be found [here][www_archwiki_schriftarten], e.g.

- `ttf-liberation`, which is used in `libreoffice`-templates
- [`ttf-ms-win10`][www_aur_ttf_ms_win10], which is a wrapper for local ms-fonts.
  Microsoft-Fonts can be added from an Windows-ISO as described [here][www_archwiki_msfonts].

## Troubleshooting <a name="troubleshooting"></a>

`CTRL`, `ALT` and e.g. `F2` selects another `tty`.
This can be used to check logs or access the system if something is not running accordingly.

### Logging <a name="logging"></a>

Via `journalctl`, e.g. `journalctl --unit=sddm.service`

### Unrecognized external HDD or tools or whatever <a name="unrecognized-hdd"></a>

If you have updated your system, e.g. via `yay`, do a restart.

Kernel-updates lead to missing support.
In my case the external HDD hasn't been detected anymore (`exFAT`).
I imagine, that old versions should be loaded that are already removed due to the system-update.
A restart fixed my problem with the unrecognized external HDD.

[www_arch_install_guide]: https://wiki.archlinux.org/index.php/installation_guide
[www_arch_group_overview]: https://www.archlinux.org/groups/
[www_stackoverflow_color_test]: https://askubuntu.com/questions/27314/script-to-display-all-terminal-colors
[www_arch_mouse_polling_rate]: https://wiki.archlinux.org/index.php/Mouse_polling_rate
[www_arch_refind]: https://wiki.archlinux.org/index.php/REFInd#refind_linux.conf
[www_arch_steps_after_install]: https://itsfoss.com/things-to-do-after-installing-arch-linux/

[www_aur_hplip]: https://www.archlinux.org/packages/extra/x86_64/hplip/
[www_hp_printer_plugin_list]: https://developers.hp.com/hp-linux-imaging-and-printing/binary_plugin.html

[www_refind_theme_minimal]: https://github.com/EvanPurkhiser/rEFInd-minimal
[www_kde_bug]: https://bugs.kde.org/show_bug.cgi?id=413223
[www_discover_no_backends]: https://wiki.archlinux.org/index.php/KDE#Discover_does_not_show_any_applications

[www_askubuntu_sddm_wrong_lang]: https://askubuntu.com/questions/1040844/wrong-language-displayed-by-sddm-on-login-kubuntu-18-04
[www_gentoo_sddm_us_keyboard_layout]: https://forums.gentoo.org/viewtopic-t-1031606-start-0.html
[www_archlinux_sddm_keyboard_selection]: https://bbs.archlinux.org/viewtopic.php?id=194408

[www_github_cascadia_code]: https://github.com/microsoft/cascadia-code/wiki/Installing-Cascadia-Code
[www_aur_cascadia_code]: https://www.archlinux.org/packages/community/any/ttf-cascadia-code/
[www_github_fira_code]: https://github.com/tonsky/FiraCode/wiki/Linux-instructions#installing-with-a-package-manager
[www_aur_fira_code]: https://www.archlinux.org/packages/community/any/otf-fira-code/
[www_archwiki_msfonts]: https://wiki.archlinux.org/index.php/Microsoft_fonts#Extracting_fonts_from_a_Windows_ISO
[www_aur_ttf_ms_win10]: https://aur.archlinux.org/packages/ttf-ms-win10/
[www_archwiki_schriftarten]: https://wiki.archlinux.de/title/Schriftarten
)