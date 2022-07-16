Status: published
Date: 2020-01-24 10:37:18
Modified: 2022-07-16 12:45:06
Author: Benjamin Du
Slug: manage-systemd-services-units
Title: Manage systemd Services and Units
Category: OS
Tags: OS, Linux, systemd, service, systemctl, enable, disable, start, stop, restart

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


1. List all services names.

        :::bash
        service --status-all

1. List all systemd units.

        :::bash
        systemctl 

3. Disable a service.

        :::bash
        systemctl disable service_name

2. Check whether systemd is running as PID 1.

        :::bash
        ps --no-headers -o comm 1

## A List of Services to Disable

### Safe to Disable

1. bluetooth

        :::bash
        sudo systemctl disable bluetooth

2. openvpn

        :::bash
        sudo systemctl disable openvpn

3. virtualbox

        :::bash
        sudo systemctl disable virtualbox


4. packagekit

        :::bash
        sudo systemctl mask packagekit

    Notice that subcommand `systemctl mask` (instead of `systemctl disable`) is used
    as `systemctl disable` does not work in this case.
    For the difference between `systemctl disable` and `systemctl mask`,
    please refer to
    [What is the difference between "systemctl mask" and "systemctl disable"?](https://askubuntu.com/questions/816285/what-is-the-difference-between-systemctl-mask-and-systemctl-disable)
    .

### Controversial Ones

1. snapd

        :::bash
        sudo systemctl disable snapd.service
        sudo systemctl disable snapd.socket
        sudo systemctl disable snapd.seeded
        sudo systemctl disable snapd.snap-repair.timer

## References

- [How to know if I am using systemd on Linux?](https://superuser.com/questions/1017959/how-to-know-if-i-am-using-systemd-on-linux)

- [Convenient way to check if system is using systemd or sysvinit in BASH? [duplicate]](https://unix.stackexchange.com/questions/121654/convenient-way-to-check-if-system-is-using-systemd-or-sysvinit-in-bash)

- [How To Use Systemctl to Manage Systemd Services and Units](https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units)

- [What is the difference between "systemctl mask" and "systemctl disable"?](https://askubuntu.com/questions/816285/what-is-the-difference-between-systemctl-mask-and-systemctl-disable)
