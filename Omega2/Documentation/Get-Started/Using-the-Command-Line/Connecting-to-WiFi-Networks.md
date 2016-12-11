

## Connecting To WiFi Networks in the Command-Line {#connecting-to-wifi-networks-command-line}

// TODO:
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
//    new section - using command line arguments

The Omega comes ready with a command-line tool called `wifisetup` that makes it easy to connect your Omega to the internet. To begin setting up your connection to the internet, enter `wifisetup` in a terminal, and you'll see the following output:

```
root@Omega-2757:/# wifisetup
Onion Omega Wifi Setup

Select from the following:
1) Scan for Wifi networks
2) Type network info
q) Exit

Selection:

```

### Scanning for Available Networks

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


Enter your selection and you will be prompted for a password if required:
// TODO: add a note saying that the network authentication type will be detected automatically when using this method

```
Selection: 11
Network: OnionWiFi
Authentication type: WPA2PSK
Enter password:
```

Enter your password, and hit enter. Your Omega's network adapter will restart, and the network manager will attempt to connect to the available network with the highest priority.


### Entering Network Info Manually

Alternatively, you can choose to type in the network info yourself by entering `2` as your selection.

```
Selection: 2
Enter network name:
```
Enter your Network's name (SSID) and hit enter


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

Enter your password, and hit enter. Your Omega's network adapter will restart, and the network manager will attempt to connect to the available network with the highest priority.


### Entering Network Information

// TODO: section on using wifisetup non-iteractively, ie just using command line arguments
//  - do an example of adding a new network
//  - give an overview of what else you can use wifisetup for (editing configured networks, removing them, changing the priority, etc)
//  - show how they can print the wifisetup full usage
