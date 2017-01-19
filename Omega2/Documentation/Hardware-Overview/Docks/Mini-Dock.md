---
title: Mini Dock
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 3
---



## Mini Dock {#mini-dock}

<!-- [//]: # (Brief overview on the expansion dock and what it's used for (usb connection, power omega). Highlight it's size and how it's useful) -->
<!-- [//]: # (for Omega-only projects or USB-based projects.) -->

The Mini Dock functions very similarly to the Expansion Dock. It supplies your Omega with power and allows you to communicate serially via a Micro-USB port. It also has a USB type A connector for you to use. All of this with a fraction of the size of an Expansion Dock.

The Mini Dock is same size as the Omega. It does not have the Expansion Header of some of the other Docks, but this makes it perfect for Omega-only or USB-based projects.

### The Hardware

<!-- [//]: # (Picture of mini dock with important bits highlighted like usb port, how to plug in the Omega, power switch (which direction is ON?).) -->
<!-- [//]: # (Maybe in depth discussion of various pieces, like USB to serial chip. People like that.) -->
<!-- [//]: # (Refer to current Power Dock Expansion doc for more info) -->

![mini dock alone](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/mini-dock-alone.JPG)


The Mini Dock is tiny. It is approximately 4.3cm (1.7in) long, and 2.7cm (1.07in) wide.

The Mini Dock is powered by the Micro-USB port that supplies 5V to the Dock. This voltage is stepped down to the required 3.3V required to power the Omega, and also provides 5V to the USB Host port

![illustration](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/mini-dock-illustration.png)


The Mini Dock allows for easy communication via the USB-to-Serial chip located in the center of the board.

The reset button, located next to the USB Connector, can be used to quickly reboot your Omega, or you can hold it down for a factory reset if your Omega is ever in a bad state.

### Connecting an Omega

<!-- [//]: # (picture guide on how to properly plug in an Omega) -->

To connect an Omega to the Mini Dock, line up the Omega's edges with that of the Mini Dock's as demonstrated below:

![mini dock plugged in](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/mini-dock-top-plugged-in.JPG)

Make sure your Omega is pushed all the way down as demonstrated in the picture below:


![mini dock side view](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/mini-dock-side-view.JPG)

You may need to line up the pins with the holes before pressing the Omega into the Dock.


<!-- #### The Mini Dock at a Glance -->

<!-- [//]: # (illustration with all of the key parts labelled - see https://wiki.onion.io/Tutorials/Expansions/Using-the-Power-Dock#the-hardware_the-power-dock-at-a-glance for an example) -->


<!-- Micro USB Port -->
```{r child = '../shared/Hardware-Overview-Component-1-Micro-USB-Port.md'}
```

<!-- USB-to-Serial -->
```{r child = '../shared/Hardware-Overview-Component-2-USB-to-Serial.md'}
```

<!-- USB-to-Serial -->
```{r child = '../shared/Hardware-Overview-Component-4-Power-Switch.md'}
```

<!-- Reset Button -->
```{r child = '../shared/Hardware-Overview-Component-0-Reset-Button.md'}
```

<!-- USB Port -->
```{r child = '../shared/Hardware-Overview-Component-5-Omega-USB-Port.md'}
```

#### Mechanical Drawings

<!-- [//]: # (insert gabe's dope mechanical drawings) -->

We have provided a [PDF](https://raw.githubusercontent.com/OnionIoT/wiki/master/Documentation/Hardware/Technical-Drawings/MINI_DOCK_DRAWING.pdf) here.


<!-- [//]: # (LATER: Add using the dock:) -->
<!-- [//]: # ( - usb storage ) -->
<!-- [//]: # ( - controlling a usb serial device) -->
