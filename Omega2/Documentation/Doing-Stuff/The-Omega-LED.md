---
title: The Omega's LED
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 2
---

## The Omega's LED {#the-omega-led}


The Omega comes equipped with an LED that has a number of uses, namely as an indication for when your Omega has finished booting.
This tutorial will show you other cool things you can do with the LED.

![Omega LED](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/unbox-6-omega-led-detail.jpg "Omega's LED")

To control the Omega's LED, we are going to be writing to files that are used to specify values for the LED, such as the LED mode. This is made possible with `sysfs`, a pseudo file system that holds information about the Omega's hardware in files, and lets the user control the hardware by editing the files.

### The LED's Name

The Omega's LED is named in the filesystem according to the LEDE style guide:

| Device  | LED Name               |
|---------|------------------------|
| Omega2  | `omega2:amber:system`  |
| Omega2+ | `omega2p:amber:system` |

The `sysfs` interface for the LED can be found in a directory named after the LED at `/sys/class/leds`

| Device  | Location                                  |
|---------|-------------------------------------------|
| Omega2  | `/sys/class/leds/omega2\:amber\:system/`  |
| Omega2+ | `/sys/class/leds/omega2p\:amber\:system/` |

**Note the difference in name and path between the Omega2 and Omega2+, keep this in mind when using the commands below!**


### LED Trigger Modes

The LED has various modes known as "triggers" that change the behavior of the LED. For example, when your Omega is booting, it's in a flashing mode, and when it has booted, it's in an "on" mode.


The current LED trigger mode can be read by looking at the file that controls the LEDs. Enter:

```
cat /sys/class/leds/omega2\:amber\:system/trigger
```

>Remember, if you're using an Omega2+, the LED will be named `omega2p:amber:system` as opposed to `omega2:amber:system` so you will have to pipe the above command to `/sys/class/leds/omega2p\:amber\:system/trigger`

and your terminal will output something similar to the following:
```
root@Omega-2757:/# cat /sys/class/leds/omega2\:amber\:system/trigger
none mmc0 timer [default-on] netdev transient gpio heartbeat morse oneshot
```

The current mode is indicated by the brackets. My Omega's LED is currently set to the `default-on` mode. Let's try changing the trigger by editing the file.


#### The Heartbeat Trigger Mode


To do this, we're going to echo a string, in this case the trigger mode, and pipe it into the file using this command:

```
echo heartbeat > /sys/class/leds/omega2\:amber\:system/trigger
```

> A pipe in Linux is used to send some output to a program for further processing
> In this case, we are using the ">" to overwrite the contents of the file located at /sys/class/leds/omega2\:amber\:system/trigger
> Another example is using ">>" to append an output to a file.


When you execute this command, your shell actually writes the word `heartbeat` to the file, and the kernel passes the message to the corresponding handlers.

Your Omega's LED should start blinking like a heartbeat now.

![upload-file-button](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/heartbeat.gif)


Let's experiment with other triggers!

#### The Timer Trigger Mode

The `timer` trigger blinks the LED on and off for specified amounts of time. You can set the trigger to timer with the following command:

```
echo timer > /sys/class/leds/omega2\:amber\:system/trigger
```

Now, you can set the `delay_on` and the `delay_off` values, which specify how long the LED remains on and off in milliseconds.

For a rapidly blinking LED you can enter these two commands:

```
echo 75 > /sys/class/leds/omega2\:amber\:system/delay_on
echo 75 > /sys/class/leds/omega2\:amber\:system/delay_off
```
![upload-file-button](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/rapid-blink.gif)

For an LED that stays on for longer than it's off, enter these two commands:

```
echo 500 > /sys/class/leds/omega2\:amber\:system/delay_on
echo 120 > /sys/class/leds/omega2\:amber\:system/delay_off
```
![upload-file-button](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/slow-fast-blink.gif)

Feel free to experiment with other combinations.

#### The Morse Trigger Mode

A really interesting trigger mode is `morse`, which converts a message from text to morse code!


First, set the trigger to morse:

```
echo morse > /sys/class/leds/omega2\:amber\:system/trigger
```

Then, enter a message you want to convert to morse code:

```
echo <YOUR MESSAGE HERE> > /sys/class/leds/omega2\:amber\:system/message
```

You can try the classic `S O S` which looks like 3 quick blinks, 3 slow blinks, and then 3 quick blinks again:

```
echo sos > /sys/class/leds/omega2\:amber\:system/message
```

My LED is blinking really quickly, and it's hard to read. Let's change the speed of the message with the following command:
![upload-file-button](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/sos-fast.gif)

```
echo 150 > /sys/class/leds/omega2\:amber\:system/delay
```

That slowed it down nicely.

![upload-file-button](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/sos-slow.gif)
