## PHP Date & Time Functions on the Onion Omega {#php-date-time-functions}

Maybe you too have just tried a date() function in PHP and received this error message:

```
Warning: date(): Invalid date.timezone value 'UTC', we selected the timezone 'UTC' for now. in /www/test.php on line 2
Fatal error: date(): Timezone database is corrupt - this should never happen! in /www/test.php on line 2
```

The good news is that it's very simple to resolve, what your Omega is missing is the timezone packages!

### How to add `zoneinfo` to your Onion Omega

For this example I am assuming you wish to use a European timezone (London or Rome etc...) to find the others is easy and this is covered in the section below.

Open a console to you Onion Omega and enter:

``` bash
opkg update
opkg install zoneinfo-europe
```

Now it's a dead simple case of updating your php.ini file(s) that are found in "/etc" with the line similar to this for London:

```
[Date]
date.timezone = "Europe/London"
```

A quick copy & paste line for the console to edit the default php.ini file is:
``` bash
nano /etc/php.ini
```

Edit as desired and press Ctrl + X, then Y to save the file.


You can confirm date/time functions are now working with this sample code:

```
<?php
echo date("d-M-Y");
```

No error messages = happy days! = happy hacking :)


### Finding the available timezones

For the example above we set up the Omega to for "Europe/London", however you may not want that due to your location, so instead you'll need to install the zoneinfo for your desired location.

To find out the package you require, run this command on your Omega's console:

``` bash
opkg update
opkg list|grep zoneinfo
```

You'll receive a list of packages similar to the ones below, back in the first example change the "zoneinfo" line to your desired zone:

```
zoneinfo-africa - 2015d-1 - Zone Information (Africa)
zoneinfo-asia - 2015d-1 - Zone Information (Asia)
zoneinfo-atlantic - 2015d-1 - Zone Information (Atlantic)
zoneinfo-australia-nz - 2015d-1 - Zone Information (Australia-NZ)
zoneinfo-core - 2015d-1 - Zone Information (core)
zoneinfo-europe - 2015d-1 - Zone Information (Europe)
zoneinfo-india - 2015d-1 - Zone Information (India)
zoneinfo-northamerica - 2015d-1 - Zone Information (NorthAmerica)
zoneinfo-pacific - 2015d-1 - Zone Information (Pacific)
zoneinfo-poles - 2015d-1 - Zone Information (Arctic, Antarctic)
zoneinfo-simple - 2015d-1 - Zone Information (simple)
zoneinfo-southamerica - 2015d-1 - Zone Information (SouthAmerica)
```

Change the zone as desired and if you're still not sure which one you need, the "[List of Supported Timezones](http://php.net/manual/en/timezones.php)" from the PHP manual will help.


### Special Thanks

A note of special thanks to Manuel Baldassarri for replying to my query about this in the [community forums](https://community.onion.io/topic/627/php-issue-fatal-error-date-timezone-database-is-corrupt-this-should-never-happen). I looked everywhere trying to resolve this issue and it turned out it was simple. Thanks Manuel!
