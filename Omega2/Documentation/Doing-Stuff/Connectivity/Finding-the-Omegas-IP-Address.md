---
title: Finding the Omega's IP Address
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 2
---

## Finding the Omega's IP Address {finding-omega-ip-address}

<!-- // brief overview of what an IP address is -->

Every machine on a network has a unique identifier, known as an IP address. Just as you put an address on a letter to send in the mail, computers use an IP address to send data to specific machines on a network. An IP address is 4 sets of numbers separated by periods. These numbers range from 0-255, and the format of an IP address is as follows:

```
123.456.789.001
```

More commonly, you'll see the leading 0's being cut off resulting in a shorter IP Address

```
123.456.789.1
```

You may want to know your Omega's IP address if you don't have Apple's Bonjour Service to find the hostname `omega-ABCD.local`, or if you want to guarantee that there won't be a mix-up between hostnames (IP addresses are unique, hostnames are not).


<!-- // some examples as to why you might want to know the ip address -->

### Finding the IP Address when Connected to a WiFi network

<!-- // finding the ip addr for an sta connection, show steps for two methods: -->


#### Finding your Omega's IP Address with `ifconfig`

You can use the `ifconfig` command to get information about all the network interfaces on your Omega. We are going to use it to get the IP address of the `apcli0` interface, which is used to connect to the internet. Type the following command to see the IP address of the `apcli0` interface:

```
ifconfig | grep apcli0 -A 1 | grep inet
```

Your command-line output will looks something like this:

```
root@Omega-2757:/# ifconfig | grep apcli0 -A 1 | grep inet
          inet addr:192.168.1.111  Bcast:192.168.1.255  Mask:255.255.255.0
```

And your IP Address is what follows the `inet addr:`. My Omega's IP address is `192.168.1.111`.


#### Finding your Omega's IP Address with `ubus`

You can use the `ubus` command to find information about your network devices. Type the following to bring up the full status of your wireless wide area network (WWAN):

```
ubus call network.interface.wwan status
```

This will show you all the information about your Omega's `apcli0` device, which handles the WiFi connection of the Omega.


To narrow down your result to just the IP address we can use `grep`. `grep` allows you to isolate your output based on keywords or patterns. We are going to isolate the address line so that we have easy access to the IP address of our Omega with the following command:

```
ubus call network.interface.wwan status | grep -w "address" | grep -v "-"
```

The result should look similar to this:

```
root@Omega-2757:/# ubus call network.interface.wwan status | grep -w address | grep -v "-"
                        "address": "192.168.1.111",
```


My Omega's IP address is `192.168.1.111`. I can connect to my Omega with this IP address, and send data to the Omega from my device.

<!-- // - using ifconfig and looking for apcli, throw in a little bit of grep -B3 magic -->
<!-- // - using ubus call network.device.wwan, maybe start with the whole output and then narrow it down with grep -->


### Finding the IP Address of the Omega on it's own AP

<!-- // finding the ip addr of the wlan, again show the two methods: -->

#### Finding the Omega's IP address on it's own AP Using `ifconfig`

You can use the `ifconfig` command to get information about all the network interfaces on your Omega. We are going to use it to get the IP address of the `br-wlan` interface, which handles the Omega's AP. Type the following command to see the IP address of the `br-wlan` interface:

```
ifconfig | grep br-wlan -A 1 | grep inet
```

Your command-line output will looks something like this:

```
root@Omega-2757:/# ifconfig | grep br-wlan -A 1 | grep inet
          inet addr:192.168.3.1  Bcast:192.168.3.255  Mask:255.255.255.0
```

And your IP Address is what follows the `inet addr:`. My Omega's IP address is `192.168.3.1`.

#### Finding the Omega's IP address on it's own AP Using `ubus`

Your Omega also has a designated IP Address on it's own Access Point. If you connect to your Omega's WiFi (connecting to the network called `Omega-ABCD`), it will have it's own IP address. The Omega's default IP Address on it's own AP is `192.168.3.1`, but you can verify this by entering the following command:

```
ubus call network.interface.wlan status
```

This will show you all the information about your Omega's `br-wlan` device, which handles the Omega's AP.

We can narrow this down further using `grep`. `grep` allows you to isolate keywords or patterns in your output. We're going to use it to isolate the IP Address of our Omega.

```
ubus call network.interface.wlan status | grep -A 2 ipv4 | grep -w address | grep -v -
```

```
root@Omega-2757:/# ubus call network.interface.wlan status | grep -A 2 ipv4 | grep -w address | grep -v -
                        "address": "192.168.3.1",
```

Here we see that on my Omega's Access Point, the IP address designated to the Omega is `192.168.3.1`. If I connect to the `Omega-2757` WiFi network on my computer, I can communicate with my Omega using this IP address.
<!-- // - using ifconfig and looking for br-wlan, throw in a little bit of grep -B3 magic -->
<!-- // - using ubus call network.device.wlan, maybe start with the whole output and then narrow it down with grep -->
