## OctoPrint 3D Printing Server {#3d-print-server}

Instead of connecting directly to our 3D printer, we can have the Omega serve up a web interface with Octoprint to connect to our printer from any device in our Local Area Network.

// TODO: download these photos, include them in the repo and link to them from the repo

![](https://community.onion.io/uploads/files/1486487035483-img_20170206_133518.jpeg)
![](https://community.onion.io/uploads/files/1486486915332-screen-shot-2017-02-07-at-12.04.00-pm.png)

### Overview

**Skill Level:** Intermediate

**Time Required:** 30 minutes

To get our printer server up and running, we'll have to use some packages from the LEDE repository. Additionally, we're going to build a custom version of OctoPrint to fix some compatibility issues.

### Ingredients


1. Onion Omega2+
1. Any Onion Dock that can safely power the Omega
1. 3D Printer that is [supported by Octoprint](https://github.com/foosel/OctoPrint/wiki/Supported-Printers)
1. USB cable to connect the Omega and 3D printer

### Step-by-Step

Follow these instructions to turn your 3D printer wireless!

<!-- // each step should be simple -->

#### 1. Set up the hardware

Here's a handy connection diagram of the way the pieces are put together:

![](https://community.onion.io/uploads/files/1486496031636-3d-printer-haredare-setup-1.png)

First, connect the printer to the Omega with a USB cable. Next, connect the 3D printer to power. Finally, power on the Omega and we'll be good to go.

#### 2. Prepare the Omega

If you need, complete the [First Time Setup Guide](https://docs.onion.io/omega2-docs/first-time-setup.html) to connect your Omega to WiFi and update to the latest firmware.


#### 3. Expand Omega storage with SD card

To install Octoprint, you will have to first expand the storage on the Omega2+.
First, plug a micro SD card into the Omega2+, it will show up as `/dev/mmcblk0`

To make it useable, we'll have to format the SD card to EXT4 (you can skip this if you already have you sd card in EXT4 format).

Install disk utilities:

```
opkg update
opkg install fdisk e2fsprogs block-mount
```

Next, partition the SD card to Linux partition using [fdisk](http://www.tldp.org/HOWTO/Partition/fdisk_partitioning.html)

Once that's done, format the SD card:

```
umount /dev/mmcblk0p1
mkfs.ext4 /dev/mmcblk0p1
```

Mount the SD card in a more legible location:

```
umount /dev/mmcblk0p1
mkdir /mnt/SD
mount /dev/mmcblk0p1 /mnt/SD
```

Copy current `/overlay` directory:

```
tar -C /overlay -cvf - . | tar -C /mnt/SD/ -xf -
umount /mnt/SD
```

Now we'll set up the `/overlay` directory to automount on startup. First, we'll copy our current setup to the filesystem record:

```
block detect > /etc/config/fstab
```

Next, we edit `/etc/config/fstab` to tell the Omega where the operating system is.

To do this, we'll change `option target '/mnt/mmcblk0p1'` to `option target '/overlay'`.

And `option enabled '0'` to `option enabled '1'`.

Reboot for our changes to take effect.

After the Omega starts again, you can verify if you /overlay is mounted properly by running `df`.

You should see something like this:

```
/dev/mmcblk0p1         7374776     33328   6947108   0% /overlay
```


#### 4. Build Octoprint

Octoprint requires some packages that are not in the Onion repository, so we'll pull them from the LEDE repo instead.

To do so, we need to edit `/etc/opkg/distfeeds.conf` and uncomment this line:

```
src/gz reboot_packages http://downloads.lede-project.org/snapshots/packages/mipsel_24kc/packages
```

Once done, we can install the packages we need:

```
opkg update
opkg install python python-pip unzip
pip install --upgrade setuptools
```

Now we need to expand `/tmp` folder on the Omega:

```bash
mkdir /overlay/tmp
rm -rf /overlay/tmp/*
cp -a /tmp/* /overlay/tmp/
umount /tmp
[ $? -ne 0 ] && {
umount -l /tmp
}
mount /overlay/tmp/ /tmp
```

Once we have the packages and enough space, we can download and build Octoprint:

```
cd /root
wget https://github.com/foosel/OctoPrint/archive/1.0.0.zip
unzip 1.0.0.zip
cd OctoPrint-1.0.0
pip install -r requirements.txt
```

>Note: Currently we're only able to get Octoprint 1.0.0 to work

Now we need to edit a few files to resolve some compatibility issues.

Unicode is going to cause problem with Python on Omega2. we have to replace the unicode author name to ascii ( Sorry Gina Häußge :p )


```
s/Häußge/H\./g
sed -i 's/Häußge/H\./g' /root/OctoPrint-1.0.0/src/octoprint/util/comm.py
sed -i 's/Häußge/H\./g' /root/OctoPrint-1.0.0/src/octoprint/util/virtual.py
```

Omega only have one user and that is root. Octoprint does not let you run as root so we have to suppress that

```
sed -i 's/exit("You should not run OctoPrint as root!")/pass/g' /root/OctoPrint-1.0.0/src/octoprint/server/__init__.py
```

That's it! Now we can test drive our Octoprint Installation:

```
./run
```

Open a browser, connect to your Omega through port `5000`.


#### 5. Auto start Octoprint at startup

Move OctoPrint to a proper location:

```
mv /root/OctoPrint-1.0.0 /usr/share/OctoPrint
```

Make a symlink to the start up binary:

```
ln -s /usr/share/OctoPrint/run /usr/bin/octoprint
```

Edit `/etc/rc.local` add the following before `exit 0`:

```
octoprint &
```

And bam, we're golden.
