## Known Firmware Issues {#known-firmware-issues}

This page lists all of the currently identified issues in the Omega OS. The issues are separated into general firmware issues and Console firmware issues.

### Issue Listing

* Cannot flash Arduino Dock if `arduino-dock-2` is installed when the [OpenWRT package repos are active](#using-opkg-switch-to-lede-repos)
    * Root Cause: 
        * The OpenWRT repo has `avrdude` version 6.3, which has a bug that prevents access to GPIOs, so the microcontroller cannot be flashed
    * Resolution: 
        * The Onion repos have `avrdude` version 6.1 which works
        * Option 1: Install `arduino-dock-2` before enabling the OpenWRT package repos
        * Option 2: If already installed:
            * Run `opkg remove avrdude`
            * Deactivate the OpenWRT package repos by commenting them out in `/etc/opkg/distfeeds.conf` (essentially follow [these instructions](#using-opkg-switch-to-lede-repos) in reverse)
            * Run `opkg update`
            * Install again but from the Onion repo: `opkg install avrdude`
                * If this doesn't work, reboot your device and try again
* ~~The Omega cannot successfully connect to the Onion Cloud~~
    * Status: ~~**Fixed** in b149~~ Onion Cloud was [decommissioned in October 2018](https://onion.io/onion-cloud-end-of-life-notice/)
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
    * No support for enterprise WiFi that requires a username and password
        * Status: not currently supported with Onion WiFi Warp Core driver
    * ~~No automatic support for TKIP-encrypted WiFi networks~~
        * ~~See [this post](https://community.onion.io/topic/1149/omega2-fails-to-connect-to-wifi/25) on the Onion Community for an interim, manual fix~~
        * Status: **Fixed** in firmware v0.2.0 and up with release of Onion WiFi Warp Core driver. See [related blog post](https://onion.io/2bt-brand-new-os-release/) for more details. 
    * ~~No automatic support for WiFi channels 13 and 14~~
        * Status:  **Fixed** in firmware v0.2.0 and up with release of Onion WiFi Warp Core driver (see [related blog post](https://onion.io/2bt-brand-new-os-release/) for more details). 
          * To enable channels 13 and 14, open `/etc/config/wireless`, change the `country` option to your country (assuming it supports channels 13 and 14), and restart the WiFi interface by running `wifi`


### Console Issue Listing

* Cannot change the account password in the Settings app
* Cannot disable the WiFi AP
* The OLED App doesn't properly save image files to the Omega
