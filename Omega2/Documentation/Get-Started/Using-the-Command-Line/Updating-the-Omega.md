---
title: Updating the Omega
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 8
---

## Updating the Omega {#updating-the-omega}

In order to keep improving user experience for the Omega, we will be releasing updated firmwares on a rolling basis. To get the benefits of these improvements, users should frequently update their Omegas to the latest firmware release. We have created a command-line utility `oupgrade` (Onion Upgrade) to handle firmware transitions.

### How do I know if I need to update my Omega?

To check if your Omega needs an upgrade, run `oupgrade -check`. The output will let you know if you need an update:
```
root@Omega-2757:/# oupgrade -c
> Device Firmware Version: 0.1.4 b210
> Checking latest version online...
> Repo Firmware Version: 0.1.5 b132
> Comparing version numbers
> New firmware version available, need to upgrade device firmware
```

The easiest thing to do is to just run `oupgrade`. This way it will check if your firmware needs updating and will perform the upgrade if necessary.

***The `oupgrade` command will not work properly if you run it from the Terminal App on the Console.***

#### Versions vs. Build Numbers

Every firmware has a **version** and **build number**.

* Minor updates will be released as new build numbers for a given firmware version.
    * eg. version 0.1.4 build 100, build 103, build 110
* Major updates will be released as a new firmware version.
    * eg. version 0.1.3, version 0.1.5, version 0.1.6


### Performing the Upgrade

#### Using `oupgrade`

To run the `oupgrade` tool, simply enter the following in your command-line:

```
oupgrade
```

It will take care of checking for firmware updates, and automatically installing them if they are available.

By default, `oupgrade` will only install new firmware **versions**.

#### Doing More with `oupgrade`

##### Getting your firmware version

To get the current firmware installed on the device type:

```
oupgrade -v
```

And you'll see:

```
root@Omega-2757:/# oupgrade -v
> Device Firmware Version: 0.1.5 b132
```

Here we're on version `0.1.5` and build `132` of the device firmware.


##### Checking for New Firmware Versions

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

As you can see from the output, our firmware is up to date!

If it were not up to date, this command would show:
```
root@Omega-2757:/# oupgrade -c
> Device Firmware Version: 0.1.5 b131
> Checking latest version online...
> Repo Firmware Version: 0.1.5 b132
> Comparing version numbers
> New build of current firmware available, upgrade is optional, rerun with '-force' option to upgrade
```

or if you're on an older version:

```
root@Omega-2757:/# oupgrade -c
> Device Firmware Version: 0.1.4 b210
> Checking latest version online...
> Repo Firmware Version: 0.1.5 b132
> Comparing version numbers
> New firmware version available, need to upgrade device firmware
```

*This command only checks for the latest firmware version and will not modify your device.*


##### Upgrading to the Latest Version #{updating-the-omega-latest-version}
Here at Onion we're constantly developing, adding new features and fixing bugs. However, sometimes the features we release may cause the firmware to be unstable. Normally `oupgrade` will only upgrade to the latest **stable** version, skipping any unstable versions.

If you need to upgrade to the latest version anyway, you can type:
```
oupgrade -l
```

**Note: This is not recommended unless you know what you're doing!**

This will not reflash the Omega if the latest firmware is already installed.

##### Force Update/Reflash

You can force `oupgrade` to reflash the Omega with the latest firmware using the `-f` flag. **Note: This will reinstall the firmware even if the Omega already has the latest available!**

```
oupgrade -f
```

Since this will cause the Omega to reflash itself, this can be used in case you need to safely reset to a working state on the latest firmware.

**IMPORTANT:** See the warning below about what files will be preserved and erased when upgrading the firmware.

### Warning: File Preservation

When an upgrade is performed, only the `/root` and `/etc` folders are preserved. It is important to backup your files on the Omega prior to upgrading if you don't want to lose any of your work.

### Help with `oupgrade`

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
