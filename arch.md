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
    1. [Install Visual-Studio-Code](#install-vscode)
1. [General snippets and interesting stuff](#general)
    1. [vpn with openconnect](#openconnect)
    1. [Monitoring system-resources with htop](#htop)
    1. [Printing system-info](#printing-system-info)
    1. [Check colors in terminal](#check-colors-in-terminal)
    1. [Activate colors for pacman (and yay)](#activate_colors_for_pacman)
    1. [Event-Listening with evtest](#evtest)
    1. [LaTeX or TeX Live](#latex)
    1. [Mouse-polling-rate](#mouse-polling-rate)
    1. [Python](#python)
    1. [Random-number-generator](#random-number-generator)
    1. [Check kernel-default-settings](#kernel-default-settings)
    1. [Check existing groups](#check-existing-groups)
    1. [Linux Container with lxc/lxd](#linux-container)
1. [Cool themes and icons](#themes-and-icons)
1. [Fonts](#fonts)
1. [Troubleshooting](#troubleshooting)
    1. [Booting into black screen with blinking cursor](#booting_into_black_screen_with_blinking_cursor)
    1. [Login doesn't work after updating pam](#login_doesnt_work_after_updating_pam)
    1. [System-maintenance and logging](#system-maintenance_and_logging)
    1. [Could not find tools on server when updating/installing tools](#tools-not-found-while-updating)
    1. [Unrecognized tools or external HDD or whatever](#unrecognized-tools)
    1. [Screen flicker after resume from suspend (Radeon GPU)](#screen-flicker-after-suspend)
    1. [CPU random generator seems to be failing (0xffffffff)](#0xffffffff)
    1. [vscode's cmd 'Open Containing Folder' opens vscode instead of Files](#vscode-open-folder)
    1. [Can't read from NTFS-format (windows-partition)](#cant_read_from_ntfs-format)
    1. [Unrecognized mount option windows_names](#unrecognized_mount_option_windows_names)
    1. [sp5100-tco: Watchdog hardware is disabled](#sp5100-tco_watchdog_hardware_is_disabled)


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

Helpful commands:

```zsh
# Show little overview
nmcli

# Show network-devices (e.g. wifi-sticks)
ip link # or
nmcli device show

# List nearby wifi networks
nmcli device wifi list

# connect to a wifi network with password being asked interactively
nmcli --ask device wifi connect "${ssid}"

# OR

# connect to a wifi network without password being stored in history
vim tmp_pw.txt
ssid='my-wlan'
nmcli device wifi connect "${ssid}" password "$(cat tmp_pw.txt)"
rm tmp_pw.txt
```

### Bootloader rEFInd <a name="refind"></a>

- [rEFInd installation guide for Arch][archlinux/wiki/refind#refind_linux.conf]
- [theme: rEFInd-minimal][github/evanprukhiser/refind-minimal]
- [configs inclusive rEFInd-minimal][github/dominicparga/refind]
- [Labeling the filesystem with Gnome's `disk`-utility][texmint.com/change-disk-partition-label] is needed for `rEFInd`s entry `volume` in a `menuentry`.
  You can check existing labels via `ll /dev/disk/by-label` (and `fdisk -l` for respective mount-names).
- Manual `stanzas` (`menuentry`s) and their options for `refind.conf` can be found [here][rodsbooks/refind/configfile#stanzas].
- `/efi/EFI/refind/refind.conf` vs `/boot/refind_linux.conf`: Former is the manually written config while latter is taken for automatically detected kernels.
  Generate a `refind_conf.linux` via `mkrlconf`.
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
sudo systemctl start cups
# for automatically starting after reboot
sudo systemctl enable cups
```

Then enter `http://localhost:631/admin` and add a new printer.
In my case, the printer is `HP_Color_LaserJet_MFP_M277dw`, so I have added the respective PDD-file from [`hplib`][archlinux/pkgs/hplip] at `/usr/share/ppd/HP/hp-color_laserjet_pro_mfp_m277-ps.ppd.gz`

Whether your printer needs a plugin, you will find [at hp][hp/printer-plugin-list].
Executing `hp-plugin --interactive` after installing `hplip` should install the plugin.
__HOWEVER__, on my machine at `6th October 2020`, this doesn't work.
The error-message is something related to the checksum, but in fact, no file is downloaded at all.
Here is a workaround:

TLDR

- When executing `hp-plugin --help`, your version is printed.
  In my case, it is `3.20.6`.
- Download the `hplip-VERSION-plugin.run` and `hplip-VERSION-plugin.run.asc` of your version (`hp-plugin --help`) from [here][hplip/plugins].
- Execute `hp-plugin --interactive` and use the relative path to the directory, where you've just downloaded your plugin-files to.

```zsh
# get version
hp-plugin --help

# Download key
curl 'https://www.openprinting.org/download/printdriver/auxfiles/HP/plugins/hplip-VERSION-plugin.run.asc' -o "${HOME}/Downloads/hplip-VERSION-plugin.run.asc"

# Download plugin-files
curl 'https://www.openprinting.org/download/printdriver/auxfiles/HP/plugins/hplip-VERSION-plugin.run' -o "${HOME}/Downloads/hplip-VERSION-plugin.run"

# Install and use relative path to download-directory
hp-plugin --interactive --path="${HOME}/Downloads"

# Cleanup
rm "${HOME}/Downloads/hplip-VERSION-plugin.run"
rm "${HOME}/Downloads/hplip-VERSION-plugin.run.asc"
```

More details about finding the right files/urls

- Execute `which hp-plugin` to find the executable, which is a symlink.
- Follow the symlink to find the underlying `py`-script.
- When digging through this `py`-script (and imported modules in neighbouring `py`-scripts), you may find the download-url.
  In my case, the download-function is in `/usr/share/hplip/installer/pluginhandler.py`.
- In case the plugin-path (pointing to a local file) is empty, the download-function gathers info from [this config][hplip/plugin.conf].
- Search for your version in the config-file and find the url to the respective file `plugin.run`.
  The key-file `plugin.run.asc` is needed as well.
  Probably add `.asc` to the url, or simply remove the url's suffix to find all relevant files listed.
  In the list, look for your version (in my case, `hplip-3.20.6-plugin.run` and `hplip-3.20.6-plugin.run.asc`).


### Install Visual-Studio-Code <a name="install-vscode"></a>

I'm using the Open-Source-Build of `vscode`, installed via `yay -S code`, and it runs very nice.
Note that the `vscode-home-directory` changes.
For more information, see the [archwiki][archlinux/wiki/vscode].


## General snippets and interesting stuff <a name="general"></a>


### vpn with openconnect <a name="openconnect"></a>

See [archwiki about OpenConnect][archlinux/wiki/openconnect].
Don't forget the integration-section `;)`


### Monitoring system-resources with htop <a name="htop"></a>

[This blog][liquidweb/htop] explains some basics, for example the colors of the bars, which are:

For CPU-usage

- __Blue__: Low priority processes (nice > 0)
- __Green__: Normal (user-) processes
- __Red__: Kernel processes
- __Yellow__: IRQ time
- __Magenta__: Soft IRQ time
- __Grey__: IO wait-time

For memory-usage

- __Green__: Used memory-pages
- __Blue__: Buffer-pages
- __Yellow__: Cache-pages


### Printing system-info <a name="printing-system-info"></a>

You can use `uname -a` for quick-info.
For a more fancy output, do `yay -S archey4` followed by `archey` printing something like

```text
[dominic:~]$ archey

               +                 User: dominic
               #                 Hostname: aqua
              ###                Model: motherboard
             #####               Distro: Arch Linux [x86_64]
             ######              Kernel: 5.4.11-arch1-1
            ; #####;             Uptime: 26 minutes
           +##.#####             WindowManager: Not detected
          +##########            DesktopEnvironment: GNOME
         #############;          Shell: /usr/bin/zsh
        ###############+         Terminal: xterm-256color ## ## ## ## ## ## ##
       #######   #######         Packages: 1147
     .######;     ;###;`".       Temperature: 16.8 C (Max. 16.8 C)
    .#######;     ;#####.        CPU: ...
    #########.   .########`      GPU: ...
   ######'           '######     RAM: 1934 MB / 16024 MB
  ;####                 ####;    Disk: 167 GB / 522 GB
  ##'                     '##    LAN_IP: ...
 #'                         `#   WAN_IP: ...
```


### Check colors in terminal <a name="check-colors-in-terminal"></a>

From [stackoverflow][askubuntu/color-test]

```zsh
msgcat --color=test
```


### Activate colors for pacman (and yay) <a name="activate_colors_for_pacman"></a>

Uncomment `#Color` in `/etc/pacman.conf`.


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


### Check existing groups <a name="check-existing-groups">

```zsh
getent group
cat /etc/group

# Syntax
man group
```


### Linux Container with lxc/lxd <a name="linux-container"></a>

Info can be found [here][archlinux/wiki/lxd].

While `lxc` stands for `client`, the `lxd` represents the `daemon`.
The daemon provides a socket and has root-rights.
The client can send commands to this socket, e.g. to create containers.

Installing `lxc` and `lxd`:

```zsh
yay -S lxc lxd
```

You can launch privileged and unprivileged containers.
The former maps the container-root to the host-root, whereas the latter maps the container-root to some nobody-user.
For unprivileged containers, create a `uid`- and `gid`-mapping by creating `/etc/subuid` and `/etc/subgid`:

```text
root:100000:65536
```

Look at this [super youtube-tutorial][youtube/lxc] as soon as `lxc/lxd` are running.
The man in the video uses `lxc` without `sudo`.
__ATTENTION:__ You can do this by adding your user to the `lxd`-group via `usermod -a -G lxd <user>`.
This makes [privilege escalation][ubuntu/bugs/privilege-escalation] possible, basically meaning that this added user is able to create privileged containers, which can mount the host-system in and change everything with host-root-rights.
By the way, same holds for [`docker`][docker].


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
- [`ttf-ms-win10`][archlinux/pkgs/ttf-ms-win10], which is a wrapper for local ms-fonts.
  Microsoft-Fonts can be added from an Windows-ISO as described [in the Archwiki][archlinux/wiki/msfonts-from-iso].


## Troubleshooting <a name="troubleshooting"></a>

`CTRL`, `ALT` and e.g. `F2` selects another `tty`.
This can be used to check logs or access the system if something is not running accordingly.


### Booting into black screen with blinking cursor <a name="booting_into_black_screen_with_blinking_cursor"></a>

Solution: Switch `TTY` with `ALT`, `F2` and back with `ALT`, `F1`.


### Login doesn't work after updating pam <a name="login_doesnt_work_after_updating_pam"></a>

Once, after updating the system, login didn't work.
Reason for this was an update in a config of the login-service `pam`.
When `pacman` updated `pam`, the config `/etc/pam.d/system-login` had merge-conflicts with the new version.
To keep both versions, `pacman` adds the new version as `/etc/pam.d/system-login.pacnew`.
Problem has been, that the updated `pam` needs the new config to work, hence crashed (or something) and login didn't work (even for root).

To solve this: boot from an Bootalbe USB-stick, `chroot` into the system (see [installation-guide on archwiki][archlinux/wiki/installation-guide]) and resolve the merge-conflict.

In general, to find `pacnew`-files, you might play around with

`sudo find . -type f -exec grep -i "pacnew" --color=auto {} +`

for finding `.pacnew`-files.


### System-maintenance and logging <a name="system-maintenance_and_logging"></a>

Via `journalctl` and `systemctl`, e.g.

- `systemctl --failed`
- `journalctl -p 3 -xb`
- `journalctl --unit=sddm.service`

See [the archwiki][archlinux/wiki/system-maintenance] for very detailed info about system-maintenance.


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

__TLDR__ Solution is updating BIOS (source: [Manjaro-Forum][manjaro/forum/cpu-rng-warning]).
If you have a mainboard from `msi`, check [this 3-min-video][youtube/update-bios/msi].
For the `x570 Aorus Elite`, check [this video][youtube/update-bios/gigabyte].

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


### vscode's cmd 'Open Containing Folder' opens vscode instead of Files <a name="vscode-open-folder"></a>

The default-application for opening folders has changed somehow, but your gnome-settings doesn't show it in its section `Default Applications`.
To solve this,

1. open `Files`,
1. right-click on a folder,
1. select `Open With Other Application` (or similar)
1. and select `Files` since this is probably your preferred application to open folders.
1. Maybe (cannot tell since I just have done it): Restart all open `vscode`-windows.

Now, `vscode` should open containing folders in `Files` again.


### Can't read from NTFS-format (windows-partition) <a name="cant_read_from_ntfs-format"></a>

See [see troubleshooting for unrecognized mount option windows_names](#unrecognized_mount_option_windows_names)


### Unrecognized mount option windows_names <a name="unrecognized_mount_option_windows_names"></a>

Install `ntfs-3g`.

Source: [the ubuntu-forum][ubuntu/forum/unrecognized_mount_option_windows_names]


### sp5100-tco: Watchdog hardware is disabled <a name="sp5100-tco_watchdog_hardware_is_disabled"></a>

Add `blacklist sp5100_tco` to `/etc/modprobe.d/sp5100_tco.conf`.

Source: [archlinux-forum][archlinux/forum/watchdog_hardware_is_disabled]
See also: [archlinux-wiki for blacklisting kernel-modules][archlinux/wiki/kernel_module/blacklisting]


[archlinux/forum/0xffffffff]: https://bbs.archlinux.org/viewtopic.php?id=250624
[archlinux/forum/radeon-screen-flicker]: https://bbs.archlinux.org/viewtopic.php?id=237084
[archlinux/forum/sddm-keyboard-selection]: https://bbs.archlinux.org/viewtopic.php?id=194408
[archlinux/forum/watchdog_hardware_is_disabled]: https://bbs.archlinux.org/viewtopic.php?id=239075
[archlinux/groups]: https://www.archlinux.org/groups/
[archlinux/pkgs]: https://www.archlinux.org/packages/
[archlinux/pkgs/hplip]: https://www.archlinux.org/packages/extra/x86_64/hplip/
[archlinux/pkgs/otf-fira-code]: https://www.archlinux.org/packages/community/any/otf-fira-code/
[archlinux/pkgs/ttf-cascadia-code]: https://www.archlinux.org/packages/community/any/ttf-cascadia-code/
[archlinux/pkgs/ttf-ms-win10]: https://aur.archlinux.org/packages/ttf-ms-win10/
[archlinux/systemd#basic-usage]: https://wiki.archlinux.org/index.php/Systemd#Basic_systemctl_usage
[archlinux/wiki/installation-guide]: https://wiki.archlinux.org/index.php/installation_guide
[archlinux/wiki/kde#discover-no-backends]: https://wiki.archlinux.org/index.php/KDE#Discover_does_not_show_any_applications
[archlinux/wiki/kernel_module/blacklisting]: https://wiki.archlinux.org/index.php/Kernel_module#Blacklisting
[archlinux/wiki/lxd]: https://wiki.archlinux.org/index.php/LXD
[archlinux/wiki/mouse-polling-rate]: https://wiki.archlinux.org/index.php/Mouse_polling_rate
[archlinux/wiki/msfonts-from-iso]: https://wiki.archlinux.org/index.php/Microsoft_fonts#Extracting_fonts_from_a_Windows_ISO
[archlinux/wiki/openconnect]: https://wiki.archlinux.org/index.php/OpenConnect
[archlinux/wiki/refind_linux.conf]: https://wiki.archlinux.org/index.php/REFInd#For_kernels_automatically_detected_by_rEFInd
[archlinux/wiki/refind#refind_linux.conf]: https://wiki.archlinux.org/index.php/REFInd#refind_linux.conf
[archlinux/wiki/schriftarten]: https://wiki.archlinux.de/title/Schriftarten
[archlinux/wiki/system-maintenance]: https://wiki.archlinux.org/index.php/System_maintenance
[archlinux/wiki/vscode]: https://wiki.archlinux.org/index.php/Visual_Studio_Code
[askubuntu/color-test]: https://askubuntu.com/questions/27314/script-to-display-all-terminal-colors
[askubuntu/sddm-wrong-lang]: https://askubuntu.com/questions/1040844/wrong-language-displayed-by-sddm-on-login-kubuntu-18-04
[docker]: https://www.docker.com/
[gentoo/forum/sddm-us-keyboard-layout]: https://forums.gentoo.org/viewtopic-t-1031606-start-0.html
[github/dominicparga/refind]: https://github.com/dominicparga/refind
[github/evanprukhiser/refind-minimal]: https://github.com/EvanPurkhiser/rEFInd-minimal
[github/wiki/cascadia-code/install]: https://github.com/microsoft/cascadia-code/wiki/Installing-Cascadia-Code
[github/wiki/fira-code/install]: https://github.com/tonsky/FiraCode/wiki/Linux-instructions#installing-with-a-package-manager
[hp/printer-plugin-list]: https://developers.hp.com/hp-linux-imaging-and-printing/binary_plugin.html
[hplip/plugin.conf]: http://hplip.sf.net/plugin.conf
[hplip/plugins]: http://www.openprinting.org/download/printdriver/auxfiles/HP/plugins/
[itsfoss.com/steps-after-install]: https://itsfoss.com/things-to-do-after-installing-arch-linux/
[kde/bugs/plasma-wayland-crashes-after-login]: https://bugs.kde.org/show_bug.cgi?id=413223
[kde/invent/fix-rdm-init-on-amd-cpus]: https://invent.kde.org/kde/krita/commit/2fdd504dfe6ec63b654ee0878c9f95cb69d4a6ad
[kernel/v5.4/params]: https://www.kernel.org/doc/html/v5.4/admin-guide/kernel-parameters.html
[liquidweb/htop]: https://www.liquidweb.com/kb/featured-freeware-htop/
[manjaro/forum/cpu-rng-warning]: https://forum.manjaro.org/t/i-get-a-cpu-random-generator-warning-advising-me-to-disable-hardware-random-number-generation/116796
[rodsbooks/refind/configfile#stanzas]: https://www.rodsbooks.com/refind/configfile.html#stanzas
[texmint.com/change-disk-partition-label]: https://www.tecmint.com/change-modify-linux-disk-partition-label-names/
[ubuntu/bugs/privilege-escalation]: https://bugs.launchpad.net/ubuntu/+source/lxd/+bug/1829071
[ubuntu/forum/unrecognized_mount_option_windows_names]: https://ubuntuforums.org/showthread.php?t=1902606
[youtube/lxc]: https://youtu.be/CWmkSj_B-wo
[youtube/update-bios/gigabyte]: https://youtu.be/1SiJpDQ083Q
[youtube/update-bios/msi]: https://youtu.be/SgTokymDCcs
