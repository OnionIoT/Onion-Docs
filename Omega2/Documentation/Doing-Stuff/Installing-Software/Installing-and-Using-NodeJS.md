---
title: Using NodeJS
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 3
---

<!-- // refer to the existing article for guidance -->

## Installing and Using NodeJS {#software-installing-and-using-nodejs}

NodeJS is a scripting language that uses a JavaScript runtime, essentially, it is Javascript you can run without using a browser. It's incredibly easy to make powerful and complex applications. NodeJS takes advantage of a large amount of open-source modules developed by the community in order to further simplify your work.

**Note**: The Omega supports NodeJS **4.3.1**.


### Installing NodeJS

Installing NodeJS will take about **8.5MB** of space on the Omega, so make sure you've got enough space before continuing.

Connect to the Omega's terminal using either SSH or Serial.

Run the following commands on the terminal:

```
opkg update
opkg install nodejs
```

### Using NodeJS

For a quick demo, you can save this to `/root/greeting.js`

```javascript
// Importing packages
var fs      = require('fs');
var util    = require('util');
    exec    = require('child_process').exec;

var child = exec('uci get system.@led[0].sysfs',
      function (error, stdout, stderr) {
            var triggerPath = '/sys/class/leds/' + stdout.replace('\n','') + '/trigger'
            blinkLed(triggerPath);
            resetAndExit(triggerPath);
        }
    );

// find the path to the Omega LED
// TODO: test for stripping needs

// Set the Omega LED trigger to "timer" so that it blinks
function blinkLed (triggerPath) {
    fs.open(triggerPath, 'w', (err, fd) => {
        fs.write(fd, 'timer', () =>{
            fs.close(fd);
        });
    });
}

function resetAndExit (triggerPath) {
    setTimeout(() => {
        currentTime = new Date();

        // Sets the Omega LED trigger to "default-on"
        if (currentTime.getHours() < 12) {
                console.log('Good morning.');
        }
        else if (currentTime.getHours() < 18  && currentTime.getHours() >= 12) {
                console.log('Good afternoon.');
        }
        else {
                console.log('Good evening.');
        }

        // Set the Omega LED back to being always on
        fs.open(triggerPath, 'w', (err, fd) => {
            fs.writeSync(fd, 'default-on');
            fs.closeSync(fd);
        });
    }, 5000);
}


// Print a greeting based on the time of day
// Gets the current time
```

You can use NodeJS the same way you would on a computer. Just write a script and execute it with the following command:

``` bash
node /path/to/script.js
```


### npm

npm stands for Node Package Manager. As the name implies, it's the official way of installing and updating node packages. Node is usable on its own, but npm gives you access to a whole new world of software others have built - so you don't need to do it yourself!

#### Installing npm

The commands and procedure is much the same as installing NodeJS:

``` bash
opkg update
opkg install npm
```

>If you've updated already, you can skip it.


### Using npm

Installing packages with npm is easy, all you need is the package name and npm installed. Then you can run the following command:

``` bash
npm install <package>
```

Not only can npm install packages, it can also create a package out of your project! To do so, run the command below, it will guide you through the creation of your own node package.

``` bash
npm init
```

If you have packages installed already, they will be included as dependencies, and your package.json will be updated accordingly.

### Going further

We've included links to guides on how you can use NodeJS on the Omega to create fantastic projects.

#### Learning NodeJS

<!-- // link to nodejs documentation and guides for more info on getting started and learning NodeJS -->

[NodeJS Documentation](https://nodejs.org/docs/latest-v4.x/api/) is available from the official Node website.

#### Omega Expansion NodeJS packages

Currently, all software for the Omega Expansions are available through `opkg`.

``` bash
opkg update
opkg install node-oled-exp
opkg install node-pwm-exp
opkg install node-relay-exp
```

Documentation for the packages can be found on the main [Onion Documentation](https://docs.onion.io) site.

[OLED Expansion](https://docs.onion.io/omega2-docs/oled-expansion-node-module.html)

[PWM Expansion](https://docs.onion.io/omega2-docs/pwm-expansion-node-module.html)

[Relay Expansion](https://docs.onion.io/omega2-docs/relay-expansion-node-module.html)


#### Using Blynk with the Omega

The Omega supports Blynk!

You can learn about how to get it up and running on your Omega in our Software Reference [article](#blynk-library)

<!-- // brief description of Blynk and how they're awesome -->
<!-- // link to the main blynk article -->

<!-- Not available on current firmware -->
