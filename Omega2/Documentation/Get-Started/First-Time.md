---
title: Get Started
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 1
---




[//]: # (Prepare the Hardware)

## Unboxing and Getting the Hardware Ready

**Step 1**:

Unpack the Omega and a Dock from their boxes:

![Omega + Dock](http://i.imgur.com/fKZfABhl.jpg "Omega + Dock")

**Step 2**:

Plug the Omega into the socket on the Dock.

![Omega plugged into Dock](http://i.imgur.com/1HNTUgKl.jpg "Omega Plugged into Dock")

Make sure your Omega's pins are fully plugged into the socket:

![Omega plugged into Dock Side View](http://i.imgur.com/0f1Prmul.jpg)

**Step 3**:

Connect the Omega to your computer or other power source through USB.

![Omega plugged into USB](http://i.imgur.com/OgKnUXdl.jpg "Omega plugged into USB")

**Step 4**:

Turn on the Omega using the switch.

![Turn on the Omega](http://i.imgur.com/sAyIEANl.jpg "Turn on the Omega")

**Step 5**:

When the amber LED has been on for about a minute, your Omega will have booted.

![Omega is on](http://i.imgur.com/kpT4L2bl.jpg "Omega is on")

*We're working on making this step more intuitive, stay tuned!*
// LAZAR: need to fix this in the firmware


[//]: # (GUI SETUP)

## Use the Setup Wizard to Get Started

**Step 1**:

Your computer may need some additional programs to access the Omega through a browser:
* If you are using Windows, install Apple's Bonjour Service
* If you are using OS X, you're all set to go
* If you are using Linux, the Zeroconf services should already be installed and you will be good to go

**Step 2**:

Let's find your Omega's name before going any further.

There's a sticker on the Omega's shielding:
// Need image of production omega here

The text printed here is the Omega's unique MAC address, we're interested in the last four digits that are in bold.

Your Omega's name is `Omega-ABCD` where `ABCD` are the last four digits from the sticker.

So the Omega from the picture above is named `Omega-296A`


**Step 3**:

Connect to your Omega’s Access Point, it's named the same as your Omega. The default password is `12345678`.

![Connect to AP](http://i.imgur.com/KumCH9Al.png "Connect to AP")


**Step 4**:

Open your favourite browser and navigate to `http://omega-ABCD.local/` where `ABCD` are the same characters from the network name above.

If the page doesn't load, you can also browse to `http://192.168.3.1`

**Step 5**:

You have now arrived at the Setup Wizard:

![Browse to Setup Wizard](http://i.imgur.com/DaHshUL.png "Browse to Setup Wizard")

Login with the following information:
```
username: root
password: onioneer
```

![Setup Wizard Login](http://i.imgur.com/y5aX5oG.png "Browse to Setup Wizard")

**Step 6**:

Follow the wizard to complete the setup of the Omega, by the end of it, your Omega will be updated with the latest firmware and connected to a WiFi network of your choosing.

**Step 7**:

Start using your fresh Omega, check out the [Tutorials section](./Tutorials/Contents) or the [Project guides](./Projects/Contents) for ideas on what to do next!


## Troubleshooting

### My Omega won't fit into the Dock!

Sometimes the Omega's pins aren't at a perfect 90˚ angle. Don't be afraid to press on them a little to get them to the correct angle, they're tougher than you think!

If they need to be bent inwards a little, try putting the pins up against a flat surface at 45˚ and pushing a little.

// IMAGE OF THIS ACTION

If the pins need to be bent outward, put the pins up against a flat surface near the edge at 45˚ the other way and pushing a little.

// IMAGE OF THIS ACTION

### My Omega won't connect to my WiFi Network

Make sure your password has been typed in correctly, remember, WiFi passwords are case sensitive.

### I've made sure my password is correct and my Omega still won't connect to my WiFi Network

// explanation regarding Omega's IP address
