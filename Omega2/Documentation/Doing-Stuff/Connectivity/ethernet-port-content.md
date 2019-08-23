### Ethernet Client: Connecting to a Network through Ethernet

The Omega can join networks through a wired Ethernet connection, much like a desktop computer. By default, the Ethernet port on the Omega is configured to act as a network client, allowing users to simply plug in an ethernet cable and the Omega will do the rest: connecting to the network and attempting to obtain an IP address.

> Note that by default, the Omega will have internet access. But it will not automatically share internet access to any devices connected to the Omega's WiFi AP.

#### Enabling Ethernet Client Mode

As mentioned, the ethernet port is configured for ethernet client operation by default. However, if the configuration on your Omega has changed and you would like to quickly return to ethernet client mode, run the following command:

```
onion ethernet client
```

This will:

* Configure the `wan` network interface to expect to obtain an IP address through DHCP
* Remove any `lan` network interfaces 
* Remove any `lan` DHCP configurations

#### How Client Mode Works

> For background, the Omega's Ethernet interface is called `eth0` by the system .

The default configuration in `/etc/config/network` defines a `wan` network interface that uses the physical `eth0` interface, and expects to be given an IP address through DHCP.

Opening the `/etc/config/network` file, you will find a block that looks something like the following:

```
config interface 'wan'
   option ifname 'eth0'
   option proto 'dhcp'   
```

> To learn more about OpenWRT's network configuration, see the [related OpenWRT network documentation](https://openwrt.org/docs/guide-user/base-system/basic-networking).


##### Packet Routing

By default, the Omega's firewall is **not** configured to share ethernet network access through the Omega's WiFi Access Point. 

If the goal is to share ethernet network access through the Omega's WiFi Access Point, then the firewall configuration will need to be changed. Specifically, we will need to:

* Add our `wan` network interface (that uses the `eth0` ethernet interface) to the `wan` firewall rule
* Update the `wan` firewall rule to **allow packet forwarding**


To do this, open the `/etc/config/firewall` file, find the block that looks something like:

```
config zone
        option name 'wan'
        option output 'ACCEPT'
        option forward 'REJECT'
        option masq '1'
        option mtu_fix '1'
        option network 'wwan'
        option input 'ACCEPT'
```

and do the following:

* Change `option forward 'REJECT'` to `option forward 'ACCEPT'`
* Change `option network 'wwan'` to `list network 'wwan'`
* Add `list network 'wan'` after the `list network 'wwan'` line

```
config zone
        option name 'wan'
        option output 'ACCEPT'
        option forward 'ACCEPT'  # changed to ACCEPT
        option masq '1'
        option mtu_fix '1'
        list network 'wwan' # changed 'option' to 'list'
        list network 'wan'  # added wan network to list
        option input 'ACCEPT'
```

> To learn more about OpenWRT's firewall, see the [related OpenWRT firewall documentation](https://openwrt.org/docs/guide-user/firewall/firewall_configuration).


### Ethernet Host: Acting as the Host on a Wired Network

Alternatively, the ethernet port can act as a host. Any devices connected to the ethernet port will receive an IP address - similar to when a device is connected directly to the ethernet ports on the back of a router.

#### Enabling Ethernet Host Mode

The ethernet port can be configured for host mode by running the following:

```
onion -t ethernet host
/etc/init.d/ethernet-mode disable
reboot
```

This will:

* Remove the existing `wan` network interface that configures the ethernet port as a client
* Creates a `lan` network interface that statically sets the IP address of that interface to `192.168.100.1`
* Creates a DHCP `lan` configuration that uses the `lan` network interfaces, and assigns any connected devices an IP address in the range of `192.168.100.100` to `192.168.100.150`
* Disable the `ethernet-mode` service that runs at boot to make sure the ethernet port is set to client mode

After your Omega reboots, the ethernet port will act as a host, assigning IP addresses to any connected devices.

#### How Host Mode Works

> For background, the Omega's Ethernet interface is called `eth0` by the system .

After running the command above to enable ethernet host host mode, the configuration in `/etc/config/network` will define a `lan` network interface that uses the physical `eth0` interface, and statically sets the IP address of that interface to `192.168.100.1`

Opening the `/etc/config/network` file, you will find a block that looks something like the following:

```
config interface 'lan'
        option ifname 'eth0'
        option force_link '1'
        option macaddr '40:a3:6b:c0:27:84'
        option type 'bridge'
        option proto 'static'
        option ipaddr '192.168.100.1'
        option netmask '255.255.255.0'
        option ip6assign '60'
```

> To learn more about OpenWRT's network configuration, see the [related OpenWRT network documentation](https://openwrt.org/docs/guide-user/base-system/basic-networking).


##### DHCP 

To be able to assign IP addresses to devices that connect to the ethernet port, there has to be a DHCP configuration. After running the command above to enable ethernet host host mode, the configuration in `/etc/config/dhcp` will define a `lan` DHCP configuration. It will be set up to assign IP address to connected devices in the range of `192.168.100.100` to `192.168.100.150` for 12 hour lease times.

> About the assigned IP addresses: the base `192.168.100.*` part comes from the `lan` network interface's static IP address and netmask (set in `/etc/config/network`), and the range of `100` to `150` is configured here in the DHCP configuration.

Opening the `/etc/config/dhcp` file, you will find a block that looks something like the following:

```
config dhcp 'lan'
        option interface 'lan'
        option start '100'
        option limit '150'
        option leasetime '12h'
        option dhcpv6 'server'
        option ra 'server'
```

> To learn more about OpenWRT's DHCP configuration, see the [related OpenWRT DHCP documentation](https://openwrt.org/docs/guide-user/base-system/dhcp).
