---
title: Running a Command on Boot
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 1
---

## Running a Command on Boot {#running-a-command-on-boot}

This article will demonstrate how you can have your Omega run commands right when it finishes booting. This can be used in a number of applications, such as showing a welcome message on the OLED Expansion when the Omega has booted or connecting to a server of your choosing, etc. The Omega can be set up to run commands on boot quite easily, so let's get started!


### Implementation

We're going to start by writing a script that will perform the actions we would like to have happen on every boot. If you already have a script or a command you'd like to run on boot you can skip the "Writing a Shell Script" step.

#### Writing a Shell Script

Let's create our script in the `/root` directory and call it `rgb-led.sh`:

```
vi /root/rgb-led.sh
```

> The /root directory is the best place to put your projects to ensure they don't get deleted when you update the firmware.
<!-- For more on updating the Omega you can read our [Guide to Updating the Omega](#updating-the-omega) -->

Now let's write a small shell script that will flash your Expansion Dock's RGB LED red, then green, then blue, and just in case you miss it the first time, it'll do it once more after waiting for 5 seconds, and then shut off the RBG LED.

Here's what that looks like:

```
#!/bin/sh -e
expled 0xff0000 #Red
expled 0x00ff00 #Green
expled 0x0000ff #Blue
sleep 5 #wait five seconds
expled 0xff0000 #Red
expled 0x00ff00 #Green
expled 0x0000ff #Blue
expled 0x000000 #Off
```

Copy the above code into your file, then save and exit the file:

Next, from your command-line, enter the following:

```
chmod +x /root/rgb-led.sh
```

The command above will change the execution permissions of the file and allow your script to be executed by entering `/root/rgb-led.sh`.

> Alternatively, the script can be run by entering `sh /root/rgb-led.sh`, note that this will work without changing the file's execution permissions. However, it's sometimes handy to be able to run a script by just typing the filename.


#### Editing the `/etc/rc.local` File

The `/etc/rc.local` file is a script that will be executed automatically by the system once the boot sequence is complete.

**When your Omega boots, it will read commands from the `/etc/rc.local` file, and execute them.**

 Type `vi /etc/rc.local` and you'll see the contents of the file:

```
# Put your custom commands here that should be executed once
# the system init finished. By default this file does nothing.

exit 0
```

Here we can see that the commands in this file will be executed after the system initialization, and that he only command being run is `exit 0`. Let's change that and get the RGB LED on the Expansion Dock to change colors on boot.

To do this, edit your `/etc/rc.local` file to look like this:

```
# Put your custom commands here that should be executed once
# the system init finished. By default this file does nothing.

sh /root/rgb-led.sh

exit 0
```

We've added the command we want to run:

```
sh /root/rgb-led.sh
```

Save and exit your file, and reboot your Omega to see the effects!


#### Saving the Output of your `rc.local` Commands (Optional)

When `/etc/rc.local` runs on boot, you won't be able to see any output from your file. You may need to see output for debugging purposes to see where your code is failing.

You can pipe the output of your command to a specific destination with a simple addition to your `/etc/rc.local` file.

The syntax for piping your command to a file is as follows:

```
<COMMAND> >> <OUTPUT FILE> 2>&1
```

> The `>>` appends the output of your command to the output file. You can use `>` to overwrite the output instead. The `2>&1` is an indicator to the shell script that you want to include the error messages into the output of your command. By default, only standard output is piped.


To apply this to your command on boot, simply edit the `/etc/rc.local` file as such:

```
# Put your custom commands here that should be executed once
# the system init finished. By default this file does nothing.

sh /root/rgb-led.sh >> /tmp/output.txt 2>&1

exit 0
```

Looking at `/tmp/output.txt` we see:

```
Setting LEDs to: ff0000
Duty: 0 100 100
> Set GPIO16: 1
> Set GPIO15: 1
Setting LEDs to: 00ff00
Duty: 100 0 100
> Set GPIO17: 1
> Set GPIO15: 1
Setting LEDs to: 0000ff
Duty: 100 100 0
> Set GPIO17: 1
> Set GPIO16: 1
Setting LEDs to: ff0000
Duty: 0 100 100
> Set GPIO16: 1
> Set GPIO15: 1
Setting LEDs to: 00ff00
Duty: 100 0 100
> Set GPIO17: 1
> Set GPIO15: 1
Setting LEDs to: 0000ff
Duty: 100 100 0
> Set GPIO17: 1
> Set GPIO16: 1
Setting LEDs to: 000000
Duty: 100 100 100
> Set GPIO17: 1
> Set GPIO16: 1
> Set GPIO15: 1
```

and if we run our script `/root/rgb-led.sh` in the command line we should see the same output:

```
root@Omega-2757:/# sh /root/rgb-led.sh
Setting LEDs to: ff0000
Duty: 0 100 100
> Set GPIO16: 1
> Set GPIO15: 1
Setting LEDs to: 00ff00
Duty: 100 0 100
> Set GPIO17: 1
> Set GPIO15: 1
Setting LEDs to: 0000ff
Duty: 100 100 0
> Set GPIO17: 1
> Set GPIO16: 1
Setting LEDs to: ff0000
Duty: 0 100 100
> Set GPIO16: 1
> Set GPIO15: 1
Setting LEDs to: 00ff00
Duty: 100 0 100
> Set GPIO17: 1
> Set GPIO15: 1
Setting LEDs to: 0000ff
Duty: 100 100 0
> Set GPIO17: 1
> Set GPIO16: 1
Setting LEDs to: 000000
Duty: 100 100 100
> Set GPIO17: 1
> Set GPIO16: 1
> Set GPIO15: 1
```

You can go back into the `/etc/rc.local` file and comment out the line that runs the script to stop the Expansion Dock RGB LED from blinking.

### Troubleshooting

If your commands don't seem to be working on boot, try copying them directly from your `/etc/rc.local` file and running them manually.

#### Infinite Loop Code

If your command runs continuously and never reaches the `exit 0` line in the `/etc/rc.local` file, then your Omega will not successfully finish it's boot sequence. To avoid this scenario, make sure you fork the process by adding an ampersand to the end of the command:

```
<YOUR COMMAND TO RUN> &
```
