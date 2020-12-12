# Raspberry Pi

There are plenty of help-pages, so this md-page just collects some useful snippets or links, but __IS NOT A COMPLETE GUIDE__.


## Table of Contents <a name="toc"></a>

1. [Notes when setting up the Raspberry Pi](#setup-raspi)
    1. [Handy commands](#handy_commands)
    1. [Install Ubuntu Server 20.4](#install-ubuntu-server-20.4)
    1. [Setup internet and update system](#setup_internet_and_update_system)
    1. [Setup user-management](#setup-user-management)
    1. [Setup ssh](#ssh)
    1. [Setup domain and connect it with your server](#setup_domain_and_ddns)


## Notes when setting up the Raspberry Pi <a name="setup-raspi"></a>

I'm using my Raspberry Pi with `Ubuntu Server 20.4` headlessly, so just plain in the cmdline, without any Desktop like `Gnome` installed.
In my experience, `Ubuntu` feels a bit heavy, but `Ubuntu Server 20.4` feels very light and is really easy to use.


### Handy commands <a name="handy_commands"></a>

Some handy commands, e.g. from [linuxhandbook][linuxhandbook/list_users_in_group] or [linuxhandbook][linuxhandbook/has_user_sudo-rights].

```zsh
# view all users
less /etc/passwd

# view all groups of the current user (or the user dominic)
groups
groups dominic

# view all existing groups
less /etc/group

# check if user dominic has sudo-rights
sudo -l -U dominic

# find all users in group sudo
grep '^sudo:.*$' /etc/group | cut -d: -f4
```


### Install Ubuntu Server 2.4 <a name="install-ubuntu-server-20.4"></a>

Installing `Ubuntu Server 20.4` is very simple using the `Raspberry Pi Imager`.
It's just writing the `OS` to the `SD`-card.


### Setup internet and update the system <a name="setup_internet_and_update_system"></a>

TODO


### Setup user-management <a name="setup-user-management"></a>

The initial user and password are predefined and probably `ubuntu` (both user and password).
Per default, this user `ubuntu` is in the `sudo`-, `wheel`- or `admin`-group (all three are kind of the same thing with different names for backwards-compatibility).

1. Change the initial password of the current user using the following command (`<username>` is probably `ubuntu`).

    ```zsh
    passwd
    ```

    This is important, since the default-user `ubuntu` is allowed to execute sudo-rights (even without being asked for the password).
    Later, when using `ssh` to access the system through your wifi-network (or Internet), this would be a __high risk__!

1. Set a root-password (or change the existing one?)

    ```zsh
    sudo passwd root
    ```

1. Attention: Edit `/etc/sudoers`, but only using `sudo visudo`.
    If you mess this file up, you can't access sudo-commands anymore.
    You can fix this by reinstalling the whole system or by booting with another OS (e.g. via USB-stick) to edit the file from there.
    That's why `sudo visudo` ensures, that your changes are valid and have no errors.
    I would add and/or edit following lines:

    ```zsh
    ## Optional and only recommended, if you are familiar with vim.
    ## Otherwise, don't add this line.
    ## It just ensures, that only vim is allowed to open sudoers with visudo,
    ## which helps when you have set ${VISUAL}=code
    Defaults editor=/usr/bin/vim:/usr/bin/vi

    ## User privilege specification
    ## user hostname=(runas-user:runas-group) command
    root ALL=(ALL:ALL) ALL

    ## Members of the admin group may gain root privileges admin is legacy, sudo
    ## is preferred
    %admin ALL=(ALL) ALL

    ## Allow members of group sudo to execute any command (but with password)
    %sudo ALL=(ALL:ALL) ALL

    ## I would delete this line, since this line allows sudo without being asked
    ## for root-password.
    #%sudo ALL=(ALL:ALL) ALL NOPASSWD: ALL

    ## I would highly recommend to delete this line, since a file in
    ## /etc/sudoers.d permits the user ubuntu to execute sudo without any
    ## password. Besides that, any file in there might corrupt your sudoers.
    ## #includedir /etc/sudoers.d
    ```

1. Create a new user for yourself (`-m` for a home-directory).

    ```zsh
    # create the user dominic
    #
    # -m
    # Create home-directory for this user
    #
    # -G sudo
    # Add this user to your sudo-group
    #
    # -s /usr/bin/bash
    # Set bash as default shell for this user (otherwise, it is probably dash)
    sudo useradd -m -G sudo -s /usr/bin/bash dominic
    sudo passwd dominic
    ```

1. Logout (just `logout`) and login with your new user.
    If everything seems to work fine, you can continue.
    It is important, that you can use `sudo` with this user.
    Otherwise, you have to login as root (and fix this), which is not recommended.

    ```zsh
    sudo -l -U dominic
    # or just, if logged in
    sudo -l
    ```

1. Remove `ubuntu` from all `sudo`-groups and delete the user.
    You can just execute the commands, even if the groups don't exist.

    ```zsh
    sudo deluser ubuntu admin
    sudo deluser ubuntu sudo
    # Probably not used in Ubuntu Server, but Arch Linux is using wheel
    # Execution doesn't matter, if this group doesn't exist.
    sudo deluser ubuntu wheel

    # delete the user
    sudo userdel ubuntu
    ```

### Setup ssh <a name="ssh"></a>

TODO


### Setup domain and connect it with your server <a name="setup_domain_and_ddns"></a>

TODO


[linuxhandbook/has_user_sudo-rights]: https://linuxhandbook.com/check-if-user-has-sudo-rights/
[linuxhandbook/list_users_in_group]: https://linuxhandbook.com/list-users-in-group-linux/
