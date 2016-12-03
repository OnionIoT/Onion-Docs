---
title: Using opkg
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 1
---

## What is OPKG?

Not everything available for the Omega is installed right away. Some people may never need certain utilities and so we configure the Omega with packages you will likely use, and let you further tailor your Omega to suit your needs.

This is accomplished with OPKG, the package manager for the Omega's Operating System. It is used primarily to download and install packages. If you're familiar with Linux or other Linux distributions then a good comparison for OPKG is the `apt-get` utility.

## How to use the Package Manager

The basic overview of managing your packages starts with updating OPKG. After that, you can add or remove packages, or show your available and installed packages.

### The Importance of `opkg update`

Running `opkg update`, provides the most recent list of packages available from Onion and OpenWRT. It's important to run `opkg update` in order to have the latest and greatest features from Onion ready for you to download.

To update OPKG, run:

```
opkg update
```

### Finding packages to install

To show all available packages in OPKG, run:

```
opkg list
```

This huge list can be very overwhelming and most of the time you want to find a package with a specific keyword. This can be easily done with `grep`.

The `grep` command allows you to filter your searches by keyword. For more information on the command, type `grep` into your console and press enter to get a full listing of the usage and available options.

To find all the packages that are Onion related, we'll use `grep` with the `-i` option to iGnOrE cAsE. Enter the following into your command line:

```
opkg list | grep -i onion-console
```
and you'll see all the available packages with onion-console in their name or description

```
root@Omega-2757:/# opkg list | grep -i onion-console
onion-console-base - 0.2-1 - Web-based virtual desktop for the Omega. Base package, only includes a few Apps.
onion-console-editor - 0.2-1 - Editor App for the Console
onion-console-terminal - 0.2-1 - Terminal App for the console
onion-console-webcam - 0.2-1 - Webcam App for the console
```

#### Listing Installed Packages
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

### Installing Packages

To install a package simply use the `opkg` command:

```
opkg install <PACKAGE NAME>
```

*Note: To find the package name you can use the `list` option from above.*

To install `curl` using OPKG, first run `opkg update` to retrieve all the latest packages:

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

and then run `opkg install curl` to install the package:

```
root@Omega-2757:/# opkg install curl
Installing curl (7.50.3-1) to root...
Downloading http://downloads.lede-project.org/snapshots/packages/mipsel_24kc/base/curl_7.50.3-1_mipsel_24kc.ipk.
Configuring curl.
```

`curl` is now installed on your Omega!


### Removing Packages

To remove a package from your Omega, use the `remove` option:

```
opkg remove <PACKAGE NAME>
```

*Note: To find the package name you can use the `list-installed` option from above.*

To remove `curl` with opkg:

```
root@Omega-2757:/# opkg remove curl
Removing package curl from root...
```
Curl is now removed from your Omega!


### Help With OPKG

To learn more about OPKG and it's functionality enter the command:

```
opkg -h
```
