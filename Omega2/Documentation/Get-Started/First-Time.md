##  First Time Setup {#first-time-setup}

Follow along with this guide to set up your Omega2 for the first time. We'll first learn how to properly connect your Omega to a Dock and power it up. Then we'll connect to it to use the Setup Wizard to have it connect to your WiFi network and then do some updates.

<!-- Second sentence above is awkward -->

<!-- Prepare the Hardware -->
```{r child = './First-Time-Components/Hardware-Prep.md'}
```



<!-- GUI SETUP -->

### Using the Setup Wizard

<!-- Computer Config -->
```{r child = './First-Time-Components/First-Time-Component-01-computer-config.md'}
```

<!-- The Omega's Name -->
```{r child = './First-Time-Components/First-Time-Component-02-omega-name.md'}
```

<!-- Connect to Omega's Wifi AP -->
```{r child = './First-Time-Components/First-Time-Component-03-connect-to-omega-network.md'}
```

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
