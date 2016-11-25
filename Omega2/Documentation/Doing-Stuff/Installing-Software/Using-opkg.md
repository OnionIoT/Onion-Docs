---
title: Using opkg
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 1
---


# What is OPKG?

Opkg is the package manager for the Omega Firmware. Installation and removal of packages available to the Omega Firmware is made simple using opkg.

# How to use the Package Manager

The basic operation of the package manager involves updating opkg and either installing or removing particular packages.

## The Importance of `opkg update`

Running opkg update, provides the most recent list of packages available from the firmware Repos as well as their respective checksums. The latter is to ensure the integrity and security of the package being downloaded and installed.

To update opkg, run:

```
opkg update
```

## Installing Packages

To install a package simply use the opkg command:

```
opkg install package_name
```

## Removing Packages

To remove a package:

```
opkg remove package_name
```

## Help With Opkg

To see the opkg usage, run:

```
opkg -h
```