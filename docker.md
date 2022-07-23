# Docker

The main purpose of this description here is being a collection of some useful snippets or links.

## Table of Contents


## Installation and setup

- See [YouTube: Raspberry Pi Cloud](https://youtu.be/-jLdkDxCDMo)
- See docker-documentation.
  Basically every snippet here is somehow copy-pasted from there, if not stated otherwise.

### Docker-group and root-privileges

__ATTENTION:__ You can use `docker` without `sudo` by adding your user to the `docker`-group via `usermod -a -G docker "${USER}"`.
However, this makes [privilege escalation](https://bugs.launchpad.net/ubuntu/+source/lxd/+bug/1829071) possible, basically meaning that this added user is able to create privileged containers, which can mount the host-system in and change everything with host-root-rights.
Therefore, I do not recommend adding your user to the group `docker`.
Instead, better keep `sudo docker`.

### Firewall

According to [techrepublic](https://www.techrepublic.com/article/how-to-fix-the-docker-and-ufw-security-flaw/), Docker ignores UFW.
You can fix this by adding

    DOCKER_OPTS="--iptables=false"

to `/etc/default/docker`.

### Logging

To prevent your logs to exhaust your disk resources, create `/etc/docker/daemon.json` (see [docs.docker.com](https://docs.docker.com/config/containers/logging/json-file/))

```json
// in /etc/docker/daemon.json
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3" 
  }
}
```

## After setup

- See `docker scan`
