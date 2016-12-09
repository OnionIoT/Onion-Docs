

## Connecting To WiFi Networks in the Command-Line {#connecting-to-wifi-networks-command-line}

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

```
Selection: 11
Network: OnionWiFi
Authentication type: WPA2PSK
Enter password:
```

Enter your password, and hit enter. Your Omega's network adapter will restart, and the network manager will attempt to connect to the available network with the highest priority.


### Entering Network Info Manually

You can choose to type in the network info yourself by entering `2` as your selection.

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
