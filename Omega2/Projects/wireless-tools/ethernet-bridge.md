## Omega WiFi Ethernet Bridge {#omega-wifi-ethernet-bridge}

// TODO: test this project out, see if we need to make any firwall changes

An Ethernet Bridge is a device that shares its WiFi network access through an Ethernet connection, kind of like an ethernet-based WiFi dongle. If the WiFi network is connected to the internet, the internet connection will be shared as well.

The Omega's flexible networking abilities and the Ethernet Expansion allow us to use the Omega as WiFi Ethernet Bridge!

// TODO: add a photo of this setup!
<!-- ![illustration](./img/ethernet-bridge-illustration.png) -->

As an example, this type of setup can be used to bring internet access to a desktop computer that does not have a network adapter.



### Overview

**Skill Level:** Intermediate

**Time Required:** 10 minutes

What we are going to do is to first enable the Omega's Ethernet connection, and then to bridge the wireless internet connection with an Ethernet connection.


### Ingredients

* Onion Omega2 or Omega2+
* Any Onion Dock that supports Expansions: Expansion Dock, Power Dock, Arduino Dock 2
* Onion Ethernet Expansion
* An Ethernet cable

<!-- The Steps -->
### Step-by-Step

Here's how to turn your Omega into an Ethernet WiFi dongle!

#### 1. Prepare the Omega

To begin, you'll need to make sure your Omega is connected to the Internet and has the latest firmware. Follow this [guide](#first-time-setup) if you'd like to learn more on how to set up your Omega.

<!--# 2 -->

#### 2. Enable the Omega's Ethernet Connection

<!-- // Connect the Ethernet Expansion to the Omega -->

Connect your Ethernet Expansion to your Expansion Dock, and then plug in an Ethernet cord to set up the hardware:

![router network](./img/router-setup.jpg)

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

>If you want to revert your configuration to the original, we have a complete set of default configurations from a factory-fresh Omega2 [in the `uci-default-configs` repo](https://github.com/OnionIoT/uci-default-configs) on GitHub.

// TODO: do we need to configure the firewall?

<!--# 3 -->
#### 3. Configure your Device to use Ethernet

Now that the Omega is configured, we should be able to get on the internet through an Ethernet cable to the Omega.

Make sure that your connection is set to `Obtain IP address and DNS address Automatically`. It should be set so by default.


##### Windows
To do this on Windows, follow this [guide](http://www.computerhope.com/issues/ch001048.htm).


##### Mac OSX
To do this on Mac OSX, follow this [guide](https://www.cs.cmu.edu/~help/networking/dhcp_info/dhcp_mac.html).

<!-- ### Linux -->

<!-- Not sure how to do or how to test that this actually does the thing? -->
