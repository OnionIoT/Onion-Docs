---
title: Using NodeJS
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 3
---

<!-- // refer to the existing article for guidance -->

## Installing and Using NodeJS {#installing-and-using-nodejs}

NodeJS is a scripting language that uses a JavaScript runtime, essentially, it is Javascript you can run without using a browser. It's incredibly easy to make powerful and complex applications. NodeJS takes advantage of a large amount of open-source modules developed by the community in order to further simplify your work.

**Note**: Any Omega2 running firmware v0.3.0 or greater supports NodeJS **v8.10.0**.


### Installing NodeJS

Installing NodeJS will take about **5.7 MB** of space on the Omega, so make sure you've got enough space before continuing.

Connect to the [Omega's terminal](#connecting-to-the-omega-terminal) using either SSH or Serial.

Run the following commands on the terminal:

```
opkg update
opkg install node
```

### Using NodeJS


You can use NodeJS the same way you would on a computer. Just write a script and execute it with the following command:

``` bash
node /path/to/script.js
```

For a quick demo, you can save this to `/root/greeting.js`

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
opkg install node-npm
```

### Using npm

**SPECIAL NOTE! This is different than on a computer!**

To install packages with NPM, there’s a **specific syntax** that needs to be used. Instead of:

```
npm install <PACKAGE>
```

use

```
node --max_old_space_size=64 $(which npm) install <PACKAGE>
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

[NodeJS Documentation](https://nodejs.org/docs/v8.10.0/api/) is available from the official Node website.

#### Visual Programming with Node-Red

Node-RED is a flow-based, visual programming tool based on NodeJS that runs in the browser. It comes packaged as an OnionOS App for the Omega2 Pro and can be easily accessed through OnionOS in any browser.

![](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/node-red-3-flow.png)

Learn more about [installing and using Node-Red on the Omega2 Pro](#node-red-article).
