---
title: Booting from USB Storage
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 2
---

## Booting from External Storage {#boot-from-external-storage}

<!-- // mention that, yes, flash storage on the Omega is limited, so it is possible to have the Omega boot from attached USB storage -->

The Omega comes with enough flash storage to get started and working on projects, but if you need more it's possible to extend the storage capacity using a USB drive or MicroSD card!

This article will explain and outline the procedure for the **pivot-overlay** process. Basically we move the writeable portion of the Omega's firmware to an external storage device such as a MicroSD card or USB drive. Then we expand the Omega's filesystem to use the entire storage device.

We'll cover how to:

* Format a USB drive or MicroSD card using the Omega
* Mount the external storage device in the Omega's filesystem
* Move the writeable portion of the filesystem to the storage device
* Set it up to mount the filesystem from the storage device on boot

### Warnings

#### Filesystem

This is a process that modifies how the Omega stores its files, so if you have any files or programs you created on the Omega, make sure you **back them up** before proceeding!

#### Firmware Updates

Updating or reflashing the firmware will **undo** the pivot-overlay process:

* The filesystem will be reverted to a fresh state and all user-created files will be deleted.
* The filesystem will return to residing only on the Omega's onboard flash storage.

<!-- TODO: is that a normal part of the firmware update in the second bullet??? not quite sure what you mean there 

Gabe: as in their files will all be erased/reset, AND the Omega will not use the external device's storage space, they'll be back to the flash only -->

<!-- TODO:
- add a few more plain-english sentences here of what pivot-overlay will help us accomplish:
    - move the writeable portion of the firmware to the usb storage
    - Expands the Omega's filesystem to the entire external storage device
- give a small outline that this article will be covering:
    - the procedure on how to set it all up
    - provides warnings and troubleshooting for working with this type of system -->

#### Booting Without the Storage Device Connected

**Caution:** If you power on the Omega without the storage device connected, the following will be unavailable or reset to default as they would have only been stored on the device:

* User-created files
* User-installed packages (eg. Python, Git)
* Software settings stored outside of `/etc`

The filesystem will revert to a "fresh" state with only the default files and folders available. However, all of the above items will be accessible again once you reboot the Omega with the storage device connected!

<!-- // remember to include the important caveats:
//  - updating the firmware might affect this (test this out and see what the outcome is) -->
<!-- //  - when the usb storage is removed, the omega will boot from the onboard flash and all of the filesystem changes made on the usb storage device will not be transferred (test this as well to find out exactly what happens) -->

### The pivot-overlay Procedure

The pivot-overlay procedure allows you to download, store, and install software and packages onto another storage device like an SD card or USB drive. The storage can be as big or small as you need, so you'll (probably) never have to worry about running out of space again!

<!-- TODO: the single sentence below is trying to do too much at once!
update the paragraph below to:
 - describe how the Omega's filesystem works:
    - /rom holds the read-only firmware, /overlay are your changes that you've made to the base firmware, when the omega boots, it combines the two.
 - then describe that what pivot overlay does is that it moves the /overlay to the usb storage, allowing for hella additional space
  -->


The technical explanation is that it mounts a storage device to the writable part of your filesystem, `/overlay`, which is merged with the read-only part of your filesystem, `/rom`, to generate the entire filesystem, `/`.

<!-- ### Boot Process

// include an illustration of how the omega currently works (boots from on-board flash)
// include an illustration of how it works when booting from USB storage -->

<!-- boot process shouldn't change for pivot-overlay only -->

### Requirements

You will need:

