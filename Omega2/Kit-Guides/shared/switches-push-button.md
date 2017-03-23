### Push Button Switches

A push button is a momentary switch, so unlike a slide switch where the change in the switch state (on or off) will be permanent, the change in a push button's state will only last while the button is being pressed. It's called a **momentary** switch because the change in state is only while the button is being pressed; when the button is released, the switch .

<!-- // DONE: Image of a push button switch -->

![Push button switch](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/shared-switches-push-button.jpg)

Unlike the SPDT switches with levers, the push button switches in your Kit are the single pole single throw type, or **SPST**. It's named this way because:

* There is one contact that is switched when you push the button ("single pole")
* The contact is switched between being disconnected and being connected to one output ("single throw")

<!-- // TODO: animation of switch being pressed, enabling flow of current in circuit, then flow stopping after button is released
- we don't have time for this one, photo added instead-->
![How the push button works](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/switches-push-button-on-off.png)

For example, the buttons on TV remotes are all momentary push button type switches, so expect the same type of functionality (changing settings) with push buttons in our experiments and projects.

You may be wondering, "If there are four pins, how come this switch doesn't have two switch contacts?" This is because the button is made of two pairs of connected pins that split each end into two connections. The photo below shows which pins are connected, so take note that your circuit properly switches when it's supposed to:

<!-- // DONE: photo or graphic of connected pins on SPST push button -->
![How the pins of a push button are connected](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/shared-switches-push-button-layout.jpg)
