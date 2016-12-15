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
1) BYB
2) studio sixteen
3) EG Energy
4) mayaaa
5) Authentic
6) OnionWiFi
7) Orpheus
8) Omega-18C2

Selection:
```


Enter your selection and you will be prompted for a password if required. Your network authentication type will be automatically detected in the scan:


```
Selection: 6
Network: OnionWiFi
Authentication type: WPA2PSK
Enter password:
```

Enter your password, and hit enter. Your Omega's network adapter will restart and attempt to connect to the new network.

Since the network adapter is restarting, the Omega's AP will go down and be inaccessible during this period, but it will come back up in roughly 30 seconds. 
