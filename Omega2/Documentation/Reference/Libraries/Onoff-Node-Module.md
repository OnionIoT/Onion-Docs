## Onoff Node Module for Omega {#onoff-node-module}

Using the OnOff Module, you can control the Omega's GPIOs using NodeJS.

We've made this package available through opkg since installing npm, the regular Node package manager, on the Omega requires the use of external USB storage.

### Programming Flow

The onoff package allows control of the direction and state of a pin. It provides a class that handles the nitty gritty of GPIO management so you can worry about making cool stuff instead. For further reading on the functionality, refer to the [documentation](https://www.npmjs.com/package/tm-onoff).

### Installation

Make sure you have node installed, we've written a [guide](#installing-and-using-nodejs) in case you get stuck. To install the onoff package run the following commands:

```
opkg update
opkg install onoff-node
```

### Using Onoff

Onoff can be used by simply importing it into your script, nothing tricky here.

#### Getting started

The module will be installed to the `/usr/bin/` directory, so you will need to point to the correct directory for import.

Your import code should look like this:

```js
var Gpio = require('/usr/bin/onoff-node/onoff.js').Gpio;
```

#### Code Example

The following is a test script that will blink an LED connected to GPIO6 every two seconds.

Let's create a file `test.js`:

```js
var Gpio = require('/usr/bin/onoff-node/onoff.js').Gpio;

var led = new Gpio(6,'out');

var num = 1;

setInterval((function(){
	this.num ^= 1;
	led.writeSync(this.num);
}),2000);

```

Run the script with the following command:

```
node test.js
```

And watch that little LED blink!
