## Factory Reset {#factory-reset}

Just in case some important system files or configurations get deleted or overwritten, the Omega can be restored to a factory state. Performing a Factory Restore on your Omega will revert all files to the default for the currently installed firmware, **all other files will be deleted**.

So a factory restore will not revert to the firmware that was actually installed at the factory, it will essentially create a clean slate on our Omega's currently installed firmware.

Make sure that you understand that a factory restore **is a destructive action** and that all **user files should be backed up** before performing a factory restore!


### What does a Factory Reset Actually Do?

The Omega's OpenWRT Linux uses OverlayFS as the filesystem. This approach includes a *overlaying* a writable filesystem (for configuration and custom files) on top of a read-only filesystem that holds the system files.

> See the [OpenWRT docs](https://openwrt.org/docs/techref/filesystems) to learn more about OverlayFS.

On the Omega, the internal storage is split into the `rootfs` (read-only) and `rootfs_data` (r/w) partitions, which are merged into a single writable overlay partition at boot:

| Partition     | Mount point | Compression      | Writable |
|---------------|-------------|------------------|----------|
| `rootfs`      | `/rom`      | Yes              | No       |
| `rootfs_data` | `/overlay`  | No               | Yes      |
| `overlay`     | `/`         | Unmodified files | Yes      |

#### How does Factory Reset Play into this?

The `rootfs` partition is only modified when the firmware is updated. For example, by running `oupgrade` or using `sysupgrade` to install a new firmware image. 

The `rootfs_data` partition stores all of your changes *on top* of the installed firmware. This includes configuration changes, any files that were created, and packages that were installed using `opkg` (that were not included in the firmware).

**A factory reset will delete everything in the `rootfs_data` partition.** When your device reboots, the filesystem will be based solely on what's in the `rootfs` partition.  


### Using a Command

To perform a factory restore on the command line, run the following commands:

```
firstboot -y
sync
reboot
```

These commands will:

* Revert the firmware to a clean slate
* Ensure all storage operations are complete
* [Reboot the Omega](#rebooting) for the changes to take effect

It will work the same no matter how you have connected to the Omega's command line, whether it was by [SSH](#connecting-to-the-omega-terminal-ssh), via [Serial](#connecting-to-the-omega-terminal-serial), or using the [Terminal App](#developing-using-the-console-terminal-app) on the Console.



### With the Reset button

With an Omega2/Omega2+ connected to a Dock with a Reset button, **pressing and holding the reset button for about 10 seconds** will trigger a factory reset and then automatically reboot your Omega. 

This can only be done on Docks that have Reset Buttons:

* Expansion Dock
* Power Dock
* Mini Dock
* Arduino Dock 2


<!-- Illustrations that point out reset buttons on each of the docks -->
```{r child = './Component-Reset-Button-Photos.md'}
```

On an Omega2S/Omega2S+, the same can be accomplished with GPIO38, the FW RST pin. GPIO38 acts as an **Active-High** reset button. If it is held high for 10 seconds and released, a factory reset will be triggered and the device will automatically reboot.

#### How does this work?

The behaviour of the FW RST (GPIO38) is controlled by the `/etc/rc.button/reset` file. This file determines what actions the device will take based on how long the button is pressed/the pin is held high. 

Make changes to the `/etc/rc.button/reset` file if you are looking to change the behaviour of this pin.

### A note about Factory Resets and RSA Key Warnings

After a factory reset, your Omega's SSH signature will be different. When you try to connect to it via SSH, your computer will recognize the key associated with the remote address is different than before and warn you. In general, it is a good idea to heed this warning, but if you've just factory reset your Omega, then this is to be expected.

SAMPLE WARNING:

```
ssh root@192.168.3.1
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the RSA key sent by the remote host is
SHA256:bhBERYdcA6wsT6Uc2np+Lt+5I9MU2ekggE+1CLTrQpg.
Please contact your system administrator.
Add correct host key in /Users/Onion/.ssh/known_hosts to get rid of this message.
Offending RSA key in /Users/Onion/.ssh/known_hosts:231
RSA host key for 192.168.3.1 has changed and you have requested strict checking.
Host key verification failed.
```
But this is not a big issue. The fix is, simply open the `known_hosts` file and delete the previous entry. The warning message will specify the line number.
