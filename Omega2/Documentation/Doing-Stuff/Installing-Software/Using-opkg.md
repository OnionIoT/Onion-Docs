---
title: Using opkg
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 1
---

## What is OPKG? {#using-opkg}

Not everything available for the Omega is installed right away. Some people may never need certain utilities and so we configure the Omega with packages you will likely use, and let you further tailor your Omega to suit your needs.

This is accomplished with OPKG, the package manager for the Omega's Operating System. It is used primarily to download and install packages. If you're familiar with Linux or other Linux distributions then a good comparison for OPKG is the `apt-get` utility.

Here you'll learn how to use the OPKG package manager and get some background on the Onion repositories from which the software packages will be installed.

### How to use the Package Manager

The basic overview of managing your packages starts with updating OPKG. After that, you can add or remove packages, or show your available and installed packages.

#### The Importance of `opkg update`

Running `opkg update`, provides the most recent list of packages available from Onion's package repositories. It's important to run `opkg update` in order to have the latest and greatest features from Onion ready for you to download.

To update OPKG, run:

```
opkg update
```

When this command runs, opkg will connect to the configured package repositories and find out which packages are available for installation.

**Note that if you do not run `opkg update`, it will not know which packages are available and will not be able to install anything!***

#### Finding packages to install

To show all available packages in OPKG, run:

```
opkg list
```

This huge list can be very overwhelming and most of the time you want to find a package with a specific keyword. This can be easily done with `grep`.

The `grep` command allows you to filter your searches by keyword. For more information on the command, type `grep` into your console and press enter to get a full listing of the usage and available options.

To find all the packages that are Onion related, we'll use `grep` with the `-i` option to iGnOrE cAsE. Enter the following into your command line:

```
opkg list | grep -i kmod-usb
```
and you'll see all the available packages with `kmod-usb` in their name or description

```
root@Omega-2757:/# opkg list | grep -i kmod-usb
kmod-usb-acm - 4.14.81-1 - Kernel support for USB ACM devices (modems/isdn controllers)
kmod-usb-audio - 4.14.81-1 - Kernel support for USB audio devices
kmod-usb-core - 4.14.81-1 - Kernel support for USB
kmod-usb-ehci - 4.14.81-1 - EHCI controller support
kmod-usb-hid - 4.14.81-1 - Kernel support for USB HID devices such as keyboards and mice
kmod-usb-net - 4.14.81-1 - Kernel modules for USB-to-Ethernet convertors
...
```

##### Listing Installed Packages
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

#### Installing Packages

To install a package simply use the `opkg` command:

```
opkg install <PACKAGE NAME>
```

*Note: To find the package name you can use the `list` option from above.*

To install `curl` using OPKG, first run `opkg update` to retrieve all the latest packages:

