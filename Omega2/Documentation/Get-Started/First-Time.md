## The Very First Time {#first-time-setup}

Follow along with this guide to set up your Omega2 for the first time. We'll first learn how to properly connect your Omega to a Dock and power it up. Then we'll connect to it to use the Setup Wizard to have it connect to your WiFi network and then do some updates.

<!-- Second sentence above is awkward -->
<!-- LAZAR: include case where there is no dock -->


<!-- Prepare the Hardware -->

### Unboxing and Getting the Hardware Ready

**Unpack**

Unpack the Omega and Dock from their boxes

![Omega + Dock](https://github.com/OnionIoT/Onion-Docs/tree/master/Omega2/Documentation/Get-Started/img/unbox-1-omega-with-dock.jpg?raw=true "Omega + Dock")

**Connect**

Plug the Omega into the socket on the Dock

![Omega plugged into Dock](https://github.com/OnionIoT/Onion-Docs/tree/master/Omega2/Documentation/Get-Started/img/unbox-2-omega-on-dock.jpg?raw=true "Omega Plugged into Dock")

Make sure your Omega's pins are fully plugged into the socket

![Omega plugged into Dock Side View](https://raw.githubusercontent.com/OnionIoT/tree/master/Omega2/Documentation/Get-Started/img/unbox-3-omega-on-dock-side.jpg)

**Provide Power**

The Omega itself is powered by a 3.3V source. But all Omega Docks have voltage regulators so you can use any microUSB to power the Dock and Omega.

<!-- ADD THIS: Plug a microUSB into your Omega -->
<!-- ADD PHOTO -->

You can power it with your computer

![Omega plugged into USB](https://github.com/OnionIoT/Onion-Docs/tree/master/Omega2/Documentation/Get-Started/img/unbox-4-omega-provide-power.jpg?raw=true "Omega plugged into USB")

Or you can power it with any wall adapter

<!-- include image of wall adapter -->

**Power On!**

Turn on the Omega using the switch.

![Turn on the Omega](https://github.com/OnionIoT/Onion-Docs/tree/master/Omega2/Documentation/Get-Started/img/unbox-5-omega-switched-on.jpg?raw=true "Turn on the Omega")

**Wait till it boots**

When the amber LED has been on for about a minute, your Omega will have booted.

![Omega is on](https://github.com/OnionIoT/Onion-Docs/tree/master/Omega2/Documentation/Get-Started/img/unbox-6-omega-led-detail.jpg?raw=true "Omega is on")

*We're working on making this step more intuitive, stay tuned!*

<!-- LAZAR: need to fix Omega LED in the firmware, when fixed, make sure to give time estimate for how long boot takes -->


<!-- GUI SETUP -->

### Using the Setup Wizard

**Some Computer Configuration**

Your computer may need some additional programs to access the Omega through a browser:
* If you are using Windows, install Apple's Bonjour Service
* If you are using OS X, you're all set to go
* If you are using Linux, the Zeroconf services should already be installed and you will be good to go

**The Omega's Name**

Let's find your Omega's name before going any further.

There's a sticker on the Omega's shielding:

<!-- Need image of production omega here -->

The text printed here is the Omega's unique MAC address, we're interested in the last four digits that are in bold.

Your Omega's name is `Omega-ABCD` where `ABCD` are the last four digits from the sticker.

So the Omega from the picture above is named `Omega-296A`


**Connect to the Omega's WiFi Network**

The Omega hosts it's own WiFi network access point. Lets connect your computer to it. The WiFi network is named the same as your Omega and the default password is `12345678`

![Connect to AP](https://github.com/OnionIoT/Onion-Docs/tree/master/Omega2/Documentation/Get-Started/img/setup-1-connect-to-wifi.png "Connect to AP")


**The Setup Wizard**

Open your favourite browser and navigate to `http://omega-ABCD.local/` where `ABCD` are the same characters from the network name above. If the page doesn't load, you can also browse to `http://192.168.3.1`

You have now arrived at the Setup Wizard:

![Browse to Setup Wizard](https://github.com/OnionIoT/Onion-Docs/tree/master/Omega2/Documentation/Get-Started/img/setup-2-wizard-start.png "Browse to Setup Wizard")

Login with the following information:
```
username: root
password: onioneer
```

![Setup Wizard Login](https://github.com/OnionIoT/Onion-Docs/tree/master/Omega2/Documentation/Get-Started/img/setup-3-wizard-login.png "Browse to Setup Wizard")

Follow the wizard to complete the setup of the Omega, by the end of it, your Omega will be updated with the latest firmware and connected to a WiFi network of your choosing.

**All Done!**

Start using your fresh Omega, check out the [Tutorials section](./Tutorials/Contents) or the [Project guides](./Projects/Contents) for ideas on what to do next!

<!-- TODO: fix the links above when the content is available -->


### Troubleshooting

#### My Omega won't fit into the Dock!

Sometimes the Omega's pins aren't at a perfect 90˚ angle. Don't be afraid to press on them a little to get them to the correct angle, they're tougher than you think!

If they need to be bent inwards a little, try putting the pins up against a flat surface at 45˚ and pushing a little.

<!-- IMAGE OF THIS ACTION -->

If the pins need to be bent outward, put the pins up against a flat surface near the edge at 45˚ the other way and pushing a little.

<!-- IMAGE OF THIS ACTION -->

#### My Omega won't connect to my WiFi Network

Make sure your password has been typed in correctly, remember, WiFi passwords are case sensitive.

#### I've made sure my password is correct and my Omega still won't connect to my WiFi Network

<!-- explanation regarding Omega's IP address -->
