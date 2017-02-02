## Rebooting your Omega {#rebooting}

Like all computers, the Omega can be restarted by rebooting. You may want to restart your Omega to ensure new settings will take effect, to occasionally resolve strange issues, or even just for kicks. There are two ways to reboot your Omega: running a command or using a physical button on a Dock.

### Using a Command

Unsurprisingly, running the `reboot` command on the Omega's command line will cause your Omega to perform a reboot. It will work the same no matter how you have connected to the Omega's command line, whether it was by [SSH](#connecting-to-the-omega-terminal-ssh), via [Serial](#connecting-to-the-omega-terminal-serial), or using the [Terminal App](#developing-using-the-console-terminal-app) on the Console.


### With the Reset button

When connected to a Dock with a Reset button, a quick **press and release** of the button will trigger a reset on the Omega.

This can only be done on Docks that have Reset Buttons:

* Expansion Dock
* Power Dock
* Mini Dock
* Arduino Dock 2


<!-- Illustrations that point out reset buttons on each of the docks -->
```{r child = './Component-Reset-Button-Photos.md'}
```
