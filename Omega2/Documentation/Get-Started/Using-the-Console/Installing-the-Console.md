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

<!-- command line console installation instructions -->
```{r child = './Installing-the-Console-Component-Command-Line-Install.md'}
```

<!-- accessing the console -->
```{r child = './Accessing-the-Console-Component.md'}
```


#### Behind the Scenes

<!-- console install tool explanation -->
```{r child = './Installing-the-Console-Component-Command-Line-Install-Explanation.md'}
```


<!-- // TODO batch 3 or 4: add a section on navigating and using the console -->

<!-- // TODO: find an appropriate place to mention that oupgrade shouldn't be run from the Terminal app on the console -->
