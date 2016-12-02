---
title: Ethernet Bridge
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 3
---

# Ethernet Bridge

// descriptive sentence describing what an ethernet bridge is: omega accepting wifi, relaying the connection to an attached device via ethernet
In this tutorial, we are going to go through how we can enable other devices to use the Omega's Ethernet Expansion to connect to an existing Wi-Fi network.

![illustration](../img/ethernet-bridge-illustration.png)

// add an example scenario where this would be useful (bringing wifi connectivity to an old desktop computer)

# Overview

| Overview |
| :---: | :---: |
| Tutorial Difficulty | **Intermediate** |
| Time Required | **10 mins** |
| Required Materials: | <ul><li>Omega2 or Omega2+</li><li>Expansion Dock</li><li>Ethernet Expansion</li></ul> |

// add a note saying that the Power Dock or Arduino Dock 2 can be used

What we are going to do is to first enable the Omega's Ethernet connection, and then try to bridge the wireless internet connection with an Ethernet connection.


[//]: # (The Steps)

## Step 1: Connect Omega with WiFi

// change this sentence
This step is fairly easy, and there are a lot of tutorials tell us how to do so in different ways. Follow this [guide](../Get-Started) to learn more on how to set up your Omega.


[//]: # (Step 2)

## Step 2: Enable the Omega's Ethernet Connection

// Connect the Ethernet Expansion to the Omega


What we need to do is to change the following code block located in `/etc/config/network`:

```
config interface 'wlan'
        option type 'bridge'
        option ifname 'eth0.1'
        option proto 'static'
        option ipaddr '192.168.3.1'
        option netmask '255.255.255.0'
        option ip6assign '60'

```

Change `option ifname 'eth0.1'` to `option ifname 'eth0'`


Restart the network service by running the follow command:
```
/etc/init.d/network restart
```



[//]: # (Step 3)
## Step 3: Configure your Device to use Ethernet

Now that the Omega is configured, we should be able to connect with other devices via Ethernet.

Make sure that your connection is set to `Obtain IP address and DNS address Automatically`. It should be set so by default.


### Windows
To do this on Windows, follow this [guide](http://www.computerhope.com/issues/ch001048.htm)


### Mac OSX
To do this on Mac OSX, follow this [guide](https://www.cs.cmu.edu/~help/networking/dhcp_info/dhcp_mac.html)

### Linux

[//]: # (Not sure how to do or how to test that this actually does the thing?)


[//]: # (Using the Project)
