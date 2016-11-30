---
title: Using opkg
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 1
---


# What is OPKG?


OPKG is the package manager for the Omega Firmware. Installation and removal of packages available to the Omega Firmware is made simple using OPKG.

# How to use the Package Manager

The basic operation of the package manager starts off with updating OPKG. After that, you can add or remove packages, and list available and installed packages.

## The Importance of `opkg update`

Running `opkg update`, provides the most recent list of packages available from the firmware Repos as well as their respective checksums. The latter is to ensure the integrity and security of the package being downloaded and installed.

To update OPKG, run:

```
opkg update
```

## Help With OPKG

To see the OPKG usage, run:

```
opkg -h
```

`opkg` has a lot of functionality, and this tutorial will show you the most important commands to know with `opkg`

## Finding packages to install

To show all available packages in OPKG, run:

```
opkg list
```

This huge list can be very overwhelming and most of the time you want to find a package with a specific keyword. This can be easily done with `grep`.

`grep` allows you to filter your searches by keyword. For more information on `grep` type it into your console and press enter:

```
root@Omega-2757:/# grep
BusyBox v1.25.1 () multi-call binary.

Usage: grep [-HhnlLoqvsriwFE] [-m N] [-A/B/C N] PATTERN/-e PATTERN.../-f FILE [FILE]...

Search for PATTERN in FILEs (or stdin)

        -H      Add 'filename:' prefix
        -h      Do not add 'filename:' prefix
        -n      Add 'line_no:' prefix
        -l      Show only names of files that match
        -L      Show only names of files that don't match
        -c      Show only count of matching lines
        -o      Show only the matching part of line
        -q      Quiet. Return 0 if PATTERN is found, 1 otherwise
        -v      Select non-matching lines
        -s      Suppress open and read errors
        -r      Recurse
        -i      Ignore case
        -w      Match whole words only
        -x      Match whole lines only
        -F      PATTERN is a literal (not regexp)
        -E      PATTERN is an extended regexp
        -m N    Match up to N times per file
        -A N    Print N lines of trailing context
        -B N    Print N lines of leading context
        -C N    Same as '-A N -B N'
        -e PTRN Pattern to match
        -f FILE Read pattern from file

```

To find all the packages that are Onion related, we'll use `grep` with the `-i` option to iGnOrE cAsE, type:

```
opkg list | grep -i onion
```
and you'll see all the available packages with Onion in their name or description

```
root@Omega-2757:/# opkg list | grep -i onion
arduino-dock-2 - 0.1-1 - Tools for using Onion Arduino Dock 2
base-www - 0.1-1 - Files for website hosting on the Omega to ensure compatibility between Onion utilities
device-client - 0.6-1 - Client for communication with Onion Cloud Device Server
liboniondebug - 0.4-1 - Library used to ease debug
libonioni2c - 0.4-1 - Library of I2C communication functions
libonionili9341 - 0.1-1 - Library for TFT ILI9341 Driver
libonionmcp23008 - 0.4-1 - Library of functions for MCP23008 chips
libonionneopixel - 0.1-1 - Library that provides functions to interact with Neopixels via the Arduino Dock
libonionoledexp - 0.4-1 - Library of functions to control the Onion OLED Expansion
libonionpwmexp - 0.4-1 - Library of functions to control the PWM Expansion
libonionrelayexp - 0.4-1 - Library of functions to control the Onion Relay Expansion
libonionspi - 0.1-1 - Library of SPI communication functions
onion-console-base - 0.2-1 - Web-based virtual desktop for the Omega. Base package, only includes a few Apps.
onion-console-editor - 0.2-1 - Editor App for the Console
onion-console-terminal - 0.2-1 - Terminal App for the console
onion-console-webcam - 0.2-1 - Webcam App for the console
onion-helper - 0.1-1 - C-based ubus service to implement various features on OpenWRT
onion-repo-keys - 0.1-1 - Signature keys required for Onion Package Repo
onion-sh-lib - 0.2-1 - Library of commonly used code for the Omega
onion-ubus - 0.1-1 - Collection of Onion ubus tools
oupgrade - 0.1-1 - Tool to upgrade device firmware with latest from Onion repo
power-dock - 0.2-1 - Onion Power Dock Drivers
pyOledExp - 0.4-1 - Python module to control the Onion OLED Expansion
pyOnionGpio - 0.1-1 - Python module with object that implements programming the GPIOs via the sysfs interface
pyOnionI2C - 0.4-1 - Python module with object that implements I2C transactions
pyOnionSpi - 0.1-1 - Python module to implement communication via the SPI protocol
pyPwmExp - 0.4-1 - Python module to control the Onion PWM Expansion
pyRelayExp - 0.4-1 - Python module to control the Onion Relay Expansion
```

You can also check your installed packages with

```
opkg list-installed
```

Let's try the same `grep` option but with `opkg list-installed` now:

```
opkg list-installed | grep -i onion
```

and the output will look similar to the following:

```
root@Omega-2757:/# opkg list-installed | grep -i onion
liboniondebug - 0.4-1
libonioni2c - 0.4-1
libonionmcp23008 - 0.4-1
libonionoledexp - 0.4-1
libonionpwmexp - 0.4-1
libonionrelayexp - 0.4-1
onion-console-base - 0.2-1
onion-console-webcam - 0.2-1
onion-helper - 0.1-1
onion-repo-keys - 0.1-1
onion-sh-lib - 0.2-1
onion-ubus - 0.1-1
```

## Installing Packages

To install a package simply use the `opkg` command:

```
opkg install <PACKAGE NAME>
```

**Note: To find the package name you can use the `list` option from above.**

To install `curl` using OPKG run `opkg update`:

```
root@Omega-2757:/# opkg update
Downloading http://downloads.lede-project.org/snapshots/targets/ramips/mt7688/packages/Packages.gz.
Updated list of available packages in /var/opkg-lists/reboot_core.
Downloading http://downloads.lede-project.org/snapshots/targets/ramips/mt7688/packages/Packages.sig.
Signature check passed.
Downloading http://downloads.lede-project.org/snapshots/packages/mipsel_24kc/base/Packages.gz.
Updated list of available packages in /var/opkg-lists/reboot_base.
Downloading http://downloads.lede-project.org/snapshots/packages/mipsel_24kc/base/Packages.sig.
Signature check passed.
Downloading http://repo.onion.io/omega2/packages/Packages.gz.
Updated list of available packages in /var/opkg-lists/reboot_onion.
Downloading http://repo.onion.io/omega2/packages/Packages.sig.
Signature check passed.
Downloading http://downloads.lede-project.org/snapshots/packages/mipsel_24kc/packages/Packages.gz.
Updated list of available packages in /var/opkg-lists/reboot_packages.
Downloading http://downloads.lede-project.org/snapshots/packages/mipsel_24kc/packages/Packages.sig.
Signature check passed.
```

and then run `opkg install curl`:

```
root@Omega-2757:/# opkg install curl
Installing curl (7.50.3-1) to root...
Downloading http://downloads.lede-project.org/snapshots/packages/mipsel_24kc/base/curl_7.50.3-1_mipsel_24kc.ipk.
Configuring curl.
```

`curl` is now installed on your Omega!

## Removing Packages

To remove a package:

```
opkg remove <PACKAGE NAME>
```

**Note: To find the package name you can use the `list-installed` option from above.**

To remove `curl` with opkg:

```
root@Omega-2757:/# opkg remove curl
Removing package curl from root...
```
Curl is now removed from your Omega!
