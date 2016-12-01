---
title: Running a Command on a Schedule
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 2
---

# Running a Command on a Schedule

The Omega's firmware has a powerful built in feature, `cron`, that allows you to schedule commands to run at specified intervals. This tutorial will show you how to take advantage of `cron` to automate commands on your Omega.

This can be especially useful when you want to automate a project (e.g. a weather monitoring device that updates the OLED Expansion every hour with new information), and is incredibly easy to do.


## What is `cron`?

In computing terms, a daemon is a program that runs continuously in the background and answers requests from services. On the Omega, `cron` runs as a daemon and monitors the `crontab`, a file that lists commands that need to run at specified intervals. These commands can be programs, scripts, or anything that you can type in the command line.

To get started with `cron`, enter the following command on the command line from any directory:

```
crontab -e
```

If you've never before worked with `cron`, an empty file will show up. The first thing we need to do is figure out a command to run at an interval. Let's change the color of the LED on the Expansion Dock using `expled`. In the empty file enter the following:

```
#
*/1 * * * * expled 0xff0000 && expled 0x00ff00 && expled 0x0000ff && sleep 5 && expled 0xff0000 && expled 0x00ff00 && expled 0x0000ff && expled 0x000000
#
```

Save your and exit your file. The restart the `cron` daemon with the following command to apply the changes:

```
/etc/init.d/cron restart
```


This code will flash your Expansion Dock's LED red, then green, then blue, and just in case you miss it the first time, it'll do it once more after waiting for 5 seconds, and then shut off the LED. This can take up to 59 seconds to work because `cron` will wait for the next minute to run (e.g. 6:05:59, 6:06:00)


### `crontab` Syntax
So let's break down how `cron` will read the `crontab` file!

|min| hour | date |month |day of the week | When will my command run? |
|*/1 | * | * | * | * | Once every minute |
|12 | */3 | * | * | * | Every 3 hours at 12 minutes (8:12, 9:12, 10:12, etc) |
|24 | 6 | 12 | 2,3,4 | * | At 6:24 on the 12th of February, March, and April |
|0 | 0 | 3,8,17 | * | * | At midnight on 3rd, 8th and 17th of every month |

*NOTE: For days of the week, `cron` treats `0` as `Sunday` and setting days of the week to `7` will make you command run every day.*


**Your `crontab` file must end with the last line as a comment for it to run**

For more information on `cron` including more rules and references you can check out [OpenWRT's guide to Cron](https://wiki.openwrt.org/doc/howto/cron).

### Saving Output of a `cron` Job to a File
// TODO: change the header title

When `cron` runs, you won't be able to see any output from your file. You can modify your script or program to save all output to a file rather than print it in the command line, or you can pipe the output of your command to a specific destination with a simple addition to your `crontab` file.

The syntax for piping your command to a file is as follows:

```
<COMMAND> >> <<OUTPUT FILE>> 2>&1
```

You can apply this to a `cron` command quite easily.

Enter the `crontab` with:

```
crontab -e
```

and edit the command whose output you want to pipe.

From the earlier example, that would look like:

```
#
*/1 * * * * expled 0xff0000 && expled 0x00ff00 && expled 0x0000ff && sleep 5 && expled 0xff0000 && expled 0x00ff00 && expled 0x0000ff && expled 0x000000 >> /tmp/output.txt 2>&1
#
```

This `cron` job actually runs multiple commands and only the last command `expled 0x000000` will have it's output piped to `/tmp/output.txt`

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

* Remember to end your `crontab` file with a comment, or it won't run.
* If your command involves rebooting your Omega please check out this [solution for rebooting with cron](https://wiki.openwrt.org/doc/howto/cron#periodic_reboot_of_a_router) provided by the OpenWRT wiki.
