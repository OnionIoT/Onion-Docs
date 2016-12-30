---
title: Using opkg
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 1
---

## What is OPKG? {#software-using-opkg}

Not everything available for the Omega is installed right away. Some people may never need certain utilities and so we configure the Omega with packages you will likely use, and let you further tailor your Omega to suit your needs.

This is accomplished with OPKG, the package manager for the Omega's Operating System. It is used primarily to download and install packages. If you're familiar with Linux or other Linux distributions then a good comparison for OPKG is the `apt-get` utility.

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

As of firmware version 0.1.7, `opkg` is configured to grab packages from Onion's package repositories. As a result, you can now successfully install kernel modules, however, we host a smaller selection of packages than the official LEDE repositories.

#### How `opkg` is Configured

The path to the package repos that `opkg` checks during the `opkg update` command can be found at `/etc/opkg/distfeeds.conf`.

#### Installing Kernel Modules

While the Omega comes with many handy kernel modules already installed, your project or idea might require some additional modules. Since all of the packages in the Onion repos are compiled by Onion, your Omega running Onion firmware will have no problems installing kernel modules using `opkg`.

> Note that your Omega cannot install kernel modules from the default LEDE repos. `opkg` only allows installation of kernel modules compiled by the creators of the firmware. This is to ensure that all installed kernel modules are the same version as the device's kernel. It would be pretty disastrous to install a module that expects a different version of the overall kernel.

For best results, make sure you're on the `latest` Omega firmware. Take a look at our guide on [updating the Omega](#updating-the-omega-latest-version) for steps on how to install the `latest` firmware.


#### You don't Have a Package I Want/Need!

As mentioned before, we host a smaller selection of packages than the official LEDE package repos. However, if you need specific packages, we would be happy to add them to our repo.

Let us know which packages you would like to see added by posting on the [Onion Community](https://community.onion.io/) or creating a [ticket on our Helpdesk](https://onion.freshdesk.com/). We'll do our best to update the repo in a timely manner!


#### How to Switch Back to the Official LEDE Package Repos

If you really dislike using our repos, it's really easy to switch back to using the official LEDE repos. You can also experiment with combining the use of Onion and LEDE repos. This can all be accomplished by editing the `/etc/opkg/distfeeds.conf` file that configures which repos are to be used.

By default, it will be configured to use the Onion respos and will look something like this:
```
#src/gz reboot_core http://downloads.lede-project.org/snapshots/targets/ramips/mt7688/packages
#src/gz reboot_base http://downloads.lede-project.org/snapshots/packages/mipsel_24kc/base
#src/gz reboot_onion http://repo.onion.io/omega2/packages
## src/gz reboot_luci http://downloads.lede-project.org/snapshots/packages/mipsel_24kc/luci
#src/gz reboot_packages http://downloads.lede-project.org/snapshots/packages/mipsel_24kc/packages
## src/gz reboot_routing http://downloads.lede-project.org/snapshots/packages/mipsel_24kc/routing
## src/gz reboot_telephony http://downloads.lede-project.org/snapshots/packages/mipsel_24kc/telephony
src/gz omega2_core http://repo.onion.io/omega2/packages/core
src/gz omega2_base http://repo.onion.io/omega2/packages/base
src/gz omega2_packages http://repo.onion.io/omega2/packages/packages
src/gz omega2_onion http://repo.onion.io/omega2/packages/onion
```

The commented out lines in the file are not active, so to go back to the official LEDE repos, just uncomment those lines, and comment out the Onion lines:
```
src/gz reboot_core http://downloads.lede-project.org/snapshots/targets/ramips/mt7688/packages
src/gz reboot_base http://downloads.lede-project.org/snapshots/packages/mipsel_24kc/base
#src/gz reboot_onion http://repo.onion.io/omega2/packages
## src/gz reboot_luci http://downloads.lede-project.org/snapshots/packages/mipsel_24kc/luci
src/gz reboot_packages http://downloads.lede-project.org/snapshots/packages/mipsel_24kc/packages
## src/gz reboot_routing http://downloads.lede-project.org/snapshots/packages/mipsel_24kc/routing
## src/gz reboot_telephony http://downloads.lede-project.org/snapshots/packages/mipsel_24kc/telephony
#src/gz omega2_core http://repo.onion.io/omega2/packages/core
#src/gz omega2_base http://repo.onion.io/omega2/packages/base
#src/gz omega2_packages http://repo.onion.io/omega2/packages/packages
src/gz omega2_onion http://repo.onion.io/omega2/packages/onion
```

We recommend leaving the `omega2_onion` repo active since it contains the packages you'll need to interact with your Expansions, Docks, as well as other Onion-developed software goodies.

For the changes to take effect, reboot your Omega and run `opkg update`. You will then have access to packages hosted by the repos that are not commented out.

> Try visiting the repo links in a browser to see what the repos actually look like online. They're actually just online directories that hold the ipk files that make up software packages for LEDE. You'll also notice files named `Packages*`, these are the files that `opkg` uses to determine which software packages are available in this repo as well as to ensure package integrity.
