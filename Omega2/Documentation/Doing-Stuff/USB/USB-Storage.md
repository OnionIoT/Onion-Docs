---
title: USB Storage
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 3
---

## Using USB Storage {#usb-storage}

<!-- Explanation of how to use USB storage: -->

The Omega2 can read and write to USB storage devices, such as USB keys, and USB external hard-drives. This tutorial will show you how to expand the storage on your Omega2 using an external USB storage device, and how to change some of the default configurations.

![usb plugged in](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/usb-plugged-in.JPG)

### USB Storage and Linux

<!-- Explanation of how a device needs to be mounted - make sure to highlight the Omega2 auto-mounts USB storage, point out the location -->
On a Linux device, a USB storage device needs to be mounted in order to be used. Mounting a device maps it's storage space to a directory on your device so that you may access it.

The Omega2 comes ready with an auto-mounting tool that will take care of that process for you! The default mount location is `/mnt/`.

> On firmware older than `v0.3.0`, the default mount location was `/tmp/mounts/` and the `mountd` package controlled automatic mounting.
> Firmwares `v0.3.0` and up use the `block-mount` package. 


### Using USB storage

<!-- explanation of how to access files -->
Steps to access USB storage:

![usb plugged in](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/usb-plugged-in.JPG)

1. Plug in the USB Storage
2. Navigate to the directory where your USB device is located.
	* The default is `/mnt/`
		* `cd /mnt/`
3. Check the directory for your USB storage device
  ```
  ls
  ```
4.  Your device will usually be named `sda1`
	* `cd <device name>` to enter the storage space on your USB
	* In this example, this would be `cd sda1`
5.  Congratulations, you can now use your USB storage device for additional space on your Omega!


Now that your device is mounted, you can treat this directory just like you would any other one on your Omega. This means you can copy files to the Omega from the USB device, and vice versa. Not only that, you can even run code from your USB device on your Omega!

You can copy files from your Omega to the USB device using the `cp` command.

```
cp <FILE YOU WANT TO COPY> <DESTINATION>
```

Based on the example above, the command would look like the following if I was moving a file from my root directory to the USB device:

```
cp /root/example.txt /mnt/sda1/example.txt
```


### Unmounting

<!-- draw a parallel to safely disconnecting in Windows -->

Once you are done with your USB storage device, make sure you unmount your device before removing it to avoid corrupting your data.

The `umount` command is used to unmount the storage

```
umount <mount point>
```

From the above example:

```
umount /mnt/sda1
```

The USB device can now be safely unplugged.


### Changing Mounting Options {#usb-storage-changing-mounting-options}

The configuration for `block-mount` can be found in `/etc/config/fstab`. By default, the configuration is as follows:

```
config global
	option anon_swap '0'
	option auto_swap '1'
	option auto_mount '1'
	option delay_root '5'
	option check_fs '0'
	option anon_mount '1'
```

The `auto_mount` option controls automatic mounting of external storage. And the `anon_mount` option controls whether anonymous storage devices - meaning haven't been previously used with the Omega - should be mounted. 

The configuration can be changed by directly editing the `/etc/config/fstab` config file, or [using UCI](#intro-to-uci).

### Changing the default mount point {#usb-storage-changing-default-mount-point}

> This is only valid for firmwares older than `v0.3.0` that used `mountd` instead of `block-mount`.

In order to change the default mount point of your USB storage devices you'll need to change a configuration file.

1. Change directories to `/etc/config/`
```
cd /etc/config
```

2. Edit the `mountd` file with `vi`
```
vi mountd
```

You'll see the following:
```
config mountd mountd
        option  timeout         60
        option  path            /tmp/mounts/
```

3. Change `/tmp/mounts/` to the desired destination

```
config mountd mountd
        option  timeout         60
        option  path            <DESIRED MOUNT DIRECTORY>
```

4. Save the file by hitting `ESC` and typing `:wq`

5. Restart the auto-mount service to apply the new settings
```
/etc/init.d/mountd restart
```

Your device should now automatically mount to your newly specified directory upon plugging in.
