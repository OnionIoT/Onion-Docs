<!--
TODO: remove all TODOs when you implement them
-->

## Using a MicroSD Card {#using-a-microsd-card}
<!--
// introdution to the topic and article,
// give a small background on SD cards, how they're flash memory etc
// give an overview of what the article will cover:
//  - correctly inserting and removing the microSD card
//  - interacting with data on the microSD card
-->

An SD card is a flash memory device that uses quantum tunneling effects to store information. Sort of like locking a piece of iron a secure glass box, and using a magnet to move it around to store information. The smallest version of the SD card available right now is the MicroSD format.

![MicroSD Card](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/microsdcard.png)

The Omega2+ comes with a MicroSD card slot, enabling you to greatly expand the storage capacity of the Omega without much added cost. The MicroSD card slot on the Omega2+ can be found at the bottom of the board inbetween the pins.

![MicroSD Card Slot Location](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/omega2p-microsd-slot.jpg)

We'll cover how to insert the SD card, how storage devices work in Linux, how to work with files on the card, and how to safely remove it without damaging your data.

**Note:** The Omega2+ supports MicroSD card on firmware builds **b143** and higher. Always remember to upgrade to the latest firmware when working with SD cards!

### Inserting a MicroSD Card
<!--
// this section should include a step by step guide on how to correctly plug in a microSD card into a Omega2+ that's on a Dock
// should include photos of each major step
// add a note saying that the microSD card will be automatically mounted, point to the Accessing the MicroSD card section below
-->

The MicroSD slot is spring loaded, and it will remain in place once it's locked in. to properly seat it,

![MicroSD card sitting the slot](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/microsd-seated.jpg)

To insert the MicroSD card, you should firmly push the SD card into the slot until you hear and feel a click.

![Push it in firmly](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/microsd-pushin.jpg)

This is what it should look like once seated properly -

![MicroSD properly locked in slot](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/microsd-lockedin.jpg)

After you insert the card, you should make sure it's mounted in the fileystem and accessible.

>Occasionally, the spring mechaism may be already preloaded and your card will pop right back out if you let go. Simply pushed it back in until the click, and you should be all set.

If you're running the latest firmware, the Omega should have automatically mounted the MicroSD card already.

### Storage Devices and Linux
<!--
// explanation of how on linux, storage devices need to first be mounted in order to be used
// (can rip this part off from the USB Storage article, it might be a good idea to isolate that part of the article into its own markdown file and include it here and the usb storage article)
-->

On a Linux device, a storage device needs to be mounted in order to access the data. Mounting a device maps its storage space to a directory on your device so that you may access it.

The Omega2 comes ready with an auto-mounting tool that will take care of that process for you!

The default mount location is `/tmp/mounts/`.


### Accessing the MicroSD Card
<!--
// see the usb storage article for reference:
// should outline:
//  - where the storage device gets mounted
//  - accessing the files
-->
Under normal circumstances, the SD card and any USB device you plugged in should be the only things that exist in the `/tmp/mounts` directory. Thus you can check there with `ls /tmp/mounts/` to determine the name the Omega assigned the card. Running `ls /tmp/mounts` gave us `SD-P1` as the name of our MicroSD card.

Once mounted, it acts as a regular directory or folder in all ways, and any file that you stored in the card originally should be there! For us, it looked something like this:

```
root@Omega-1234:~# cd /tmp/mounts
root@Omega-1234:/tmp/mounts# ls
SD-P1
```

>The P1 in the name means partition #1 of the MicroSD card, if you have partitioned your MicroSD, they should show up as `SD-P1`, `SD-P2`, and so on.

If you'd like to change where the MicroSD card is mounted on the filesystem, we've written a [guide](#usb-storage-changing-default-mount-point) covering how to do so for both MicroSD cards and USB drives.

### Safely Removing a MicroSD Card

To safely remove your SD card you should always unmount it first. This will eliminiate the possibility of the data being accessed while you physically remove it, which can corrupt the SD card's data and filesystem.

The `umount` command is used to unmount the storage.

```
umount <mount point>
```

From the above example:

```
umount /tmp/mounts/SD-P1
```

>Note: **not** `unmount`! We've made this error more than once when we started out.

Now that the card is no longer being used by the Omega, we can physically remove it without risking corruption.

The MicroSD card can now be safely removed.

![Push it in firmly until you hear a click](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/microsd-lockedin.jpg)

Just push until it clicks.

![MicroSD properly locked in slot](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/microsd-pushin.jpg)

Now you can pull it out of the slot - careful not to lose it!

![Pull the MicroSD out](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/microsd-pullout.jpg)
