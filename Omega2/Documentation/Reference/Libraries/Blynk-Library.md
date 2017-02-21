## Blynk Library for Omega {#blynk-library}

The Omega officially supports Blynk and the Blynk Library. You can now use the Blynk app to control your Omega. This means you can get your project running in minutes! The library comes as a NodeJS module, and can be installed using opkg.


### Programming Flow {#blynk-programming-flow}

The Blynk library for the Omega works with [NodeJS](#software-installing-and-using-nodejs), and uses virtual pins to send signals to the Omega. In the front end, you can connect pins to buttons, knobs and dials to suit your needs.

### In the Blynk of an Eye {#blynk-context}

Blynk is a platform dedicated to create apps that interface IoT devices with mobile phones - the Omega/2/2+ amongst them. It provides an app that allows you to make beautiful apps of your own for your IoT network.

For further reading on the library's functionality refer to the [documentation](https://www.npmjs.com/package/blynk-library) or check out [blynk.cc](blynk.cc).


### The Blynk Library {#blynk-description}

The library works with NodeJS - Blynk leverages the Node ecosystem, so you can integrate it to any Node projects with ease!


#### Installation

To install the Blynk library run the following commands:

```
opkg update
opkg install blynk-library
```

This will install Node.js 4.3.1 as well, if it is not already installed.

NodeJS is **pretty big**. Plus the libraries, you may find your Omega getting full. To help you out, you'll find below info on how much space each package will take up on your Omega:

|Package|Size|
|-------|----|
|nodejs|8.5MB|
|blynk-library|260kB|
|onoff|880kB|


#### OnOff Package

If you would like to use Blynk to control the Omega's GPIOs, you will need to install the `onoff` Node package as well:
```
opkg update
opkg install onoff-node
```


#### Auth Token Check

You can run a quick check to see if your Auth Token works correctly:

``` js
node /usr/bin/blynk-library/bin/blynk-client.js <Auth Token>
```

> See [Blynk's getting started guide](http://www.blynk.cc/getting-started/) for info on creating your Auth Token


### Using the Library {#blynk-using-library}

Blynk is a platform, thus integration with their service is needed for your Omega/Blynk projects to work properly. Blynk has provided a solid [guide](http://www.blynk.cc/getting-started/) to get you started on using the platform.


#### Getting Started with Blynk

On the Omega, the modules will be installed to the `/usr/bin/` directory, so you will need to point to the correct directory for import. Your import code should look like this:

```js
var BlynkLib = require('/usr/bin/blynk-library');
```


#### Code Example

The following is a test script to illustrate communication via the Blynk App. On the App side create a button that is a virtual pin 1 (V1)

Then create a file test.js:

```javascript
var BlynkLib = require('/usr/bin/blynk-library');

var blynk = new BlynkLib.Blynk('<YOUR AUTH TOKEN HERE!>'); // Make sure to replace this with your Auth Token
var v1 = new blynk.VirtualPin(1);

v1.on('write', function(param) {
  console.log('V1:', param);
});

```

And you can run the script with the following command:
```
node test.js
```

Press the button on you app and note the output on the screen.


You can take this further by using the [OnOff module](#onoff-node-module) to control the Omega's GPIOs.
