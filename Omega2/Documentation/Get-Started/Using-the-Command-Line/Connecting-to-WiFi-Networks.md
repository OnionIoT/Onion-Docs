

## Connecting To WiFi Networks in the Command-Line {#connecting-to-wifi-networks-command-line}

<!-- // TODO:
//  idea: separate the what from the how in this article
//  lets have a section outlining WHAT is going to happen here:
//    - enter network info
//    - connection attempt based on available networks and configured network priority
//      - super describe what priority means in this case - assume that readers of this article haven't read any of the console articles
//      - mention that the AP will go down for about a maximum of 30 seconds while the connection is attempted
//    - talk about the case where connecting to the STA fails - how the AP should come back up afterwards, give a few reasons as to why the connection may have failed (wrong authentication type selected, wrong password entered)
//
//  And then we can go over the 3 HOWs:
//    1) scanning for available networks
//    2) typing the network info
//    new section - using command line arguments -->

The Omega comes ready with a command-line tool called `wifisetup` that makes it easy to connect your Omega to the Internet. This article will cover what `wifisetup` is, as well as how you can use it to connect your Omega to the Internet.

### Using `wifisetup`

To begin setting up your connection to the Internet, enter `wifisetup` in a terminal, and you'll see the following output:

```
root@Omega-2757:/# wifisetup
Onion Omega Wifi Setup

Select from the following:
1) Scan for Wifi networks
2) Type network info
q) Exit

Selection:
```

You can enter `1`, and your Omega will scan for available networks:

```
Selection: 1
Scanning for wifi networks...

Select Wifi network:
1) BYB-Guest
2) BYB-Corporate
3) studio six
4) maya
5) ITL
6) maya
7) EG Energy
8) maya
9) Omega_C02759
10) Authentica
11) OnionWiFi
12) Omega-2928
13) OnionFriends
14) Orpheus
15) Omega-18C2

Selection:
```


Enter your selection and you will be prompted for a password if required. Your network authentication type will be automatically detected in the scan:


```
Selection: 11
Network: OnionWiFi
Authentication type: WPA2PSK
Enter password:
```

Enter your password, and hit enter. Your Omega's network adapter will restart, causing the AP to go down for roughly 30 seconds. Once your network adapter is back up, it will attempt to connect to the network.


>**The Omega's Network Manager**

>The Omega's network manager will attempt to the networks in range that are configured on your Omega. For example, if you have three configured networks (school, home, friend's house) and you're currently at your friend's house, the network manager will immediately attempt to connect to that network.

>On the other hand, if you have multiple configured networks in range the Omega will attempt to connect to the network with the highest priority. Priority is defined as most recently configured networks having the lowest priority. This means that adding a network configuration immediately assigns it as the lowest priority.


### Entering Network Info Manually

Alternatively, you can choose to type in the network info yourself by entering `2` as your selection.

```
Selection: 2
Enter network name:
```
Enter your network's name (SSID) and hit enter


```
Selection: 2
Enter network name: OnionWiFi

Select network authentication type:
1) WPA2
2) WPA
3) WEP
4) None

Selection:
```

Select the network authentication type

```
Selection: 2
Enter network name: OnionWiFi

Select network authentication type:
1) WPA2
2) WPA
3) WEP
4) None

Selection: 1
Enter password:
```

Enter your password, and hit enter. Your Omega's network adapter will restart, causing the AP to go down for roughly 30 seconds. Once your network adapter is back up, it will attempt to connect to the network.

>**The Omega's Network Manager**

>The Omega's network manager will attempt to the networks in range that are configured on your Omega. For example, if you have three configured networks (school, home, friend's house) and you're currently at your friend's house, the network manager will immediately attempt to connect to your friend's house's network.

>On the other hand, if you have multiple configured networks in range the Omega will attempt to connect to the network with the highest priority. Priority is defined as most recently configured networks having the lowest priority. This means that adding a network configuration immediately assigns it as the lowest priority.



### Using the `wifisetup` Command-Line Arguments


You can also use `wifisetup` in the command line to directly add configurations without having to go through the user input method. To begin lets show the available usage for `wifisetup` with the following command:

```
wifisetup -h
```


Going through the available commands we see that we can add new networks, edit current networks, remove current networks, change the priority of networks, list the networks, and list the info about a specific network.


#### Adding or Editing a Network

To add or edit a network use the following:

```bash
wifisetup add -ssid <SSID> -encr <ENCRYPTION TYPE> -password <PASSWORD>
wifisetup edit -ssid <SSID> -encr <ENCRYPTION TYPE> -password <PASSWORD>
```

For example to add a network named `myNetwork` enter the following:

```
wifisetup add -ssid myNetwork -encr psk2 -password mynetworkpassword
```

And if you wanted to edit the network after adding it, you would enter:

```
wifisetup edit -ssid myNetwork -encr psk2 -password myNewNetworkPasswordWithCaps
```

#### Removing a Network

The command for removing a network takes in the ssid as the only parameter:

```
wifisetup remove -ssid <SSID>
```

From the above example, if you were to remove `myNetwork` from my list of configured networks you would enter the following

```
wifisetup remove -ssid myNetwork
```

>Note if you have multiple networks with the same SSID, this command would remove the highest priority network from your list of configured networks.


#### Changing a Network's Priority

The network priority determines the order in which the Omega's network manager will attempt to connect, assuming that the network is within range. A network of higher priority will have a lower number. For example, your highest priority network has priority 1, and your Omega will attempt to connect to that network first if it is available.

You can use `wifisetup priority -ssid <SSID> -move <up|down>` to change the priority of a specified network.

For example, to move the priority of `myNetwork` up you would enter:

```
wifisetup priority -ssid myNetwork -move up
```

and to move it down you would enter:

```
wifisetup priority -ssid myNetwork -move down
```
