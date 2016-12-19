### Debouncing Switches

To simplify our circuits, we assume switches cleanly change state when you push or flip them. However, in real life with real physics, switches' electrical contacts don't work exactly the way we want them to. When changing state, the electrical contacts will rapidly connect and disconnect like mini sparks as they just start to touch (when closing) or separate (when opening), until settling to their final value. This is known as **bouncing**. The graph below shows an example of a switch closing with respect to time: notice how the switch rapidly goes from OFF (low) to ON (high) repeatedly until settling at ON.

![bouncing-switch](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/switch-bouncing.gif)

We want to avoid this since it will wreak havoc on our software that treats the button as a trigger for an action. When we press the button once, we expect the action to trigger only once; however, because the signal is bouncing, the action may be triggered tens or even hundreds of times. While this may not be an issue for simple actions such as turning on an LED, this can cause huge problems in more complex systems, such as programs that send messages to each other. For example, you don't want to press a button to lower the thermostat by 1 degree and have it lower by 12!

One way to solve this problem, or **debounce** the signal, is to add a few simple components around the switch to *filter* out these unwanted bounces. The diagram below shows a way of doing this.

![hardware-debouncer](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/hardware-debouncer.jpg)

Something to keep in mind about this setup is that **the input reads HIGH when the switch is open, and LOW when the switch is closed**. This may seem backwards at first, but this convention is actually very common with integrated circuits out in the wild! When writing programs, you should abstract this convention away from the main routines by using functions that return `TRUE` or `FALSE` depending on how you define the switch state, not the signal itself.

// explain how the debouncing capacitor smooths out the signal:
//  * when the switch is turned on: it takes a while for it to charge up to a logical one voltage level and it will only charge while the signal coming from the switch is high, by the time the capacitor charges up, the signal bouncing should have ended (include a graphic)
//  * when the switch is turned off: it will take a while for it to discharge down to a logical zero voltage level, but that time the signal will have stopped bouncing (include a graphic)
// [go into more detail for these two points: see http://www.ganssle.com/debouncing-pt2.htm for a great reference on the whole process]

We've added 2 resistors, which limit the current or charge flow, through the circuit, and a capacitor, which can store and release electrical charge. Here's how it works:

**Closing the Switch**

* If the switch has been open for a while, the capacitor is fully charged and stores enough charge for a logic HIGH. The GPIO senses a logic HIGH.
* When you close the switch, the GPIO and capacitor are now connected to ground. The GPIO starts to be pulled LOW, but the contacts are bouncing and the signal is rapidly changing between HIGH and LOW.
* While the switch is bouncing, the capacitor starts slowly releasing its charge to ground through R2, and so the GPIO still sees a logic HIGH.
* When the switch is done debouncing, the capacitor quickly discharges the rest of its charge and the GPIO sees a logic LOW.

**Opening the Switch**

    