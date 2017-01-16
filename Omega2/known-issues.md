## Known Firmware Issues {#known-firmware-issues}

This page lists all of the currently identified issues in the Omega OS. The issues are separated into general firmware issues and Console firmware issues.

### Issue Listing

* The Omega cannot successfully connect to the Onion Cloud
    * More info: Onion's `device-client` code has not changed, the `libcurl` library version has been updated to v7.53.0, is likely the root cause
    * Status: Currently Investigating
* The reset button does not work
    * Info: does not trigger a reboot after a momentary press or a factory reset after a 10 second press
    * Status: Actively working on fixing
* ~~Omega2+ cannot reboot~~
    * Status: Fixed in b142
* ~~Omega2+ cannot mount MicroSD cards~~
    * Status: Fixed in b143
* The `fast-gpio` program always crashes
    * Root Cause: the firmware does not expose the `/dev/mem` device which allows access to the memory map
    * Status: Investigating
* No support for enterprise WiFi that requires a username and password
    * Status: expect a fix in February
* No automatic support for WiFi channels 13 and 14
    * Status: expect a fix early February


### Console Issue Listing

* Cannot change the account password in the Settings app
* Cannot disable the WiFi AP
* The OLED App doesn't properly save image files to the Omega
