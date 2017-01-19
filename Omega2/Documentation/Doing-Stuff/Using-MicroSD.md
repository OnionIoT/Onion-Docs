<!-- TODO: everywhere you use MicroSD card, use the same capitalization! 
TODO: remove all TODOs when you implement them -->

## Using a MicroSD Card {#using-a-microsd-card}
<!--
// introdution to the topic and article,
// give a small background on SD cards, how they're flash memory etc
// give an overview of what the article will cover:
//  - correctly inserting and removing the microSD card
//  - interacting with data on the microSD card
-->

An SD card is a flash memory device that uses quantum tunneling effects to store information. Sort of like locking a piece of iron a secure glass box, and using a magnet to move it around to storge information.
// TODO: fix typo above and add a photo of a microSD card

// TODO: add sentence, something along the lines of: 'The Omega2+ has a MicroSD card slot on the underside of the board, using a MicroSD card, you can greatly increase the amount of storage available to the Omega in a very cost effective manner.'


We'll quickly go over how storage devices work in Linux, how to insert and remove the microSD card from its slot, and how to work with files on the card.

*Note: MicroSD card 


### Inserting a MicroSD Card
<!-- // this section should include a step by step guide on how to correctly plug in a microSD card into a Omega2+ that's on a Dock

// should include photos of each major step

// add a note saying that the microSD card will be automatically mounted, point to the Accessing the MicroSD card section below
-->

The microSD slot is spring loaded. To insert the MicroSD card, you should firmly push the SD card into the slot until you hear and feel a click. After you insert the card, you should make sure it's mounted and accessible.

// TODO: include 3 photos:
// - microSD card inserted but not popped in
// - finger visible pushing the sd card down
// - showing how it should look when the sd card is properly inserted

>Occasionally, the spring mechaism may be already preloaded and your card will pop right back out if you let go. Simply pushed it back in until the click, and you should be all set.

// TODO: small seque-way into the next section: 'The Omega will automatically mount the MicroSD card as a storage volume'

### Storage Devices and Linux
<!--
// explanation of how on linux, storage devices need to first be mounted in order to be used
// (can rip this part off from the USB Storage article, it might be a good idea to isolate that part of the article into its own markdown file and include it here and the usb storage article)
-->

On a Linux device, a storage device needs to be mounted in order to access the data. Mounting a device maps it's storage space to a directory on your device so that you may access it.

The Omega2 comes ready with an auto-mounting tool that will take care of that process for you! The default mount location is `/tmp/mounts/`. 

// TODO: give a small run-down and example of where the SD card will be mounted




### Accessing the MicroSD Card
<!--
// see the usb storage article for reference:
// should outline:
//  - where the storage device gets mounted
//  - accessing the files 
-->
Under normal circumstances, the SD card and any USB device you plugged in should be the only things that exist in the `/tmp/mounts` directory. Thus you can check there with `ls /tmp/mounts/` to determine the name the Omega assigned the card. Running `ls /tmp/mounts` gave us `SD-P1` as the name of our microSD card.

Once mounted, it acts as a regular directory or folder in all ways, and any file that you stored in the card originally should be there!

For more options on changing how your microSD card is mounted, refer to the 'Changing the default mount point' section of the [USB Storage](#using-usb-storage} Article.

// TODO: for the above sentence, you should add a {#blah} tag to the section in the usb article and then link directly to that!


### Safely Removing a MicroSD Card

To safely remove your SD card you should always unmount it first. This will eliminiate the possibility of the data being accessed while you physically remove it, which can corrupt the SD card's data and filesystem.

The `umount` command is used to unmount the storage

```
umount <mount point>
```

From the above example:

```
umount /tmp/mounts/SD-P1
```

The microSD card can now be safely popped out - just push until it clicks and let go.

// TODO: include photos
// - fully inserted microsd card (can reuse from above)
// - finger pushing down on the card (can reuse from above)
// - pulling out the card
