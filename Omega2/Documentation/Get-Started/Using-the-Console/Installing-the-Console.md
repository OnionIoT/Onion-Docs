---
title: Installing the Console
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 2
---

## Installing the Console {#installing-the-console}

<!-- // Show how to install the console through the setup-wizard, or through the command line -->
The Console can be installed through the Setup Wizard, or through the command line.
Follow this [guide](#first-time-setup) on setting up your Omega, if you have not already done so.

### Installing Using the Setup Wizard

If you have set up the Omega and didn't install the console, skip to the Software page and make sure the checkbox is checked.
![checkbox](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/installing-console-checkmark.png)

Click the Install Console button and your Omega will begin installing the Console. This process takes about 5 minutes.

> This process can take longer than 5 minutes depending on your download speeds.

Refresh the page and you should see the Console login page.
![login-page](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/installing-console-login.png)

The default login info is:

```
username: root
password: onioneer
```

### Installing Using the Command Line

The console can also be installed using the command line using the Omega's package manager, `opkg`.
>For information on how to access the Omega's command line, follow this [guide to connecting to the Omega's Terminal](#connecting-to-the-omega-terminal)

<!-- // note this won't be available till 3rd batch... -->

>You'll need to be connected to the internet in order to install the Console. If you've followed the Setup Wizard, you will be all good to go.

With your terminal open, run the following commands:

```
opkg update
opkg install onion-console-base
```


You can learn more about `opkg` in our [guide to opkg](#using-opkg).

After installation is complete, you'll need to restart the rpcd service to load the console configuration with the following command:

```
/etc/init.d/rpcd restart
```

Now, you can access the console by going to `http://omega-ABCD.local/` where `ABCD` is your Omega's unique identifier.

> If you don't know how to find your Omega's unique identifier you can take a look at our brief [guide to finding your Omega's name](#omega-name)

Upon loading, you should see the console login page.
![login-page](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Get-Started/img/installing-console-login.png)

The default login info is:

```
username: root
password: onioneer
```

<!-- // TODO batch 3 or 4: add a section on navigating and using the console -->

<!-- // TODO: find an appropriate place to mention that oupgrade shouldn't be run from the Terminal app on the console -->
