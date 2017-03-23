### GPIOs as Inputs

Now let's talk about the I in GPIO: using GPIOs in the input direction. This will allow you to read the logical level of circuits that are connected to the Omega.

This leads to two situations:

1. If a signal is connected to an input GPIO and its voltage is 0V, the Omega will read a logic low

![GPIO LOW](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/shared-gpio-input-low.jpg)

2. If a signal with a voltage of around 3.3V is connected to an input GPIO, the Omega will read a logic high.

![GPIO HIGH](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/shared-gpio-input-high.jpg)

<!-- // DONE: IMAGE: add illustrations of: 1) gpio connected to ground, reading logical low, 2) gpio connected to Vcc, reading logical high -> USE FRITZING FOR THIS -->


Using GPIOs in the input direction, allows us to sample the state of any circuit connected to the Omega. As you'll see, this is going to be very useful.
