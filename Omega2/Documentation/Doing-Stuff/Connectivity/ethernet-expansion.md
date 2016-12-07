---
title: Using the Ethernet Expansion
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 2
---

## Using the Ethernet Expansion {#ethernet-expansion}


The Ethernet Expansion is a piece of hardware that gives your Omega the ability to establish an Ethernet connection with other devices. With this Expansion, you can use your Omega as a router, an Ethernet bridge, and more.

<!-- // a photo on the Expansion -->

### Connecting to a Network through Ethernet

The Ethernet Expansion can be used to establish a wired internet connection to the Omega. We're going to go through how to properly set up your Omega.

### Step 1: Enable `eth0`

The Omega is primarily designed as a development board to prototype WiFi-enabled devices, so by default, we have turned off the ethernet interface `eth0` in the firmware. In order to use the Ethernet Expansion, you will need to make sure this is enabled. To do this, you will need to open up the `/etc/config/network` file, find the block that looks something like the following:

```
config interface 'wan'
   option ifname 'eth0'
   option proto 'dhcp'   
```
and add the following line:

```
option hostname 'OnionOmega'
```

```
config interface 'wan'
   option ifname 'eth0'
   option proto 'dhcp'
   option hostname 'OnionOmega'
```

This will tell the Omega to turn on the `eth0` interface and we will also be referring to this network as `wan`.

Once you have saved and closed the file, run the following command to restart the network service to reload the new configuration:

```
/etc/init.d/network restart
```

### Step 2: Enabling Packet Routing

Next, you will need to configure the Omega to route packets from the Ethernet interface (`eth0`) to your WiFi interface (`wlan0`). To do this, you will be editing the `/etc/config/firewall` file:

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

and add the following line:

```
list   network      'wan'
```

What you will end up with is something like the following:

```
config zone
    option name         wan
    list   network      'wwan'
    list   network      'wan'
    option input        ACCEPT
    option output       ACCEPT
    option forward      ACCEPT
    option masq         1
    option mtu_fix      1
```

What this tells the Omega to do is to add the `wan` network (which we defined in the `/etc/config/network` file) to a firewall zone called `wan`. This zone has already been setup to route packets to another firewall zone called `lan`, which contains the `br-wlan` interface.

Once you have saved and closed the file, run the following command to restart the firewall with the updated configuration:

```
/etc/init.d/firewall restart
```

Your Ethernet Expansion is now ready to supply an internet connection to your Omega. Simply plug an Ethernet cord into an Ethernet port on a modem or a router, and connect it to your Ethernet Expansion.


### Going Further with the Ethernet Expansion

If you don't have a router and need to supply internet to devices, the Ethernet Expansion can transform the Omega into a very effective router. For more on that you can read our [tutorial on transforming your Omega into a router](#omega-router)


You can use the Ethernet Expansion and the Omega to provide a wired connection to a laptop or a computer. This is known as an Ethernet Bridge, and you can learn more about it in our [tutorial on creating an Ethernet Bridge using the Omega](#ethernet-bridge)
