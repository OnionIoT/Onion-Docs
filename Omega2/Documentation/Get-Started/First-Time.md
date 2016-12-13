##  First Time Setup {#first-time-setup}

Follow along with this guide to set up your Omega2 for the first time. We'll first learn how to properly connect your Omega to a Dock and power it up. Then we'll connect to it to use the Setup Wizard to have it connect to your WiFi network and then do some updates.

<!-- Second sentence above is awkward -->

<!-- Prepare the Hardware -->
```{r child = './Hardware-Prep.md'}
```



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
![Omega2+](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/omega-name-0-just-omega.jpg)

The text printed here is the Omega's unique MAC address, we're interested in the last four digits that are in bold.

Your Omega's name is `Omega-ABCD` where `ABCD` are the last four digits from the sticker.

So the Omega from the picture above is named `Omega-296A`


**Connect to the Omega's WiFi Network**

The Omega hosts it's own WiFi network access point. Lets connect your computer to it. The WiFi network is named the same as your Omega and the default password is `12345678`

![Connect to AP](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/setup-1-connect-to-wifi.png "Connect to AP")


**The Setup Wizard**

Open your favourite browser and navigate to `http://omega-ABCD.local/` where `ABCD` are the same characters from the network name above. If the page doesn't load, you can also browse to `http://192.168.3.1`

You have now arrived at the Setup Wizard:

![Browse to Setup Wizard](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/setup-2-wizard-start.png "Browse to Setup Wizard")

Login with the following information:
```
username: root
password: onioneer
```

![Setup Wizard Login](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/setup-3-wizard-login.png "Browse to Setup Wizard")

After you've logged in you'll be asked to connect to a Wireless Network. This is **MANDATORY** in order to complete the setup-wizard.

![Setup Wizard wifi configure](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/setup-4-wizard-wifi-configure.png)

Enter your Wireless Network information and click configure. Your Omega will attempt to connect to the network. This can take up to a minute to complete. Once connected, you will be moved to the next step.

![Setup Wizard configuring](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/setup-5-wizard-wifi-configuring.png)

On this step you can choose to register your device on the cloud. If you would like to do this some other time you can click `Skip Step` to move onto the next step.

![Setup Wizard cloud](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/setup-6-wizard-cloud.png)

You've nearly finished now. Click the `Upgrade Firmware and Install Console` button to do just that. This will upgrade your Omega to the latest firmware and install the console for you.

>If you don't want to install the console you can de-select the checkbox above. You can always come back to the setup wizard to install the console afterwards.

![Setup Wizard downloading firmware](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/setup-7-wizard-upgrade-button.png)

Your Omega will download the latest firmware, and then begin installing it. This process takes several minutes and you'll know that it's complete when your Omega's LED finishes flashing.

![Setup Wizard installing firmware](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/setup-8-wizard-installing-firmware.png)

When the firmware installation is complete you'll also see the page below, notifying you that your Omega is ready to use.

![Setup Wizard finished](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/setup-9-wizard-finished.png)



**All Done!**

Start using your fresh Omega, check out the [Using the Omega section](#doing stuff) for ideas on what the Omega can do!
<!-- Start using your fresh Omega, check out the [Tutorials section](./Tutorials/Contents) or the [Project guides](./Projects/Contents) for ideas on what to do next! -->
<!-- TODO: fix the links above when the content is available -->
