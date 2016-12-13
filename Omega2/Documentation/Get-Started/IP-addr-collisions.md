
## Fix Network IP Address Collisions {#fix-ip-addr-collisions}

If you've been unsuccessful in connecting your Omega to your home WiFi network and you've made sure that the password is 100% correct, you might have an *IP address collision* between your WiFi network and the Omega's AP network.


### What is an IP Address Collision?

<!-- // ip address collision - if both the wifi network and the Omega's AP have the same `192.168.3.0/24` subnet/ip address network prefix, the Omega won't know what to send where -->

An IP address collision can happen with your Omega if both your Omega's Access Point and the WiFi network that you try to connect to share the same subnetwork (subnet). The Omega's Access Point subnet is `192.168.3.0/24` and it's possible that your WiFi can have the same subnet. This results in the Omega not knowing what data to send where.

We'll use an analogy to briefly explain how this works. Say an IP address is the **street address** on a letter. You can think of the subnet being the **city** of that address. So if your Omega's subnet is the same as the WiFi network's and you try to send data to some IP address, it would be like sending a letter to an address in **Paris, France** but then having it arrive at the same address but in ***Paris, Texas, USA***. Not what we wanted, but a good try nonetheless.

>You can read more on subnets and network prefixes on [Wikipedia's Subnetwork article](https://en.wikipedia.org/wiki/Subnetwork).

#### Identifying your WiFi Network's IP Address Prefix

<!-- // need to reconnect your computer to your wifi network and then find your IP address, if it's  `192.168.3.X`, then you have a collision -->
<!-- // link to articles showing how to find a computer's ip address in windows, os x, and linux -->

A IP address collision will happen if your WiFi network's IPv4 address is `192.168.3.X` where X is any number from 0-255. To find your IPv4 Address you'll need to first connect a computer to a WiFi network. Then, based on the OS you'll have to get your wireless config settings.

>You can read [this guide to finding your router's ip address](http://www.howtogeek.com/233952/how-to-find-your-routers-ip-address-on-any-computer-smartphone-or-tablet/) for an in depth explanation.

### Fixing the Collision


There are two possible solutions for fixing the collision. 

1. The first is to change the Omega's AP network prefix.
    * This is method is very simple and will be covered below.
1. The second is to change your router's network prefix. 
    * This is relatively complex and will not be covered in this guide. 

First, connect to the Omega's command-line interface.

To change the Omega's IP address we can use `uci`, a command-line tool that allows us to edit configuration files with simple commands. The command to modify the IP address of your Omega is the following:

```bash
uci set network.wlan.ipaddr=<IP ADDRESS>
```

For example, we can change the Omega's IP Address to `192.168.9.1` by entering the following:

```
uci set network.wlan.ipaddr=192.168.9.1
```

Now once we have set our IP address, we'll want to save this change. The command to save a setting looks like this:

```bash
uci commit <CONFIGURATION>
```

The configuration we're changing is `network`, so we'll enter the following to save our changes:

```
uci commit network
```

Now once you've saved your settings, you'll need to restart the network to apply the changes with this command:

```
/etc/init.d/network restart
```

And that's it! Your Omega's new IP address on its Access Point is now `192.168.9.1`, and there will no longer be a collision. You can now try connecting to your WiFi network again.

<!-- // two ways to fix the collision:
// 1: change the Omega's AP network prefix (easier)
// 2: change your router's network prefix (mention this but say we're not gonna cover this)

// show steps on connecting to the command line, using uci to change the ip address to 192.168.<WHATEVER>.1, restarting the network service, and trying to connect to your wifi network again -->
