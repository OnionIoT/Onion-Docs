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
<!-- TODO: link to connecting to the omega's command line article -->

Run the following commands on the terminal:

```
opkg update
opkg install nodejs
```

### Using NodeJS


You can use NodeJS the same way you would on a computer. Just write a script and execute it with the following command:

``` bash
node /path/to/script.js
```

For a quick demo, you can save this to `/root/greeting.js`

TODO: verify the modified script works

```javascript
// Importing packages
var fs      = require('fs');
var util    = require('util');
    exec    = require('child_process').exec;

// Set the Omega LED trigger to the specified mode
function setLed (triggerPath, triggerMode) {
    fs.open(triggerPath, 'w', (err, fd) => {
        fs.write(fd, triggerMode, () =>{
            fs.close(fd);
        });
    });
}

var child = exec('uci get system.@led[0].sysfs',
      function (error, stdout, stderr) {
            // set the Omega LED to blink
            var triggerPath = '/sys/class/leds/' + stdout.replace('\n','') + '/trigger'
            setLed(triggerPath, 'timer');

            // Print a greeting based on the time of day
            currentTime = new Date(); // get the current time
            if (currentTime.getHours() < 12) {
                    console.log('Good morning.');
            }
            else if (currentTime.getHours() < 18  && currentTime.getHours() >= 12) {
                    console.log('Good afternoon.');
            }
            else {
                    console.log('Good evening.');
            }

            // set the Omega LED to solid after 5 seconds
            setTimeout(() => {
                setLed(triggerPath, 'default-on');
            }, 5000);
        }
    );
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

### Omega Expansion NodeJS packages

We have developed NodeJS modules for controlling several Omega Expansions, they're all available hrough `opkg`.

``` bash
opkg update
opkg install node-oled-exp
opkg install node-pwm-exp
opkg install node-relay-exp
```

<!-- TODO: this is hosted on the documentation site... no need for the link -->

Documentation for the packages can be found on the main [Onion Documentation](https://docs.onion.io) site:

* [OLED Expansion](https://docs.onion.io/omega2-docs/oled-expansion-node-module.html)
* [PWM Expansion](https://docs.onion.io/omega2-docs/pwm-expansion-node-module.html)
* [Relay Expansion](https://docs.onion.io/omega2-docs/relay-expansion-node-module.html)

<!-- TODO: change the above links to use the #tags -->


### Blynk & the Omega

The Omega supports Blynk! Check out our [Blynk article](#blynk-library) to learn more!

<!-- TODO: add a little bit more info on blynk to this blurb -->

<!-- // brief description of Blynk and how they're awesome -->
<!-- // link to the main blynk article -->
