## Known Firmware Issues {#known-firmware-issues}

This page lists all of the currently identified issues in the Omega OS. The issues are separated into general firmware issues and Console firmware issues.

### Issue Listing

* Cannot flash Arduino Dock if `arduino-dock-2` is installed when [LEDE package repos are active](#using-opkg-switch-to-lede-repos)
    * Root Cause: 
        * The LEDE repo has `avrdude` version 6.3, which has a bug that prevents access to GPIOs, so the microcontroller cannot be flashed
    * Resolution: 
        * The Onion repos have `avrdude` version 6.1 which works
        * Option 1: Install `arduino-dock-2` before enabling the LEDE package repos
        * Option 2: If already installed, run `opkg remove avrdude`, deactivate the LEDE package repos by commenting them out in `/etc/opkg/distfeeds.conf`, run `opkg update`, then install again but from the Onion repo: `opkg install avrdude`
* ~~The Omega cannot successfully connect to the Onion Cloud~~
    * Status: **Fixed** in b149
* ~~The reset button does not work~~
    * Status: **Fixed** in b146
* ~~Omega2+ cannot reboot~~
    * Status: **Fixed** in b142
* ~~Omega2+ cannot mount MicroSD cards~~
    * Status: **Fixed** in b143
* ~~Cannot successfully register a 1-Wire master in the filesystem~~
    * Status: **Fixed** in b151
* ~~The `fast-gpio` program always crashes~~
    * Root Cause: the firmware does not expose the `/dev/mem` device which allows access to the memory map
    * Status: **Fixed** in b160
* WiFi Issues
    * No automatic support for TKIP-encrypted WiFi networks
        * See [this post](https://community.onion.io/topic/1149/omega2-fails-to-connect-to-wifi/25) on the Onion Community for an interim, manual fix
        * Status: expect a fix in March
    * No support for enterprise WiFi that requires a username and password
        * Status: expect a fix in March
    * No automatic support for WiFi channels 13 and 14
        * Status: expect a fix in March


### Console Issue Listing

* Cannot change the account password in the Settings app
* Cannot disable the WiFi AP
* The OLED App doesn't properly save image files to the Omega
