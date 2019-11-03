# Arch Linux

There are plenty of help-pages, so this md-page just collects some useful snippets or links, but __IS NOT A COMPLETE GUIDE__.

Good pages to start

- [Arch installation guide][www_arch_install_guide]
- as orientation: [Arch - steps after installation][www_arch_steps_after_install]
- [Package-group overview][www_arch_group_overview]

## General snippets

### Add a user

```zsh
useradd -m -G wheel -s /usr/bin/zsh USERNAME
passwd USERNAME
visudo # for wheel-user-group
```

### Check colors in terminal

From [stackoverflow][www_stackoverflow_color_test]

```zsh
msgcat --color=test
```

## Bootloader rEFInd

- [rEFInd installation guide for Arch][www_arch_refind]
- [theme: rEFInd-minimal][www_refind_theme_minimal]

## GNOME

## Display-Server (xorg, wayland)

```zsh
sudo pacman -S xorg-server xorg-xinit
sudo pacman -S xf86-video-amdgpu
```

## KDE-Plasma5

Repeadingly removes my home-directory when trying to uninstall a color-theme.
Hence goodbye KDE-Plasma, hello GNOME.

### Desktop-Environment itself

```zsh
sudo pacman -S plasma-meta

sudo pacman -S kdebase-meta
sudo pacman -S kdegraphics-meta
sudo pacman -S kdeutils-meta
sudo pacman -S kdeadmin-meta
sudo pacman -S kdegames-meta
sudo pacman -S kde-gtk-config
```

### Login-Manager

KDE uses sddm (`sudo pacman -S sddm sddm-kcm` according to ).
Based on Google Images, the theme `breeze` is the same as `Manjaro` is using.

Changing keyboard-layout for login with `SDDM` (a display-manager for `KDE`) can be done in the file `/usr/share/sddm/scripts/Xsetup`.
Add the line

```zsh
setxkbmap de,us
```

to enable a selection.
More information from [askubuntu - Wrong language displayed by SDDM on login Kubuntu 18.04][www_askubuntu_sddm_wrong_lang] or [US keyboard layout always used][www_gentoo_sddm_us_keyboard_layout] or [ArchLinux Forum SDDM Keyboard Selection][www_archlinux_sddm_keyboard_selection].

### Wayland

- `sudo pacman -S plasma-wayland-session`
- [crashes with `RX 5700 XT`][www_kde_bug]

### Applications

If discover shows `No application back-ends found, please report to your distribution.`, then install `package-qt5` according to [this doc][www_discover_no_backends].

## Troubleshooting

`CTRL`, `ALT` and e.g. `F2` selects another `tty`.
This can be used to check logs or access the system if something is not running accordingly.

### Logging

Via `journalctl`, e.g. `journalctl --unit=sddm.service`

[www_arch_install_guide]: https://wiki.archlinux.org/index.php/installation_guide
[www_arch_group_overview]: https://www.archlinux.org/groups/
[www_stackoverflow_color_test]: https://askubuntu.com/questions/27314/script-to-display-all-terminal-colors
[www_arch_refind]: https://wiki.archlinux.org/index.php/REFInd#refind_linux.conf
[www_arch_steps_after_install]: https://itsfoss.com/things-to-do-after-installing-arch-linux/

[www_refind_theme_minimal]: https://github.com/EvanPurkhiser/rEFInd-minimal
[www_kde_bug]: https://bugs.kde.org/show_bug.cgi?id=413223
[www_discover_no_backends]: https://wiki.archlinux.org/index.php/KDE#Discover_does_not_show_any_applications

[www_askubuntu_sddm_wrong_lang]: https://askubuntu.com/questions/1040844/wrong-language-displayed-by-sddm-on-login-kubuntu-18-04
[www_gentoo_sddm_us_keyboard_layout]: https://forums.gentoo.org/viewtopic-t-1031606-start-0.html
[www_archlinux_sddm_keyboard_selection]: https://bbs.archlinux.org/viewtopic.php?id=194408
