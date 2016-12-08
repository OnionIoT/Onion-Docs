---
title: Extending the Omega's Available Memory
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 1
---

## Extending the Omega's Available Memory {#extending-omega-memory}

While the Omega2 comes with a decent 64MB of RAM, and the Omega2+ with 128MB, you might find yourself in a situation where this is simply not enough! This tutorial will walk you through how you can use USB Storage and a Swap File to extend the amount of memory available to your Omega.

// this article will cover how to extend the Omega's available memory by using a swap file on USB storage

// heavily base it on the existing article, should be pretty complete



### What is a Swap File?

A Swap File is a special file on a disk drive or flash storage that is used by the operating system to store information not currently being used by the device's RAM. This allows the system and programs to use more memory than just by using the physically available RAM memory.

Swap Files, therefore, implement virtual memory. This is also known as paging and is used in every modern desktop and mobile operating system to manage and optimize the use of memory.

For more information, check out the [Wikipedia article on Paging](https://en.wikipedia.org/wiki/Paging).



### The Setup Procedure

Let's get to setting up our very own Swap File and extending the available memory on the Omega!

#### Step 1: Install Required Packages

First, we will install the `swap-utils` and `block-mount` packages that will allow us to create and use Swap Files:

```
opkg update
opkg install swap-utils
opkg install block-mount
```

#### Step 2: USB Storage

Plug in a USB drive and make sure it's mounted. For best results, you will need to setup automatic mounting. See the [USB Storage tutorial](#usb-storage) for details on the procedures.

For the purposes of this tutorial, let's assume the USB device was mounted to `/tmp/mounts/USB-A1`.


#### Step 3: Create Swap File on the USB storage

Now we need to create the file on the USB drive that will be used as the Swap file. We will be using the `dd` utility to help us create the file. The `dd` utility is meant to convert and copy files, it is very powerful so it can potentially be very destructive if used incorrectly, **stay on your toes when using `dd`**.

The specific `dd` command we will be running will look like:
```
dd if=/dev/zero of=/tmp/mounts/USB-A1/swap.page bs=1M count=256
```

This command will create a file on the USB drive that is 256MB with all of its bytes initialized to `0x00`. This is the file that will be used as the Swap File, so we will effectively be extending our RAM by 256MB.

Let's go through each part of the command:
* The `if` argument specifies the source of the data, in this case `/dev/zero` is a special system file that outputs as many `0x00` bytes as requested.
* The `of` argument tells `dd` where to create the new file. In our scenario, the USB drive was mounted at `/tmp/mounts/USB-A1` and we want to make a `swap.page` file on the top level of the drive.
* The `bs` and `count` arguments will specify the size of the file that will be created:
  * The `bs` argument actually stands for Block Size, with a Block being the number of bytes that are read, written, or converted at one time. We are setting our Block size to 1 Million Bytes or 1 Megabyte (MB)
  * The `count` argument defines how many blocks are to be created. So we are creating 256 blocks that are 1MB each, therefore the file will be 256MB in total


#### Step 4: Setup the Swap File

Now that the Swap File has been created, we need to tell Linux to setup this file as a swap area:
```
mkswap /tmp/mounts/USB-A1/swap.page
```

Running the `free` command will show that nothing has changed yet:
```
root@Omega-1302:~# free
             total         used         free       shared      buffers
Mem:         61152        42528        18624           96        11648
-/+ buffers:              30880        30272
Swap:            0            0            0
```


#### Step 5: Activate the Swap File

We're finally ready to activate the Swap File and actually expand our available memory:
```
swapon /tmp/mounts/USB-A1/swap.page
```

Now, when `free` is run again, we will see that the Swap row is populated:
```
root@Omega-1302:~# free
             total         used         free       shared      buffers
Mem:         61152        42644        18508           96        11648
-/+ buffers:              30996        30156
Swap:       262140            0       262140
```

The units of the numbers displayed by the `free` command are kilobytes. The total Swap size is 262140 kilobytes which is equivalent to 256MB, so we can confirm that the Swap File is active and being used as memory.

**Note:** When the Omega is rebooted, the USB Swap Page will no longer be used. Step 5 will have to be repeated after every boot unless some automatic method for activating the Swap Page is created...

### Going Further

It's a little problematic that the Swap File needs to be activated manually after every boot, so let's automate this!

#### Automatically Mount the USB using Block + Fstab

In order to automatically activate the Swap File, we will need to set up automounting on your USB using a different method than the default tool on the Omega2.

Let's take a look at our `fstab` configuration. This is the configuration file that holds all of the storage device info on the system. It can be found at `/etc/config/fstab`, meaning we can access it using the following command: `uci show fstab`. This will show various configuration info like below:

```
fstab.@global[0]=global
fstab.@global[0].anon_swap='0'
fstab.@global[0].anon_mount='0'
fstab.@global[0].auto_swap='1'
fstab.@global[0].auto_mount='1'
fstab.@global[0].delay_root='5'
fstab.@global[0].check_fs='0'
```

Make sure your swap USB drive is plugged into the Omega. We will tell the Omega to detect the information for the drive and save it in our `fstab` configuration like so:
```
block detect > /etc/config/fstab
```

Now the Omega has an fstab [UCI] entry for this specific USB drive. Let's update the UCI entry so that it will automatically be mounted.

First, let's see the current configuration by running `uci show fstab`, it will output something like the following:
```
fstab.@global[0]=global
fstab.@global[0].anon_swap='0'
fstab.@global[0].anon_mount='0'
fstab.@global[0].auto_swap='1'
fstab.@global[0].auto_mount='1'
fstab.@global[0].delay_root='5'
fstab.@global[0].check_fs='0'
fstab.@mount[0]=mount
fstab.@mount[0].target='/mnt/sda1'
fstab.@mount[0].uuid='1806-3FEB'	// this is the unique identifier of the USB drive
fstab.@mount[0].enabled='0'
```

Now, lets enable the `mount[0]` device:
```
uci set fstab.@mount[0].enabled='1'
uci commit fstab
```

**Make sure fstab is Enabled**

Just to be safe, let's enable `fstab` to run at boot:
```
/etc/init.d/fstab enable
block mount
```

**Restarting fstab**

Any time the `fstab` configuration is changed, the following command can be used to restart the process so the changes will take effect:
```
block umount;block mount
```

There's a file called `/etc/rc.local` where you can put terminal commands that will be run automatically after every boot. This is perfect for what we're trying to do.

However, 

Add the following to your `/etc/rc.local` file:
```
### activate the swap file on an external USB drive
SWAP_FILE="/tmp/mounts/USB-A1/swap.page"
if [ -e "$SWAP_FILE" ]; then
        swapon /tmp/mounts/USB-A1/swap.page
fi
```

**Make sure this code is placed above the `exit 0` line that already exists in the file!**

This will first check that the Swap File exists, and will then activate the Swap File. Note that this depends on the USB drive being automatically mounted during boot, see the [USB Storage tutorial](#usb-storage) for details on how to accomplish automatic mounting.

<!-- Above paragraph no longer relevant -->

Try adding this code, reboot your Omega (with the USB drive still plugged in), and running `free` to confirm the Swap File is indeed being used.



### Summary

Using a Swap File allows us to use other types of storage (USB, flash) to extend the amount of RAM available in our system. All modern desktop and mobile operating systems implement swap files in one way or another since storage is generally much cheaper than memory. This isn't exactly equivalent to adding more RAM since memory is much, much faster than storage, but for situations where memory usage becomes an issue, this method is incredibly useful.

Happy hacking!
