## Factory Reset {#factory-reset}

Just in case some important system files or configurations get deleted or overwritten, the Omega can be restored to a factory state. Performing a Factory Restore on your Omega will revert all files to the default for the currently installed firmware, **all other files will be deleted**.

So a factory restore will not revert to the firmware that was actually installed at the factory, it will essentially create a clean slate on our Omega's currently installed firmware.

Make sure that you understand that a factory restore **is a destructive action** and that all **user files should be backed up** before performing a factory restore!



### Using a Command

To perform a factory restore on the command line, run the following commands:

```
firstboot -y
sync
reboot
```

These commands will:

* Revert the firmware to a clean slate
* Ensure all storage opeartions are complete
* [Reboot the Omega](#rebooting) for the changes to take effect

It will work the same no matter how you have connected to the Omega's command line, whether it was by [SSH](#connecting-to-the-omega-terminal-ssh), via [Serial](#connecting-to-the-omega-terminal-serial), or using the [Terminal App](#developing-using-the-console-terminal-app) on the Console.



### With the Reset button

When connected to a Dock with a Reset button, **pressing and holding the reset button for about 10 seconds** will trigger a factory reset and then automatically reboot you Omega.

This can only be done on Docks that have Reset Buttons:

* Expansion Dock
* Power Dock
* Mini Dock
* Arduino Dock 2


<!-- Illustrations that point out reset buttons on each of the docks -->
```{r child = './Component-Reset-Button-Photos.md'}
```

<!-- TODO: add this section -->
<!-- ### With the Console -->
