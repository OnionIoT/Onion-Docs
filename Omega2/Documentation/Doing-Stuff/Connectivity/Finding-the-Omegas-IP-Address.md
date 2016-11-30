---
title: Finding the Omega's IP Address
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 2
---

# Finding the Omega's IP Address

// brief overview of what an IP address is
// some examples as to why you might want to know the ip address

## Finding the IP Address when Connected to a WiFi network

// finding the ip addr for an sta connection, show steps for two methods:
// - using ifconfig and looking for apcli, throw in a little bit of grep -B3 magic
// - using ubus call network.device.wwan, maybe start with the whole output and then narrow it down with grep


## Finding the IP Address of the Omega on it's own AP

// finding the ip addr of the wlan, again show the two methods:
// - using ifconfig and looking for br-wlan, throw in a little bit of grep -B3 magic
// - using ubus call network.device.wlan, maybe start with the whole output and then narrow it down with grep
