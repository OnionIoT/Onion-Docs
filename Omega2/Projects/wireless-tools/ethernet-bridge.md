## Omega as an WiFi Ethernet Bridge


An Ethernet Bridge is a device that shares its WiFi internet access through an Ethernet connection, similar to a WiFi dongle.

Our Omega's WiFi and the Ethernet Expansion will allow this to be accomplished.

<!-- ![illustration](../img/ethernet-bridge-illustration.png) -->

As an example, this type of setup can be used to bring internet access to a desktop computer that does not have a network adapter.

// TODO: add a photo of this setup!

### Overview

**Skill Level:** Intermediate

**Time Required:** 10 minutes

What we are going to do is to first enable the Omega's Ethernet connection, and then to bridge the wireless internet connection with an Ethernet connection.


### Ingredients

1. Onion Omega2 or Omega2+
1. Any Onion Dock that supports Expansions: Expansion Dock, Power Dock, Arduino Dock 2
1. Onion Ethernet Expansion
1. An Ethernet cable

<!-- The Steps -->
### Step-by-Step

Here's how to turn your Omega into a WiFi dongle!

#### 1: Connect Omega WiFi to the Internet

To begin, you'll need to make sure your Omega is connected to the Internet and has the latest firmware. Follow this [guide](#first-time-setup) if you'd like to learn more on how to set up your Omega.

<!--# 2 -->

#### 2: Enable the Omega's Ethernet Connection

<!-- // Connect the Ethernet Expansion to the Omega -->

Connect your Ethernet Expansion to your Expansion Dock, and then plug in an Ethernet cord to set up the hardware.

What we need to do next is change the following code block located in `/etc/config/network`:

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

>If you want to revert your configuration to the original, we have a complete set of default configurations from a factory-fresh Omega2 [here](https://github.com/OnionIoT/uci-default-configs)


<!--# 3 -->
#### 3: Configure your Device to use Ethernet

Now that the Omega is configured, we should be able to get on the internet through an Ethernet cable to the Omega.

Make sure that your connection is set to `Obtain IP address and DNS address Automatically`. It should be set so by default.


##### Windows
To do this on Windows, follow this [guide](http://www.computerhope.com/issues/ch001048.htm)


##### Mac OSX
To do this on Mac OSX, follow this [guide](https://www.cs.cmu.edu/~help/networking/dhcp_info/dhcp_mac.html)

<!-- ### Linux -->

<!-- Not sure how to do or how to test that this actually does the thing? -->
