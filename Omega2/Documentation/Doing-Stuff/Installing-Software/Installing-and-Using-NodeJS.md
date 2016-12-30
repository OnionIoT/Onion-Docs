---
title: Using NodeJS
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 3
---

<!-- // refer to the existing article for guidance -->

## Installing and Using NodeJS {#software-installing-and-using-nodejs}

<!-- // brief intro to NodeJS (scripting language, easy to write) -->
<!-- // make sure to mention that its v4.3.1 -->
<!-- // make sure to note how much space installing node will take up -->



NodeJS is a scripting language that uses a JavaScript runtime, essentially, it writes like JavaScript but gives you a lot of flexibility and power. It's incredibly easy to make powerful and complex applications. NodeJS takes advantage of a large amount of open-source modules developed by the community in order to further simplify your work.


The Omega supports NodeJS 4.3.1 which can be installed on your Omega using `opkg`.

### Installing NodeJS

>*Installing NodeJS will take about 8.5MB of space on the Omega, so make sure you've got enough space before continuing.*

Connect to the Omega's terminal using either SSH or Serial.

Run the following commands on the terminal:

```
opkg update
opkg install nodejs
```

### Using NodeJS
<!-- // How to use NodeJS on the Omega.

// example of writing a basic python script that changes the trigger of the Omega LED
// example of how to run it from the command line -->

// TODO: add example of writing a basic script and running it - script should say good morning, good afternoon, good evening based on the system time, also have the Omega LED start blinking at the beginning of the script, when the print is done, sleep for 10 seconds, and then set it back to default-on

You can use NodeJS the same way you would on a computer. Just write a script and execute it with the following command:

```
node /path/to/script.js
```

### Going further

This section will give you more information on how you can use NodeJS on the Omega to create fantastic projects.

#### Learning NodeJS

<!-- // link to nodejs documentation and guides for more info on getting started and learning NodeJS -->

[NodeJS Documentation](https://nodejs.org/api/)

<!-- #### Omega NodeJS packages -->

<!-- // several nodejs packages created by onion to control omega Expansions -->
<!-- // have a list of articles with links -->
<!-- // note: we will create a fourth documentation section, reference, to house all of th e existing documentation -->

<!-- #### Using Blynk with the Omega -->

<!-- // brief description of Blynk and how they're awesome -->
<!-- // link to the main blynk article -->

<!-- Not available on current firmware -->


<!-- #### Using npm - Node Package manager -->

<!-- // info on why npm is useful, note that packages that require compilation will not be installed -->
<!-- // note how much space installing npm will take up -->

<!-- Not available on current firmware -->


<!-- ##### Installing npm -->

<!-- // steps to install npm -->

<!-- ##### Using npm -->

<!-- // give an example of installing a package with npm -->
