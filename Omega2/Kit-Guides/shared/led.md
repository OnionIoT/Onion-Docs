### LEDs

Now let's talk about Light Emitting Diodes, or as they're more commonly known, LEDs. A regular diode is an electronic component that allows current to flow in only one direction. Think of it as a very strict policeman watching a one-way street. An LED is a type of diode that lights up when there is current flowing through it (but only when it's flowing in the right direction)!

<!-- // DONE: IMAGE: good image of an LED -->
![A red LED](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/shared-led-photo.jpg)

If you look closely, you'll see that every LED has a longer leg and a shorter leg. This is because LEDs are diodes and we need to know in which direction it will allow current to flow. 

* The longer leg is the positive side, called the **anode**. It should always be connected to the current **source**. 
* The shorter leg is the negative side, called the **cathode**, where the current **exits** the LED. Always connect this side towards the ground connection.

![Labelled LED](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/shared-led-labelled.png)

<!-- // DONE: this image is really good but doesn't show the difference between the cathode and anode. Need something like: https://cdn.sparkfun.com/assets/learn_tutorials/2/7/5/LED_drawing_01.png (pls don't just jack this image) -->


Just like a regular light bulb, an LED can burn out if it's supplied with too much current. LEDs in electronics are almost always used in series with a current limiting resistor that, you guessed it, will put a limit on how much current can pass through the LED.

> For more information on how a resistor can limit current, we recommend checking out this [Sparkfun tutorial on Ohm's law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)
