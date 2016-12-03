---
title: USB Storage
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 3
---

## Using USB Storage

<!-- Explanation of how to use USB storage: -->

The Omega2 can read and write to USB storage devices, such as USB keys, and USB external hard-drives. This tutorial will show you how to expand the storage on your Omega2 using an external USB storage device, and how to change some of the default configurations.

<!-- add an image of a usb key plugged into an omega -->

### USB Storage and Linux

<!-- Explanation of how a device needs to be mounted - make sure to highlight the Omega2 auto-mounts USB storage, point out the location -->
On a Linux device, a USB storage device needs to be mounted in order to be used. Mounting a device maps it's storage space to a directory on your device so that you may access it.

The Omega2 comes ready with an auto-mounting tool that will take care of that process for you! The default mount location is `/tmp/mounts/`.


### Using USB storage

<!-- explanation of how to access files -->
Steps to access USB storage:

<!-- TODO: photo of plugged in usb stick -->
1. Plug in the USB Storage
2. Navigate to the directory where your USB device is located.
	* The default is `/tmp/mounts/`
		* `cd /tmp/mounts/`
3. Check the directory for your USB storage device
	```
  ls
  ```
4.  Your device will usually be named `USB-A1`
	* `cd <device name>` to enter the storage space on your USB
	* In this example, this would be `cd USB-A1`
5.  Congratulations, you may now use your USB storage device for additional space on your Omega!


Now that your device is mounted, you can treat this directory just like you would any other one on your Omega. This means you can copy files to the Omega from the USB device, and vice versa. Not only that, you can even run code from your USB device on your Omega!

You can copy files from your Omega to the USB device using the `cp` command.

```
cp <FILE YOU WANT TO COPY> <DESTINATION>
```

Based on the example above, the command would look like the following if I was moving a file from my root directory to the USB device:

```
cp /root/example.txt /tmp/mounts/USB-A1/example.txt
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
umount /tmp/mounts/USB-A1
```

The USB device can now be safely unplugged.


### Changing the default mount point

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
