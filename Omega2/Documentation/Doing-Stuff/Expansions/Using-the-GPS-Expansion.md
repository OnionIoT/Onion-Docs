---
title: Using the GPS Expansion
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 2
---

## Using the GPS Expansion {#using-gps-expansion}


The GPS expansion from Onion features a ublox neo GPS module, which allows seamless integration into your Omega projects. This Expansion outputs GPS data in the form of NMEA messages, which include all relevant information (latitude, longtitude, etc). We have prepared a package called `ogps` to handle the NMEA messages and offer up the relevant information to the user via `ubus` calls in the command-line.

### Reading the Raw Output of the GPS Expansion

The device driver will already be installed and Linux should recognize the device automatically. To double check, run the following command.

```
ls /dev/ttyACM*
```

![checking for device](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/using-gps-expansion-1-ls.png)

You should see a device called "ttyACM0". This is our GPS expansion.

At this point you can read the raw output of the GPS using `cat`:

```
cat /dev/ttyACM0
```

And you'll see something that looks like the following:

![nmea output](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/using-gps-expansion-2-nmea.png)

This is the NMEA output, and it's quite hard to read. Luckily we've got a utility that will translate this data into useful information.


### Reading NMEA Data Using `ogps`

You can also use `ogps` to access relevant data offered up by the GPS via `ubus` calls. To install `ogps` enter the following commands.

```
opkg update
opkg install opgs
```

![opkg installation](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/using-gps-expansion-3-opkg-install.png)

You can now access the GPS information through `ubus`. To make sure the `gps` service has initialized, run the following command, which will list all the available `ubus` services:

```
ubus list
```

You should see the `gps` service listed:

![ubus list](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/using-gps-expansion-4-ubus-list.png)


If you don't see `gps` listed, you'll need to restart your `rpcd` service in order to refresh the list:

```
/etc/init.d/rpcd restart
```

If this doesn't work, try reinstalling the `ogps` package by running the following commands:

```
opkg remove ogps
opkg update
opkg install ogps
```

### Usage

First, make sure your GPS Expansion is connected! Then, to access the data you'll need to `call` the correct service with the following command:

```
ubus call gps info
```

If the GPS is not locked, the command will return `signal=false`. In this case you may need to give the GPS more time to lock onto a satellite; try it again after 10 seconds. If this still doesn't work, you will need to move to a more open area where the GPS Expansion can see more satellites.

>You may need to go outside in order to lock the GPS signal.

Otherwise you should have an output that looks like this.

![ubus call success](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/using-gps-expansion-5-ubus-success.png)


>Note: If you've used the GPS Expansion with the Omega1, you may remember some hardware stability issues regarding the GPS Expansion. This is no longer the case with the Omega2 and Omega2+.
