---
title: Running a Command on Boot
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 1
---

# Running a Command on Boot

This article will demonstrate how you can have your Omega run commands on boot. This can be used in a number of applications, such as showing a welcome message on the OLED Expansion when the Omega has booted or connecting to a server of your choosing, etc. The Omega can get commands to run on boot quite easily, so let's get started!


## Implementation

The Omega reads the commands to run on boot from the `/etc/rc.local` file. Type `vi /etc/rc.local` and you'll see the contents of the file:

```
# Put your custom commands here that should be executed once
# the system init finished. By default this file does nothing.

exit 0
```

Here we can see that the commands in this file will be executed after the system initialization, and that he only command being run is `exit 0`. Let's change that and get the RGB LED on the Expansion Dock to change colors on boot.

To do this, edit your `/etc/rc.local` file to look like this:

```
#!/bin/sh -e
# Put your custom commands here that should be executed once
# the system init finished. By default this file does nothing.

expled 0xff0000 && expled 0x00ff00 && expled 0x0000ff && sleep 5 && expled 0xff0000 && expled 0x00ff00 && expled 0x0000ff && expled 0x000000

exit 0
```

We started by adding `#!bin/sh -e`, known as a "Shebang". This instructs the program loader to run the script as a shell script.

The next thing we add is the command we want to run:

```
expled 0xff0000 && expled 0x00ff00 && expled 0x0000ff && sleep 5 && expled 0xff0000 && expled 0x00ff00 && expled 0x0000ff && expled 0x000000
```

This code will flash your Expansion Dock's LED red, then green, then blue, and just in case you miss it the first time, it'll cycle through once more after waiting for 5 seconds, and then shut off the LED.

Save and exit your file, and reboot your Omega to see the effects!


### Text Output

// give reason as to why you would want to see the output

When `/etc/rc.local` runs on boot, you won't be able to see any output from your file. You may need to see output for debugging purposes to see where your code is failing.

You can pipe the output of your command to a specific destination with a simple addition to your `/etc/rc.local` file.

The syntax for piping your command to a file is as follows:

```
<COMMAND> >> <<OUTPUT FILE>> 2>&1
```

// explain what 2>&1 means

To apply this to your command on boot, simply edit the `/etc/rc.local` file as such:

```
#!/bin/sh -e
# Put your custom commands here that should be executed once
# the system init finished. By default this file does nothing.

expled 0xff0000 && expled 0x00ff00 && expled 0x0000ff && sleep 5 && expled 0xff0000 && expled 0x00ff00 && expled 0x0000ff && expled 0x000000 >> /tmp/output.txt 2>&1

exit 0
```

This `/etc/rc.local` file actually runs multiple commands and only the last command, `expled 0x000000`, will have it's output piped to `/tmp/output.txt`

Looking at `/tmp/output.txt` we see:

```
Setting LEDs to: 000000
Duty: 100 100 100
> Set GPIO17: 1
> Set GPIO16: 1
> Set GPIO15: 1
```
and if we run the command `expled 0x000000` in the command line we should see the same output:

```
root@Omega-2757:/tmp# expled 0x000000
Setting LEDs to: 000000
Duty: 100 100 100
> Set GPIO17: 1
> Set GPIO16: 1
> Set GPIO15: 1
```

## Troubleshooting

If your commands don't seem to be working on boot, try copying them directly from your `/etc/rc.local` file and running them manually.
