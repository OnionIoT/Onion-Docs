---
title: Updating the Omega
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 8
---

# Updating the Omega

In order to keep improving user experience for the Omega, we will be releasing updated firmwares on a rolling basis. To capitalize on these improvements users should update their Omegas to the latest firmware release. To handle firmware transitions we have created a command-line utility `oupgrade` (Onion Upgrade).

## Using the Command line

// explain how the average user will use this tool
// doing more - check, latest, force
`oupgrade` has a lot of functionality on the command line. Type

```
oupgrade -h
```

to get the usage output.

```
root@Omega-2757:/# oupgrade -h
Functionality:
  Check if new Onion firmware is available and perform upgrade

Usage: /usr/bin/oupgrade

Arguments:
 -h, --help        Print this usage prompt
 -v, --version     Just print the current firmware version
 -l, --latest      Use latest repo version (instead of stable version)
 -f, --force       Force the upgrade, regardless of versions
 -c, --check       Only compare versions, do not actually update
 -u, --ubus        Script outputs only json
```


To get the current firmware installed on the device type:
```
oupgrade -v
```

And you'll see:
```
root@Omega-2757:/# oupgrade -v
> Device Firmware Version: 0.1.5 b132
```

Here I'm on version 0.1.5 and build 132 of the device firmware.

To check your firmware version and compare it with the latest available firmware versions type:
```
oupgrade -c
```

```
root@Omega-2757:/# oupgrade -c
> Device Firmware Version: 0.1.5 b132
> Checking latest version online...
> Repo Firmware Version: 0.1.5 b132
> Comparing version numbers
> Device firmware is up to date!
```

As you can see from the output, my firmware is up to date!

Here at Onion we are constantly in development, adding new features and fixing bugs. Sometimes the features we make cause the firmware to be unstable. `oupgrade` will only upgrade to the latest stable version as opposed to the latest version available.

To upgrade to the latest version (instead of stable version) you can type:
```
oupgrade -l
```
**Note: This is not recommended unless you know what you're doing!**


You can also force `oupgrade` to upgrade to the latest version of the firmware with the `-f` flag:
```
oupgrade -f
```



## Notes On Upgrades

When an upgrade is performed, only the `root` and `etc` folders are preserved. It is important to backup your work on the Omega prior to upgrading if you don't want to lose any of your work.
