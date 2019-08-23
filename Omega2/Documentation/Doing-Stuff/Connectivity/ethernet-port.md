## The Ethernet Port {#the-ethernet-port}

The Omega2 family devices feature a single 10/100M Ethernet integrated PHY. The addition of a transformer and a RJ45 port allow for quick and easy wired networking with ethernet cables. 


The ethernet port can be configured to be a client or a DHCP host. It is set to client mode by default. Given the flexibility of the networking stack on the Omega2, there are a few overall modes of operation available:

* Ethernet client - Omega obtains network access through a wired connection
* Ethernet client + Router - Omega obtains network access through a wired connection and **shares** network access through its WiFi AP
* Ethernet host - Omega provides IP addresses to a device connected to the ethernet port
* Ethernet bridge - Omega obtains network access by connecting to a wireless network and **shares** network access to a device through ethernet

When using a through-hole Omega2 on a Dock with an Expansion Header, the Ethernet Expansion can be used to quickly add wired networking capabilities to the device. With custom hardware powered by the Omega2 or Omega2S, a transformer and an RJ45 port are required. See the [Omega2S Reference Schematic](https://github.com/OnionIoT/Omega2/blob/master/Schematics/Omega2S-Reference-Schematic.pdf) for details.


<!-- ethernet client and ethernet host explanation  -->
```{r child = './ethernet-port-content.md'}
```
