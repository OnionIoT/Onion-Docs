## Device MAC Addresses {#mac-address}

The Omega2, being an IoT Computer, is a connectivity device. Here we'll discuss the Omega2's MAC addresses, how they're allocated, how to read them, and how to programmatically generate a unique ID based on them.

> A MAC (Media Access Control) address is a unique, 6-byte identifier assigned to network interface controllers. Devices with multiple network interfaces must have a unique MAC address for each interface.

### MAC Address Allocation

Every Omega2 device is allocated **three** sequential MAC address during production, one for each of the available network interfaces:

* `ra0` – the WiFi Access Point interface – this matches the MAC address on the sticker on the shielding
* `eth0` – ethernet port
* `apcli0` – the WiFi *client* interface

The `ra0` MAC address matches the MAC address that is printed on the device's shielding. The other two MAC addresses are sequential: 

* The `eth0` MAC address is the `ra0` MAC address + `0x01`
* The `apcli0` MAC address is the `ra0` MAC address + `0x02`

### Reading the MAC Address

The `iwpriv` command can be used to access the wireless driver parameters, among these parameters are the MAC addresses. 

[Connect to the Omega's command line](#connecting-to-the-omega-terminal) and run the following command:

```
iwpriv ra0 e2p
```

It will output quite a bit of data:

![read mac address](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/mac-address-read-iwpriv.png)

We're interested in:

* The 6 bytes starting at `0x0004` - the `ra0` MAC address
* The 6 bytes starting at `0x0028` - the `eth0` MAC address
* The 6 bytes starting at `0x002e` - the `apcli0` MAC address

Take a look at how these address map to the network interfaces by running the `ifconfig` command:

![mac address to interface mapping](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/mac-address-to-interface.png)


### Programmatically Generate a Unique ID based on the Device's MAC Address

When working with IoT devices, it's always useful when an ID that's unique to each device can be generated with the same code. And what better to use than the device's own MAC address.

To illustrate the process, consider a shell script named `macId.sh`. The shell script will create and output a unique ID based on the Omega's `ra0` MAC address:

```
#!/bin/sh

## Generate UID based on device's MAC addr for ra0 intf

generateMacUid () {
        # grab line 2 of iwpriv output
        line1=$(iwpriv ra0 e2p | sed -n '2p')
        # isolate bytes at addresses 0x0004 and 0x0006, and perform byte swap
        bytes5432=$(echo $line1 |  awk '{print $3":"$4}' | awk -F ":" '{print substr($2,3) substr($2,1,2) substr($4,3) substr($4,1,2)}')

        # grab line 3 of iwpriv output
        line2=$(iwpriv ra0 e2p | sed -n '3p')
        # isolate bytes at address 0x0008 and perform byte swap
        bytes10=$(echo $line2 | awk '{print $1}' | awk -F ":" '{print substr($2,3) substr($2,1,2)}')

        macId=$(echo ${bytes5432}${bytes10})
        echo $macId
}

uid=$(generateMacUid)
echo "Unique ID based on MACD for this device is: $uid"
```

When run on the device:

```
root@Omega-2013:~# sh macId.sh                                                              
Unique ID for this device is: 40A36BC32013
```

Feel free to translate this code to other languages and use it in your own applications.
