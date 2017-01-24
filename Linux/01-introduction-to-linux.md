## Linux for Omega Beginners {#linux-for-omega-beginners}

If you have your Omega in hand and have no experience with Linux, this tutorial will walk you through all the big topics, hopefully giving you some context

By the end of this tutorial, users should be comfortable with some of the Omega's built in functionality as well as getting started with their own projects.


### What Is Linux?

Linux is an operating system (OS) similar to Windows or MacOS in that it allows you to operate the hardware of your computer without too much effort. Linux is different in that it's much more modular. In fact, 'Linux' technically just refers to the Linux kernel - a low level programming interface allowing software to use the hardware in a uniform way. Like its counterparts, Windows and MacOS, the Linux Kernel provides the software bridge between applications and hardware processes. Unlike Windows or MacOS however, the Kernel doesn't do much beyond that - it doesn't even come with a GUI.

Instead, there are developers who take the Linux kernel and build fully functional GUI-based systems around it. Some examples you may have heard of include Ubuntu, Fedora, and Arch. These fully featured operating systems are commonly referred to as distributions, or 'distros'.

The reason this kind of development happen on top of Linux is because Linux is mostly Open Source. This means that no one company or source is responsible for the development of Linux and anyone can use it to build their own OS. In fact, anyone can submit patches to the Linux kernal or contribute to a free and open source distro. There's a strong spirit of DIY in the Linux community. Often exciting and powerful new software is created just because someone with free time decided the existing tools aren't good enough. Check out this [article](https://www.linux.com/learn/new-user-guides/376-linux-is-everywhere-an-overview-of-the-linux-operating-system) for a more extensive read on Linux. Linux comes in many distributions/distros (versions) each tailored to serve particular applications.

The Omega runs a distro called LEDE.

### What's LEDE?

The OMEGA runs LEDE. LEDE is a distribution designed to be run on a router - or any other low power device intended to communicate through the internet (sound familiar?).  The reason we chose LEDE is because it supports a ton of software specifically made for embedded devices. More importantly: LEDE is built to be tiny, weighing in at just under 4MB. This means you can fit more software into the Omega. The tradeoff of course, is you may not find the tools you need on the Omega out of the box, and more powerful software may not be available at all.

LEDE is a **fork** of OpenWRT, because of its history, 'most of the operational aspects of the two projects are identical' - from the LEDE Project [website](https://lede-project.org/docs/guide-quick-start/start). This means, that in addition to referencing the LEDE Project [documentation](https://lede-project.org/docs/start), the OpenWRT Project [documentation](http://wiki.openwrt.org/doc/start) is also a good source of tutorials and guides.

In the [next section](#the-command-line-interface), we'll be doing a tour of the most powerful tool in the Linux arsenal - the command line.