* A USB drive or MicroSD card with however much memory you need
    * Only the Omega2+ can use MicroSD cards. Read our [MicroSD card guide](#using-a-microsd-card) for full details.
* A Dock with a USB host port if using a USB drive
* Firmware >= 0.1.9 b149

Before you begin, you can see for yourself how much space is being used on your filesystem via the `df` command. Run this in your Omega's terminal:

```
df -h
```

On a freshly-flashed Omega2, you should get something like this:

```
Filesystem                Size      Used Available Use% Mounted on
/dev/root                 5.5M      5.5M         0 100% /rom
tmpfs                    29.7M    192.0K     29.5M   1% /tmp
/dev/mtdblock6            9.1M      2.3M      6.8M  26% /overlay
overlayfs:/overlay        9.1M      2.3M      6.8M  26% /
tmpfs                   512.0K         0    512.0K   0% /dev
```

Here we have about 14.6 MB of space total on the Omega's flash, which is the sum of:

* `/overlay` - the `overlayfs:/overlay` entry
* `/rom` - the `/dev/root` entry

Now let's get started on preparing the external storage device.

### Format Your Storage Device to `ext4`

For pivot-overlay to work properly, you will need a storage device formatted to the `ext4` filesystem.

>If you already have an `ext4` formatted storage device , you can skip this part and continue to the next step: [Mounting the External Storage Device](#boot-from-external-storage-mounting-the-external-storage-device).

If you don't have one that's formatted, you can format it using the Omega.

**Warning: Formatting will erase *all data* on your USB drive. If you're reusing an old drive, make sure to back up your data before continuing!**

#### Installing the Tools

On your Omega, install  a few filesystem tools by running the following commands:

```
opkg update
opkg install kmod-usb-storage-extras e2fsprogs kmod-fs-ext4
```

#### Connecting External Storage Device

Insert or connect your storage device to the Omega and it will be automounted for file input/output. This blocks us from formatting it, so we'll need to unmount it first. 

By default, devices with a single partition are mounted to the following locations:

* USB: `/tmp/mounts/USB-A1`
* MicroSD: `/tmp/mounts/SD-P1`

Devices with multiple partitions may have multiple entries such as `USB-A2`, `SD-P3`, and so on. Choose the name of the partition that you want to use and continue below.

Unmount the target device by running the following command, replacing `<mount path>` with one of the paths above:

```
umount <mount path>
```

The Omega should now be ready to format the device.

#### Formatting the Device

Now we need to find the name under which our device is listed in `/dev`. By default, devices with a single partition are listed as follows:

* USB: `sda1`
* MicroSD: `mmcblk0p1`

Devices with multiple partitions may have multiple entries such as `sda2`, `mmcblk0p3`, and so on. Choose the name of the partition that you want to use and continue below.

Run the following command and fill in your device's name corresponding to one of the examples above:

```
mkfs.ext4 /dev/<device name>
```

It may warn you that the device contains a file system. Enter `y` to proceed.

For a USB drive, the process should look something like this:

```
root@Omega-7ADD:/tmp/mounts# mkfs.ext4 /dev/sda1
mke2fs 1.43.3 (04-Sep-2016)
/dev/sda1 contains a vfat file system
Proceed anyway? (y,n) y
Creating filesystem with 3784448 4k blocks and 946560 inodes
Filesystem UUID: f5ca350a-d8e2-4334-8aa2-ee17d623c444
Superblock backups stored on blocks:
        32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208

Allocating group tables: done
Writing inode tables: done
Creating journal (16384 blocks): done
Writing superblocks and filesystem accounting information: done
```

### Mounting the External Storage Device {#boot-from-external-storage-mounting-the-external-storage-device}

<!-- TODO: throw in a photo of the Omega&Dock with a USB drive plugged in and the Omega2+ with an SD card inserted -->

If you did not need to use the Omega to format your storage device, make sure the device is now connected to the Omega.

Run the following commands and fill in `<device name>` with your device's name (eg. `sda1`).

```
mkdir /mnt/<device name>
mount /dev/<device name> /mnt/<device name>
```

### Duplicating the `/overlay` Directory

Move the `/overlay` directory into the storage device that we just mounted by running the following command:

```
mount /dev/<device name> /mnt ; tar -C /overlay -cvf - . | tar -C /mnt -xf - ; umount /mnt
```

### Automatically Mount `/overlay` on Startup

First install `block-mount`:

```
opkg update
opkg install block-mount
```

Now generate the device's `fstab` entry using `block-mount`:

```
block detect > /etc/config/fstab
```

Then edit the `/etc/config/fstab` file to enable auto-mounting the `/overlay` directory:

```
vi /etc/config/fstab
```

Look for the line

```
option  target  '/mnt/<device name>'
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

<!-- TODO: make this last part its own section, we really want to highlight what they've accomplished! -->

And voilà! Your Omega should automatically mount the `/overlay` directory. From this point on, all changes to your filesystem will be made on your USB storage device. This is what it should look like with a 16 GB USB drive:

![pivot-overlay-omega2-filesystem](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/pivot-overlay-02.jpg "pivot-overlay Omega2 Filesystem")


<!-- TODO: add a blurb about the `df -h` command and show a screencap of the new space! -->
