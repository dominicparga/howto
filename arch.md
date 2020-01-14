# Arch Linux

There are plenty of help-pages, so this md-page just collects some useful snippets or links, but __IS NOT A COMPLETE GUIDE__.

Good pages to start

- [Arch installation guide][archlinux/wiki/installation-guide]
- as orientation (but don't install everything from there!): [Arch - steps after installation][itsfoss.com/steps-after-install]
- [Package-group overview][archlinux/groups]

## Table of Contents <a name="toc"></a>

1. [Notes when installing Arch](#install-arch)
    1. [Partitioning](#partitioning)
    1. [Add a user](#add-a-user)
    1. [systemd and systemctl](#systemd-and-systemctl)
    1. [wifi on reboot](#wifi-on-reboot)
    1. [Bootloader rEFInd](#refind)
1. [Notes when setting up Arch](#setup-arch)
    1. [GNOME](#gnome)
    1. [Display-Server (xorg, wayland)](#xorg-wayland)
    1. [KDE-Plasma5](#kde)
        1. [Desktop-Environment itself](#desktop-env)
        1. [Login-Manager](#login-mgr)
        1. [Wayland](#wayland)
        1. [Applications](#applications)
    1. [Install printer](#install-printer)
1. [General snippets and interesting stuff](#general)
    1. [Check colors in terminal](#check-colors-in-terminal)
    1. [Event-Listening with evtest](#evtest)
    1. [LaTeX or TeX Live](#latex)
    1. [Mouse-polling-rate](#mouse-polling-rate)
    1. [Python](#python)
    1. [Random-number-generator](#random-number-generator)
    1. [Check kernel-default-settings](#kernel-default-settings)
1. [Cool themes and icons](#themes-and-icons)
1. [Fonts](#fonts)
1. [Troubleshooting](#troubleshooting)
    1. [Logging](#logging)
    1. [Could not find tools on server when updating/installing tools](#tools-not-found-while-updating)
    1. [Unrecognized tools or external HDD or whatever](#unrecognized-tools)
    1. [Screen flicker after resume from suspend (Radeon GPU)](#screen-flicker-after-suspend)
    1. [CPU random generator seems to be failing (0xffffffff)](#0xffffffff)

## Notes when installing Arch <a name="install-arch"></a>

In addition to the [installation-guide on archwiki][archlinux/wiki/installation-guide], the following notes could be helpful and save google-time. `:)`

### Partitioning <a name="partitioning"></a>

Use `fdisk -l` to find the respective partition- and disk-names.
Note, that the `Device`-names for Disks, like `/dev/sdb` or `/dev/sda`, can change between reboots.
Hence don't use these names without lookup via `fdisk -l`.
Then, partition the disk-name (not a partition-name) via `fdisk`, e.g. `fdisk /dev/sdb`.
Made changes in the resulting mode will change the actual disk-partitions only if you save them.
So don't hesitate in executing the `fdisk`-command.

You will need following types, which can be added inside the `fdisk`-mode:

- `EFI System`
- `Linux filesystem`
- `Linux swap`

The swap-partition can have a size of `~4 GB`.
With hibernation (meaning saving RAM to HDD when turning off to restore RAM after reboot), you should take the whole RAM-size plus some extra space, but I don't use hibernation.

### Add a user <a name="add-a-user"></a>

```zsh
useradd -m -G wheel -s /usr/bin/zsh USERNAME
passwd USERNAME
visudo # for wheel-user-group
```

### systemd and systemctl <a name="systemd-and-systemctl"></a>

Basic systemctl-stuff can be found [here][archlinux/systemd#basic-usage]
Note that `enable` means the service to start automatically on reboot, while `start` means starting it right now for once.

### wifi on reboot <a name="wifi-on-reboot"></a>

Install `networkmanager` (including `nmcli`) for wifi and enable it on reboot via `systemctl enable NetworkManager.service` (should be explained in the Archwiki).

### Bootloader rEFInd <a name="refind"></a>

- [rEFInd installation guide for Arch][archlinux/wiki/refind#refind_linux.conf]
- [theme: rEFInd-minimal][github/evanprukhiser/refind-minimal]
- [configs inclusive rEFInd-minimal][github/dominicparga/refind]
- [Labeling the filesystem with Gnome's `disk`-utility][texmint.com/change-disk-partition-label] is needed for `rEFInd`s entry `volume` in a `menuentry`.
  You can check existing labels via `ll /dev/disk/by-label` (and `fdisk -l` for respective mount-names).
- Manual `stanzas` (`menuentry`s) and their options for `refind.conf` can be found [here][rodsbooks/refind/configfile#stanzas].
- `/efi/EFI/refind/refind.conf` vs `/boot/refind_linux.conf`: Former is the manually written config while latter is taken for automatically detected kernels.
  Take a look at [the archwiki][archlinux/wiki/refind_linux.conf] for more info.

### Configure Kernel

Take a look [at this super link][kernel/v5.4/params] for documentation of the options.
Note that you could have another version as used in the URL.

To check your kernel-version, execute `uname -r`.

## Notes when setting up Arch <a name="setup-arch"></a>

### GNOME <a name="gnome"></a>

Just install as mentioned in the Archwiki.
When logging in, the default is wayland, but currently (end 2019), wayland doesn't support app-switching, e.g. when `Enpass` wants to authenticate via `browser`, going back to the app afterwards.

### Display-Server (xorg, wayland) <a name="xorg-wayland"></a>

```zsh
sudo pacman -S xorg-server xorg-xinit
sudo pacman -S xf86-video-amdgpu
```

### KDE-Plasma5 <a name="kde"></a>

> deprecated

Repeadingly removes my home-directory when trying to uninstall a color-theme.
Hence goodbye KDE-Plasma, hello GNOME.

#### Desktop-Environment itself <a name="desktop-env"></a>

```zsh
sudo pacman -S plasma-meta

sudo pacman -S kdebase-meta
sudo pacman -S kdegraphics-meta
sudo pacman -S kdeutils-meta
sudo pacman -S kdeadmin-meta
sudo pacman -S kdegames-meta
sudo pacman -S kde-gtk-config
```

#### Login-Manager <a name="login-mgr"></a>

KDE uses sddm (`sudo pacman -S sddm sddm-kcm` according to ).
Based on Google Images, the theme `breeze` is the same as `Manjaro` is using.

Changing keyboard-layout for login with `SDDM` (a display-manager for `KDE`) can be done in the file `/usr/share/sddm/scripts/Xsetup`.
Add the line

```zsh
setxkbmap de,us
```

to enable a selection.
More information from [askubuntu - Wrong language displayed by SDDM on login Kubuntu 18.04][askubuntu/sddm-wrong-lang] or [US keyboard layout always used][gentoo/forum/sddm-us-keyboard-layout] or [ArchLinux Forum SDDM Keyboard Selection][archlinux/forum/sddm-keyboard-selection].

#### Wayland <a name="wayland"></a>

- `sudo pacman -S plasma-wayland-session`
- [crashes with `RX 5700 XT`][kde/bugs/plasma-wayland-crashes-after-login]

#### Applications <a name="applications"></a>

If discover shows `No application back-ends found, please report to your distribution.`, then install `package-qt5` according to [this doc][archlinux/wiki/kde#discover-no-backends].

### Install printer <a name="install-printer"></a>

```zsh
yay -S cups cups-pdf
yay -S hplip
```

Then enter `http://localhost:631/admin` and add a new printer.
In my case, the printer is `HP_Color_LaserJet_MFP_M277dw`, so I have added the respective PDD-file from [`hplib`][archlinux/pkgs/hplip] at `/usr/share/ppd/HP/hp-color_laserjet_pro_mfp_m277-ps.ppd.gz`
If your printer needs a plugin (execute `hp-plugin` after installing `hplip`), you will find it [at hp][hp/printer-plugin-list].

## General snippets and interesting stuff <a name="general"></a>

### Check colors in terminal <a name="check-colors-in-terminal"></a>

From [stackoverflow][askubuntu/color-test]

```zsh
msgcat --color=test
```

### Event-Listening with evtest <a name="evtest"></a>

Execute `sudo evtest` and follow instructions.

### LaTeX or TeX Live <a name="latex"></a>

Install the packages mentioned in the ArchWiki-page.

### Mouse-polling-rate <a name="mouse-polling-rate"></a>

Check with [`sudo evhz`][archlinux/wiki/mouse-polling-rate]

### Python <a name="python"></a>

Just install python and pip-modules with your package-manager (e.g. `yay`).
No need to use `pip` (yesss).

### Random-number-generator <a name="random-number-generator"></a>

```zsh
yay -S haveged
```

### Check kernel-default-settings <a name="kernel-default-settings"></a>

Snippet: `zcat /proc/config.gz | grep CONFIG_RANDOM_TRUST_CPU`

## Cool themes and icons <a name="themes-and-icons"></a>

Install them using `yay`, like `yay nordic-theme-git`.

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

- `Cascadia Code` via [github][github/wiki/cascadia-code/install] or [AUR][archlinux/pkgs/ttf-cascadia-code]
- `Fira Code` via [github][github/wiki/fira-code/install] or [AUR][archlinux/pkgs/otf-fira-code]
- `Inconsolata` via AUR

More useful fonts/fonts-pkgs can be found [in the Archwiki][archlinux/wiki/schriftarten], e.g.

- `ttf-liberation`, which is used in `libreoffice`-templates
- [`ttf-ms-win10`][www_aur_ttf_ms_win10], which is a wrapper for local ms-fonts.
  Microsoft-Fonts can be added from an Windows-ISO as described [in the Archwiki][archlinux/wiki/msfonts-from-iso].

## Troubleshooting <a name="troubleshooting"></a>

`CTRL`, `ALT` and e.g. `F2` selects another `tty`.
This can be used to check logs or access the system if something is not running accordingly.

### Logging <a name="logging"></a>

Via `journalctl`, e.g. `journalctl --unit=sddm.service`

### Could not find tools on server when updating/installing tools <a name="tools-not-found-while-updating"></a>

Arch is strict in versioning, meaning if your system is too old (could mean days), you won't find tools in the mirror-servers.
Just update the system (e.g. via `yay`) and reboot.

### Unrecognized tools or external HDD or whatever <a name="unrecognized-tools"></a>

If you have updated your system, e.g. via `yay`, do a restart.

Kernel-updates lead to missing support.
In my case the external HDD hasn't been detected anymore (`exFAT`).
I imagine, that old versions should be loaded that are already removed due to the system-update.
A restart fixed my problem with the unrecognized external HDD.

### Screen flicker after resume from suspend (Radeon GPU) <a name="screen-flicker-after-suspend"></a>

See [in the archlinux-wiki][archlinux/forum/radeon-screen-flicker]

### CPU random generator seems to be failing (0xffffffff) <a name="0xffffffff"></a>

__TL;DR__ Solution is updating BIOS (source: [Manjaro-Forum][manjaro/forum/cpu-rng-warning]).
If you have a motherboard from `msi` as I do, check [this 3-min-video][youtube/update-bios] out.

My AMD-CPU seems to have a bug or something, throwing the message

```text
WARNING: CPU random generator seem to be failing, disable hardware random number generation
WARNING: RDRND generated: 0xffffffff 0xffffffff 0xffffffff 0xffffffff
```

resulting in bad random numbers (only `fff...ff`) [when using `QT`][kde/invent/fix-rdm-init-on-amd-cpus] (e.g. in `matplotlib`).

You can check the random-number-generator of your cpu via the following c-script, using an inline-assembler-snippet to access the hardware-random-generator directly, not through your `OS`.

If the code is saved as script named `rdrand-test.c`, just execute `gcc rdrand-test.c && ./a.out` to print the random number.

```c
/*
   The code has been derived from systemd:
   https://github.com/systemd/systemd/blob/master/src/basic/random-util.c

   SPDX-License-Identifier: LGPL-2.1+
*/

#include <stdio.h>

int main() {
  unsigned char success;
  unsigned long v;
  asm volatile("rdrand %0;"
               "setc %1"
               : "=r"(v), "=qm"(success));

  printf("success: %i  value: %lx\n", success, v);
}
```

Though, you can check the output of `head -c 8 /dev/urandom | xxd`.
If it is random stuff, your `OS` probably has detected the issue by its own.

Source: [archlinux-forum][archlinux/forum/0xffffffff]

[archlinux/forum/0xffffffff]: https://bbs.archlinux.org/viewtopic.php?id=250624
[archlinux/forum/radeon-screen-flicker]: https://bbs.archlinux.org/viewtopic.php?id=237084
[archlinux/forum/sddm-keyboard-selection]: https://bbs.archlinux.org/viewtopic.php?id=194408
[archlinux/groups]: https://www.archlinux.org/groups/
[archlinux/pkgs]: https://www.archlinux.org/packages/
[archlinux/pkgs/hplip]: https://www.archlinux.org/packages/extra/x86_64/hplip/
[archlinux/pkgs/otf-fira-code]: https://www.archlinux.org/packages/community/any/otf-fira-code/
[archlinux/pkgs/ttf-cascadia-code]: https://www.archlinux.org/packages/community/any/ttf-cascadia-code/
[archlinux/pkgs/ttf-ms-win10]: https://aur.archlinux.org/packages/ttf-ms-win10/
[archlinux/systemd#basic-usage]: https://wiki.archlinux.org/index.php/Systemd#Basic_systemctl_usage
[archlinux/wiki/installation-guide]: https://wiki.archlinux.org/index.php/installation_guide
[archlinux/wiki/kde#discover-no-backends]: https://wiki.archlinux.org/index.php/KDE#Discover_does_not_show_any_applications
[archlinux/wiki/mouse-polling-rate]: https://wiki.archlinux.org/index.php/Mouse_polling_rate
[archlinux/wiki/msfonts-from-iso]: https://wiki.archlinux.org/index.php/Microsoft_fonts#Extracting_fonts_from_a_Windows_ISO
[archlinux/wiki/refind_linux.conf]: https://wiki.archlinux.org/index.php/REFInd#For_kernels_automatically_detected_by_rEFInd
[archlinux/wiki/refind#refind_linux.conf]: https://wiki.archlinux.org/index.php/REFInd#refind_linux.conf
[archlinux/wiki/schriftarten]: https://wiki.archlinux.de/title/Schriftarten
[askubuntu/color-test]: https://askubuntu.com/questions/27314/script-to-display-all-terminal-colors
[askubuntu/sddm-wrong-lang]: https://askubuntu.com/questions/1040844/wrong-language-displayed-by-sddm-on-login-kubuntu-18-04
[gentoo/forum/sddm-us-keyboard-layout]: https://forums.gentoo.org/viewtopic-t-1031606-start-0.html
[github/dominicparga/refind]: https://github.com/dominicparga/refind
[github/evanprukhiser/refind-minimal]: https://github.com/EvanPurkhiser/rEFInd-minimal
[github/wiki/cascadia-code/install]: https://github.com/microsoft/cascadia-code/wiki/Installing-Cascadia-Code
[github/wiki/fira-code/install]: https://github.com/tonsky/FiraCode/wiki/Linux-instructions#installing-with-a-package-manager
[hp/printer-plugin-list]: https://developers.hp.com/hp-linux-imaging-and-printing/binary_plugin.html
[itsfoss.com/steps-after-install]: https://itsfoss.com/things-to-do-after-installing-arch-linux/
[kde/bugs/plasma-wayland-crashes-after-login]: https://bugs.kde.org/show_bug.cgi?id=413223
[kde/invent/fix-rdm-init-on-amd-cpus]: https://invent.kde.org/kde/krita/commit/2fdd504dfe6ec63b654ee0878c9f95cb69d4a6ad
[kernel/v5.4/params]: https://www.kernel.org/doc/html/v5.4/admin-guide/kernel-parameters.html
[rodsbooks/refind/configfile#stanzas]: https://www.rodsbooks.com/refind/configfile.html#stanzas
[texmint.com/change-disk-partition-label]: https://www.tecmint.com/change-modify-linux-disk-partition-label-names/
[manjaro/forum/cpu-rng-warning]: https://forum.manjaro.org/t/i-get-a-cpu-random-generator-warning-advising-me-to-disable-hardware-random-number-generation/116796
[youtube/update-bios]: https://youtu.be/SgTokymDCcs
