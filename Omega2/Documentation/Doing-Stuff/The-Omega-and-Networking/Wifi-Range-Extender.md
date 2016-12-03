---
title: WiFi Range Extender
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 1
---

## WiFi Range Extender

A WiFi range extender is a device that can increase the effective range of a router by being placed closer to the end user and emitting it's own access point.
The Omega's powerful WiFi capabilities and incredibly small footprint allow it to be effective as a WiFi range extender.


<!-- illustration -->

Even though the Omega has only one physical WiFi interface, you can create two virtual interfaces and have the Omega relay the packets back and forth between the two interfaces. This allows you to set up the Omega as a WiFi range extender that relays the packets between your computer/smartphone and your router. This can be very helpful if your router has a short range and the connection has problems from beyond a certain distance.
Let's get started!


## Overview

| <span style="font-weight:normal">Tutorial Difficulty</span> | Intermediate |
| :--- | :--- |
| Tutorial Difficulty | **Beginner** |
| Time Required | **5 min** |
| Required Materials: | Omega2 or Omega2+<br>Expansion Dock, Mini Dock, Arduino Dock or Power Dock |

<!-- batch2: add a few sentences describing at a high level what the steps will accomplish -->

### Step 1: Connect the Omega to the router

First, you will need to connect the Omega to your router. To do this, you will use the `wifisetup` command:

```
root@Omega-0104:/# wifisetup
Onion Omega Wifi Setup

Select from the following:
1) Scan for Wifi networks
2) Type network info
q) Exit

Selection:
```

Follow the instructions to scan for WiFi and connect to your router's network.

<!-- section on making sure the firewall forwards STA->AP -->
### Step 2: Firewall Settings

Next, you will need to configure the Omega to route packets from your device to the Omega to the Router, and back. To do this, you will be editing the `/etc/config/firewall` file:

Enter the following command to edit the file:
```
vi /etc/config/firewall
```

Find the block that looks something like the following:

```
config zone
    option name         wan
    list   network      'wwan'
    option input        ACCEPT
    option output       ACCEPT
    option forward      ACCEPT
    option masq     1
    option mtu_fix      1
```

and make sure that the input, output, and forwarding settings are set to `ACCEPT`

```
    option input        ACCEPT
    option output       ACCEPT
    option forward      ACCEPT
```


Once you have saved and closed the file, run the following command to restart the firewall with the updated configuration:

```
/etc/init.d/firewall restart
```


### Step 3: Use Your Omega WiFi Range Extender

At this point, your Omega is connected to router as well as serving its own access point, and the Omega is setup to relay information back and forth between these two WiFi interfaces. This means that you can connect your computer/smartphone to the AP of your Omega, and be able to access the data coming from the router.

To use the Omega as the WiFi range extender, you would typically place the Omega somewhere between your router and your computer/smartphone. Packets will travel from your router to the Omega, and from the Omega to your computer/smartphone instead of directly from the router to your device. Effectively, extending your WiFi network's range!

Happy hacking!
