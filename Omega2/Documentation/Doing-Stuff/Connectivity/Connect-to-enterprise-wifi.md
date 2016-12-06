---
title: Connecting to an Enterprise WiFi Network
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 4
---

## Connecting to an Enterprise WiFi Network with a Username and Password {#omega-enterprise-network}

<!-- // explain what an Enterprise WiFi Network is, that it requires a username and password for added security, give examples where this type on network is used: universities, corporations, etc -->

An Enterprise WiFi Network is a secure network that require a username and login in order to access the internet through the WiFi. A common example of a network that requires this is Eduroam, which can be found at most universities around the world. Many corporations also use Enterprise Networks for added security.

Connecting to these types of networks can be tricky, but in this tutorial we'll try to simplify it into easy steps.


### Step 1: Installing `wpad`

Your Omega starts off with `wpad-mini`, a stripped down version of `wpad` that handles viewer protocols. We'll need to install `wpad` using `opkg`, the package manager on the Omega. First, you'll need to connect to the internet. This can be done using the Ethernet Expansion, or by finding a non-Enterprise WiFi network.

>For more on `opkg`, you can read our [guide to using opkg on the Omega](#using-opkg)

<!-- Really hate this step... Hopefully we can include the full wpad in the firmware to avoid this. -->


You'll then need to run the following commands to remove `wpad-mini`, and install `wpad`:

```
opkg update
opkg remove wpad-mini
opkg install wpad
```

### Step 2:  Determine the Authentication Type

You'll need to determine the authentication type of the network in order to connect t

I am assuming you are capable of connecting to the Enterprise secured WiFi through another device, a laptop, for example. You can then easily find what type of authentication the newtork uses:

![type of security](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/connecting-enterprise-pic-1.png)

In the picture above, I am using a Linux device to find the security type. This can be done on other operating systems as well by finding the wireless properties and reading the security type. So from the picture you can see the encryption type of my Eduroam network is WPA/WPA2 Mixed Enterprise, and the EAP Type is Protected EAP (PEAP).

In case your network doesn't match the one above, you can check out [OpenWRT's networking documentation](https://wiki.openwrt.org/doc/uci/wireless#wpa_modes) to find the encryption type that matches yours. You'll need this for the next steps.


### Step 3: Configuring your Wireless Network

First, run `wifisetup` to add the enterprise network to your list of networks. Run `vi /etc/config/wireless` look for the block of code that resembles the one below:

```
config wifi-iface
        option device 'ra0'
        option network 'wlan'
        option mode 'ap'
        option encryption 'psk2'
        option key '12345678'
        option ApCliAuthMode 'WPA2PSK'
        option ApCliEncrypType 'AES'
        option ApAuthMode 'WPA2PSK'
        option ApCliEnable '1'
        option ApCliSsid 'OnionWiFi'
        option ApCliPassWord 'onioneer'
        option ssid 'Omega-2757'

```

Now, modify this entry with the information corresponding to the network type according to the [OpenWRT wiki page](https://wiki.openwrt.org/doc/uci/wireless#wpa_modes) mentioned above.

```
config wifi-iface               
        option device 'ra0'  
        option mode 'sta'       
        option network 'wwan'   
        option eap_type 'peap'  
        option ssid 'eduroam'   
        option encryption 'wpa-mixed'
        option auth 'MSCHAPv2'       
        option identity '<your user name>'
        option password '<your password>'
        option disabled '0'
```

<!-- This needs some work. The config file does not resemble this stuff any more -->

The order doesn't matter, as long as all of the options are defined.


[//]: # (Step 4)

### Step 4: Restart the Service

Let's apply our settings by restarting the network service. Run `/etc/init.d/network restart` and you should now be connected to the enterprise network.

If this does not work, try rebooting your Omega. If you still cannot connect to the network, go back and double-check your settings.

Otherwise, enjoy your super-secure WiFi connection on your Omega!



<!-- // base it on the existing article, just fix the english -->
<!-- // talk to Lazar re including the full `wpad` package in the firmware by default (instead of `wpad-mini`) -->