```
root@Omega-2757:/# opkg update
Downloading http://downloads.lede-project.org/snapshots/targets/ramips/mt76x8/packages/Packages.gz.
Updated list of available packages in /var/opkg-lists/reboot_core.
Downloading http://downloads.lede-project.org/snapshots/targets/ramips/mt76x8/packages/Packages.sig.
Signature check passed.
Downloading http://downloads.lede-project.org/snapshots/packages/mipsel_24kc/base/Packages.gz.
Updated list of available packages in /var/opkg-lists/reboot_base.
Downloading http://downloads.lede-project.org/snapshots/packages/mipsel_24kc/base/Packages.sig.
Signature check passed.
Downloading http://repo.onioniot.com/omega2/packages/Packages.gz.
Updated list of available packages in /var/opkg-lists/reboot_onion.
Downloading http://repo.onioniot.com/omega2/packages/Packages.sig.
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


#### Removing Packages

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


#### Help With OPKG

To learn more about OPKG and it's functionality enter the command:

```
opkg -h
```



### The Onion Package Repo {#onion-package-repo}

As of firmware version 0.1.7 and later, `opkg` is configured to grab packages from Onion's package repositories. As a result, you can now successfully install kernel modules, however, we host a smaller selection of packages than the official OpenWRT repositories.

The Onion package repo can be found here: http://repo.onioniot.com/omega2/packages/

#### How `opkg` is Configured

The path to the package repos that `opkg` checks during the `opkg update` command can be found at `/etc/opkg/distfeeds.conf`.

#### Installing Kernel Modules

While the Omega comes with many handy kernel modules already installed, your project or idea might require some additional modules. Since all of the packages in the Onion repos are compiled by Onion, your Omega running Onion firmware will have no problems installing kernel modules using `opkg`:

```
opkg update
opkg install kmod-fs-hfs
```

> Note that your Omega cannot install kernel modules from the default LEDE repos. `opkg` only allows installation of kernel modules compiled by the same machine that compiled the firmware. This is to ensure that all installed kernel modules are the exact same version as the device's kernel. It would be pretty disastrous to install a module that expects a different version of the overall kernel so `opkg` never lets it happen!

For best results, make sure you're on the `latest` Omega firmware. Take a look at our guide on [updating the Omega](#updating-the-omega) for steps on how to install the `latest` firmware.


### You don't Have a Package I Want/Need!

By default, `opkg` on the Omega2 platform is configured use Onion's online package repositories. We host a selection of packages that are frequently used by the Omega2 userbase. However, the official OpenWRT repositories host a larger selection of packages.

If you're looking for a specific package and it isn't available by default, you can try enabling the official OpenWRT package repositories on your Omega. Read on for more details.

### Enable the Official OpenWRT Package Repos {#using-opkg-switch-to-lede-repos}

It's very straightforward to configure `opkg` to use the OpenWRT package repos in addition to the Onion package repos. This can be accomplished by editing the `/etc/opkg/distfeeds.conf` file that configures which repos are to be used.

By default, it will be configured to use the Onion repos and will look something like this:
```
#src/gz openwrt_core http://downloads.openwrt.org/releases/18.06-SNAPSHOT/targets/ramips/mt76x8/packages
#src/gz openwrt_base http://downloads.openwrt.org/releases/18.06-SNAPSHOT/packages/mipsel_24kc/base
#src/gz openwrt_luci http://downloads.openwrt.org/releases/18.06-SNAPSHOT/packages/mipsel_24kc/luci
#src/gz openwrt_onion http://downloads.openwrt.org/releases/18.06-SNAPSHOT/packages/mipsel_24kc/onion
#src/gz openwrt_packages http://downloads.openwrt.org/releases/18.06-SNAPSHOT/packages/mipsel_24kc/packages
#src/gz openwrt_routing http://downloads.openwrt.org/releases/18.06-SNAPSHOT/packages/mipsel_24kc/routing
#src/gz openwrt_telephony http://downloads.openwrt.org/releases/18.06-SNAPSHOT/packages/mipsel_24kc/telephony
src/gz omega2_core http://repo.onioniot.com/omega2/packages/core
src/gz omega2_base http://repo.onioniot.com/omega2/packages/base
src/gz omega2_packages http://repo.onioniot.com/omega2/packages/packages
src/gz omega2_routing http://repo.onioniot.com/omega2/packages/routing
src/gz omega2_onion http://repo.onioniot.com/omega2/packages/onion
```

The commented out lines in the file are not active. To enable the official OpenWRT repos, just uncomment those lines. 
```
src/gz openwrt_core http://downloads.openwrt.org/releases/18.06-SNAPSHOT/targets/ramips/mt76x8/packages
src/gz openwrt_base http://downloads.openwrt.org/releases/18.06-SNAPSHOT/packages/mipsel_24kc/base
#src/gz openwrt_luci http://downloads.openwrt.org/releases/18.06-SNAPSHOT/packages/mipsel_24kc/luci
#src/gz openwrt_onion http://downloads.openwrt.org/releases/18.06-SNAPSHOT/packages/mipsel_24kc/onion
src/gz openwrt_packages http://downloads.openwrt.org/releases/18.06-SNAPSHOT/packages/mipsel_24kc/packages
#src/gz openwrt_routing http://downloads.openwrt.org/releases/18.06-SNAPSHOT/packages/mipsel_24kc/routing
#src/gz openwrt_telephony http://downloads.openwrt.org/releases/18.06-SNAPSHOT/packages/mipsel_24kc/telephony
src/gz omega2_core http://repo.onioniot.com/omega2/packages/core
src/gz omega2_base http://repo.onioniot.com/omega2/packages/base
src/gz omega2_packages http://repo.onioniot.com/omega2/packages/packages
src/gz omega2_routing http://repo.onioniot.com/omega2/packages/routing
src/gz omega2_onion http://repo.onioniot.com/omega2/packages/onion
```

> It's up to you to if you want to comment out the Onion packages. We recommend leaving the `omega2_onion` repo active since it contains the packages you'll need to interact with your Expansions, Docks, as well as other Onion-developed software goodies.

For the changes to take effect, run `opkg update`. You will then have access to packages hosted by the repos that are not commented out in your `distfeeds.conf` file. If this doesn't work, try rebooting your device and running `opkg update` again.

> Try visiting the repo links in a browser to see what the repos actually look like online. They're actually just online directories that hold the ipk files that make up software packages for OpenWRT. You'll also notice files named `Packages*`, these are the files that `opkg` uses to determine which software packages are available in this repo as well as to ensure package integrity.
