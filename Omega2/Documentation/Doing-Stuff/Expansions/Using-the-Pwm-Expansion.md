---
title: Using the PWM Expansion
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 2
---

<!-- //  this article should include:
    * An Example circuit
    * Controlling the Relays from the command line
    * Info on how the address switch configuration affects the command line call
    * Link to article on controlling relays from C/C++, python
// refer to existing doc for reference - should follow it closely -->

## Using the PWM Expansion {#using-pwm-expansion}


#### Pulse Width Modulation

PWM is a technique to control power output from a circuit. Here's an analogy to explain how this works. Let's say you're watering some delicate flowers in a garden. You have a very simple hose that can only be in either of the following states:

1. **off**, or
1. **on at full blast**, destroying your flowers! :(

PWM is the technique of rapidly turning the hose on and off so that the hose acts as a gentle sprinkler. For example, this can be used to vary the brightness of an LED, making it fade in and out instead of just blinking!

Pulse Width Modulated signals can be described by duty cycle or periods.

![Duty Cycle Graph](http://www.bristolwatch.com/picaxe/images/io43.gif)

##### Duty Cycle

Indicates what percentage of the time a signal is on or high voltage. So a PWM signal with a 25% duty cycle will be high for 25% of the time, and low 75% of the time. The duty cycle can be calculated as follows:

$$DutyCycle = {\frac{T_{on}}{T_{CompleteCycle}}}\times100\%$$

##### Period

Indicates the amount of time (usually in milliseconds) for each part of the cycle.
The Time On, Ton in the diagram above is the time the signal is high. This is also known as pulse width.
Similarly, Time Off, or Toff is the time the signal is low.

The Complete Cycle time corresponds to the overall period of the PWM. Changing the period will also change the frequency of the PWM signal:

$$Frequency = {\frac{1}{Period}}$$