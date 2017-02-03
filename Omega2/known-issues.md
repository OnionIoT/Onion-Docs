## Known Firmware Issues {#known-firmware-issues}

This page lists all of the currently identified issues in the Omega OS. The issues are separated into general firmware issues and Console firmware issues.

### Issue Listing

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
* The `fast-gpio` program always crashes
    * Root Cause: the firmware does not expose the `/dev/mem` device which allows access to the memory map
    * Status: Investigating
* WiFi Issues
    * No automatic support for TKIP-encrypted WiFi networks
        * See [this post](https://community.onion.io/topic/1149/omega2-fails-to-connect-to-wifi/25) on the Onion Community for an interim, manual fix
        * Status: expect a fix in late January
    * No support for enterprise WiFi that requires a username and password
        * Status: expect a fix in February
    * No automatic support for WiFi channels 13 and 14
        * Status: expect a fix early February


### Console Issue Listing

* Cannot change the account password in the Settings app
* Cannot disable the WiFi AP
* The OLED App doesn't properly save image files to the Omega
