## Linux for OMEGA Beginners {#linux-for-omega-beginners}

If you have your Omega in hand and have no experience with Linux, this tutorial will walk you through all the big topics, hopefully giving you some context

By the end of this tutorial, users should be comfortable with some of the Omega's built in functionality as well as getting started with their own projects.


#### What Is Linux?

Linux is an operating system (OS) similar to Windows or MacOS in that it allows you to operate the hardware of your computer without too much effort. Linux is different in that it's much more modular. In fact, 'Linux' technically just refers to the Linux kernel - a low level programming interface allowing software to use the hardware in a uniform way. Like its counterparts, Windows and MacOS, the Linux Kernel provides the software bridge between applications and hardware processes. Unlike Windows or MacOS however, the Kernel doesn't do much beyond that - it doesn't even come with a GUI.

Instead, there are developers who take the Linux kernel and build fully functional GUI-based systems around it. Some examples you may have heard of include Ubuntu, Fedora, and Arch. These fully featured operating systems are commonly referred to as distributions, or 'distros'.

The reason this kind of development happen on top of Linux is because Linux is mostly Open Source. This means that no one company or source is responsible for the development of Linux and anyone can use it to build their own OS. In fact, anyone can submit patches to the Linux kernal or contribute to a free and open source distro. There's a strong spirit of DIY in the Linux community. Often exciting and powerful new software is created just because someone with free time decided the existing tools aren't good enough. Check out this [article](https://www.linux.com/learn/new-user-guides/376-linux-is-everywhere-an-overview-of-the-linux-operating-system) for a more extensive read on Linux. Linux comes in many distributions/distros (versions) each tailored to serve particular applications.

The Omega runs a distro called LEDE.

#### What's LEDE?

The OMEGA runs LEDE. LEDE is a distribution designed to be run on a router - or any other low power device intended to communicate through the internet (sound familiar?).  The reason we chose LEDE is because it supports a ton of sofware specifically made for embedded devices. Additionally, due to the distribution being designed for use on embedded devices, it  In the interest of being memory efficient, OpenWRT doesn't come with all of the packages found on a larger distribution such as Ubuntu and available packages may have functionality stripped down.
LEDE is a **fork** of OpenWRT, a distribution inteneded for similar purposes.


For now we will move onto using OpenWRT on the Omega, but we do encourage users to further peruse the OpenWRT wiki which can be found [here](https://wiki.openwrt.org/).



Next, we will move onto introducing users to the [Command Line Interface](#the-command-line-interface).
