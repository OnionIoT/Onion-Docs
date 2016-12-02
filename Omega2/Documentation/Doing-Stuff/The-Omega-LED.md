---
title: The Omega's LED
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 2
---

# The Omega's LED

// how to control the Omega's LED
// write me pls!

// explanation of the sysfs interface - using the filesystem to control hardware, clever abstraction

// seeing the current led trigger - make this into a subheading
The current led trigger can be read by looking at the file that controls the leds. Enter:

```
cat /sys/class/leds/onion\:amber\:system/trigger
```

and your terminal will output something similar to the following:
```
root@Omega-2757:/# cat /sys/class/leds/onion\:amber\:system/trigger
none mmc0 timer [default-on] netdev transient gpio heartbeat morse oneshot
```

The current mode is indicated by the brackets. My Omega's LED is currently set to the `default-on` mode. Let's try changing the trigger by editing the file.

// add subheading here
To do this, we're going to echo a string, in this case the trigger mode, and pipe it into the file using this command:

```
echo heartbeat > /sys/class/leds/onion\:amber\:system/trigger
```

>// subsection on piping
> mention overwrite > and append >>


When you execute this command, your shell actually writes the word `heartbeat` to the virtual file, and the kernel passes the message to the corresponding handlers. //somehow throw sysfs into the mix here

Your Omega's LED should start blinking like a heartbeat now. Let's experiment with other triggers!
// setting the led trigger
//  - explain echo "blah" and piping that (look at the linux and openwrt basics articles)


// show example of setting it to timer and changing the delay - add subsection

The `timer` trigger blinks the LED on and off for specified amounts of time. You can set the trigger to timer with the following command:

```
echo timer > /sys/class/leds/onion\:amber\:system/trigger
```

Now, you can set the `delay_on` and the `delay_off` values, which specify how long the LED remains on and off in milliseconds.

For a rapidly blinking LED you can enter these two commands:

```
echo 75 > /sys/class/leds/onion\:amber\:system/delay_on
echo 75 > /sys/class/leds/onion\:amber\:system/delay_off
```

For an LED that stays on for longer than it's off, enter these two commands:

```
echo 500 > /sys/class/leds/onion\:amber\:system/delay_on
echo 120 > /sys/class/leds/onion\:amber\:system/delay_off
```

Feel free to experiment with other combinations.

// subesction
A really interesting trigger mode is `morse`, which converts a message from text to morse code!


First, set the trigger to morse:

```
echo morse > /sys/class/leds/onion\:amber\:system/trigger
```

Then, enter a message you want to convert to morse code:

```
echo <YOUR MESSAGE HERE> > /sys/class/leds/onion\:amber\:system/message
```

You can try the classic `S O S` which looks like 3 quick blinks, 3 slow blinks, and then 3 quick blinks again:

```
echo sos > /sys/class/leds/onion\:amber\:system/message
```

My LED is blinking really quickly, and it's hard to read. Let's change the speed of the message with the following command:

```
echo 150 > /sys/class/leds/onion\:amber\:system/delay
```

That slowed it down nicely.

// show example of setting it to morse code, setting a message, changing the delay

// overall: include notes of where it would be useful to have gifs


// use https://www.lede-project.org/docs/user-guide/led_configuration?s[]=led&s[]=configuration#led_triggers for reference - link to this guy as well
