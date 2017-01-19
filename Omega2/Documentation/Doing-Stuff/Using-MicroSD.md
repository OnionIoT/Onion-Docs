<!-- TODO: JAMES: please complete this article -->
<!-- Refer to the Using USB storage article for reference, this article should be similar -->

## Using a MicroSD Card {#using-a-microsd-card}
<!--
// introdution to the topic and article,
// give a small background on SD cards, how they're flash memory etc
// give an overview of what the article will cover:
//  - correctly inserting and removing the microSD card
//  - interacting with data on the microSD card
-->

An SD card is a flash memory device that uses quantum tunneling effects to store information. Sort of like locking a piece of iron a secure glass box, and using a magnet to move it around to storge information.

We'll quickly go over how storage devices work in Linux, how to insert and remove the microSD card from its slot, and how to work with files on the card.

The MicroSD card slot is available on the Omega2+, and can be found at the bottom of the board inbetween the pins. 

### Inserting a MicroSD Card
<!-- // this section should include a step by step guide on how to correctly plug in a microSD card into a Omega2+ that's on a Dock

// should include photos of each major step

// add a note saying that the microSD card will be automatically mounted, point to the Accessing the MicroSD card section below
-->

The microSD slot is spring loaded. To mount, you should firmly push the SD card into the slot until you hear and feel a click. After you insert the card, you should make sure it's mounted and accessible.

>Occasionally, the spring mechaism may be already preloaded and your card will pop right back out if you let go. Simply pushed it back in until the click, and you should be all set.



### Storage Devices and Linux
<!--
// explanation of how on linux, storage devices need to first be mounted in order to be used
// (can rip this part off from the USB Storage article, it might be a good idea to isolate that part of the article into its own markdown file and include it here and the usb storage article)
-->

On a Linux device, a USB storage device needs to be mounted in order to be used. Mounting a device maps it's storage space to a directory on your device so that you may access it.

The Omega2 comes ready with an auto-mounting tool that will take care of that process for you! The default mount location is `/tmp/mounts/`. For automounting of microSD cards, the firmware version needs to be at least `0.1.8 b143`.



### Safely Removing a MicroSD Card

// a mirror of the previous section: step by step guide on how to correctly remove a microSD card

// should include photos of each major step

// one of the steps must be unmounting

To safely remove your SD card you should always unmount it first. This will eliminiate the possibility of it being accessed while you physically remove it, which can corrupt your data.

The `umount` command is used to unmount the storage

```
umount <mount point>
```

From the above example:

```
umount /tmp/mounts/SD-P1
```

The microSD card can now be safely popped out - just push until it clicks and let go.



### Accessing the MicroSD Card
<!--
// see the usb storage article for reference:
// should outline:
//  - where the storage device gets mounted
//  - accessing the files 
-->
Under normal circumstances, the SD card and any USB device you plugged in should be the only things that exist in the `/tmp/mounts` directory. Thus you can check there with `ls /tmp/mounts/` to determine the name the Omega assigned the card. Running `ls /tmp/mounts` gave us `SD-P1` as the name of our microSD card.

Once mounted, it acts as a regular directory or folder in all ways, and any file that you stored in the card originally should be there!

For more options on changing how your microSD card is mounted, refer to the `Changing the default mount point' section of the [USB Storage](#using-usb-storage} Article.
