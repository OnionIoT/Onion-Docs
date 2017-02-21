### LEDs

Now let's talk about Light Emitting Diodes, or as they're more commonly known, LEDs. A regular diode is an electronic component that allows current to flow in only one direction. Think of it as a very strict policeman watching a one-way street. An LED is a type of diode that lights up when there is current flowing through it (but only when it's flowing in the right direction)!

// TODO: IMAGE: good image of an LED

If you look closely, you'll see that every LED has a longer leg and a shorter leg. Don't worry, they didn't make a mistake at the factory, remember, LEDs are diodes so we need to know the direction in which to apply current. The longer leg is the positive side, it's called the `anode` and it should always be connected to the current source. The shorter leg is the negative side, called the `cathode`, where the current exits the LED. Always connect this side to ground.

// TODO: IMAGE: labelled drawing of an LED (include the flat side thing as well)

Just like a regular light bulb, an LED can burn out if it's supplied with too much current. LEDs in electronics are almost always used in series with a current limiting resistor that, you guessed it, will put a limit on how much current can pass through the LED.

> For more information on how a resistor can limit current, we recommend checking out this [Sparkfun tutorial on Ohm's law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)
