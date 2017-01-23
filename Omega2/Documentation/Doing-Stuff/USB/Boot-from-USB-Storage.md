---
title: Booting from USB Storage
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 2
---

## Booting from USB Storage {#boot-from-usb-storage}

<!-- // mention that, yes, flash storage on the Omega is limited, so it is possible to have the Omega boot from attached USB storage -->

The Omega comes with enough flash storage to get started and working on projects, but if you need more it's possible to extend the storage capacity using a USB drive!

This article will explain and outline the procedure for the **pivot-overlay** process.

<!-- // base this on the existing article:
//  notes on this: find the different between pivot-root and pivot-overlay and then discuss them with Lazar, we will likely only choose one to inlcude in the article -->

### pivot-overlay

pivot-overlay allows you to download, store, and install software and packages onto another device such as a USB drive. The drive can be as big or small as you need, so you'll (probably) never have to worry about running out of space again!

The technical explanation is that it mounts a USB storage device to the writable part of your filesystem, `/overlay`, which is merged with the read-only part of your filesystem, `/rom`, to generate the entire filesystem, `/`.

<!-- ### Boot Process

// include an illustration of how the omega currently works (boots from on-board flash)
// include an illustration of how it works when booting from USB storage -->

<!-- boot process shouldn't change for pivot-overlay only -->

### Requirements

You will need:

* A USB drive with however much memory you need
* A Dock with a USB host port
* Firmware >= 0.1.9 b149
* Onion Console installed (so you can confirm that the storage space has increased)

### Important Warnings

Updating or reflashing the firmware will undo this process.

* All user-created files will be deleted. (this is a normal part of updating firmware)
* The filesystem will return to residing only on the Omega's onboard flash storage.

<!-- // remember to include the important caveats:
//  - updating the firmware might affect this (test this out and see what the outcome is) -->
//  - when the usb storage is removed, the omega will boot from the onboard flash and all of the filesystem changes made on the usb storage device will not be transferred (test this as well to find out exactly what happens)

And as always, **make sure your Omega has the latest firmware.**

**Before you continue, make sure all of your user code and binaries on the Omega are backed up somewhere!**

### Format Your USB Drive to `ext4`

>If you already have an `ext4` USB drive prepped, you can continue with the next step.

**Formatting will erase *all data* on your USB drive. If you're reusing an old drive, make sure to back up your data before continuing!**

You will need a USB drive formatted in `ext4`. If you don't have one that's formatted, you can format it using the Omega. On your Omega, install the necessary tools by running the following commands:

```
opkg update
opkg install kmod-usb-storage-extras e2fsprogs kmod-fs-ext4
opkg install block-mount
```

Connect your USB drive to the USB host port on the Dock. By default, it will appear in `/dev` as `sda1`. In this case, run the following command:

```
mkfs.ext4 /dev/sda1
```

Replace `sda1` with the name of your drive if it appears differently.

### Mounting the USB Storage Device

If you did not need to use the Omega to format your USB drive, make sure the drive is now connected to the Omega.

Run the following commands (assuming the drive appears as `sda1`):

```
mkdir /mnt/sda1
mount /dev/sda1 /mnt/sda1
```

### Duplicating the `/overlay` Directory

Move the `/overlay` directory into the USB storage device that we just mounted by running the following command:

```
mount /dev/sda1 /mnt ; tar -C /overlay -cvf - . | tar -C /mnt -xf - ; umount /mnt
```

### Automatically Mount `/overlay` on Startup

Generate the `fstab` template using `block-mount`:

```
block detect > /etc/config/fstab
```

Then edit the `/etc/config/fstab` file to enable auto-mounting the `/overlay` directory:

```
vi /etc/config/fstab
```

Look for the line

```
option  target  '/mnt/sda1'
```

and change it to:

```
option target '/overlay'
```

Then, look for the line: 

```
option  enabled '0'
```

and change it to 

```
option  enabled '1'
```

Save the file and restart the Omega:

```
reboot
```

And voilà! Your Omega should automatically mount the `/overlay` directory. From this point on, all changes to your filesystem will be made on your USB storage device. 

### Booting Without the USB Drive Connected

**Caution:** If you power on the Omega without the USB drive connected, the following will be unavailable as they would have only been stored on the drive:

* Certain firmware settings
* User-installed packages (eg. Python)
