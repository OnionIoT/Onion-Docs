---
title: Fading an LED
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 3
---

# Dimming an LED

So far we've been turning LEDs fully on and fully off, but it's also possible have LEDs dimmed to somewhere between on and off. And that's what we're going to do in this experiment: we're going to use Pulse Width Modulation (PWM) to create a dimming effect on an LED.

## Pulse Width Modulation

Pulse Width Modulation (PWM) sounds complicated but in it's essence it's just turning a digital signal on and off at regular intervals. It allows us to easily control how much power is supplied to a component. In our case that component will be an LED and the less power we provide, the dimmer the light the LED will produce.

// TO DO: GRAPHIC: Insert square wave graphic

### Duty Cycle 

The main method to describing PWM signals is the concept of the Duty Cycle: it tells us the percentage of the time the signal is on - at high voltage.

// TO DO: GRAPHIC: Insert PWM Square wave graphic (http://www.bristolwatch.com/picaxe/images/io43.gif)

Consider a PWM signal with a 25% duty cycle: it will be **on** for 25% of the time and **off for 75% of the time. Figuring out the duty cycle is a piece of cake, let's go over the main components:
* The Time On, T<sub>on</sub>, is the amount of time the signal is **on** (also known as the *pulse width*)
* The Time Off, T<sub>off</sub>, is the amount of time the signal is **off**
* The total cycle time, T<sub>cycle</sub>, is the sum of T<sub>on</sub> and T<sub>off</sub>

To calculate the duty cycle, we divide the time the signal is high, T<sub>on</sub>, by the complete cycle time, T<sub>CompleteCycle</sub>, and then express it as a percentage:

$$DutyCycle = {\frac{T_{on}}{T_{on} + T_{off}}}\times100\% = {\frac{T_{on}}{T_{CompleteCycle}}}\times100\%$$

If we remember that:

$$Frequency = {\frac{1}{Period}}%%

We see that the period - the total cycle time - is directly related to the frequency of the PWM signal. A PWM signal with a total cycle time of 20ms has a frequency of 50 Hz. All this means is that the signal will complete 50 full cycles in a second.

### PWM and LEDs 

By sending a PWM signal to an LED, we can control how bright that LED appears to shine. What's actually going on is that the LED is turning on and off many, many times in a second. For example, if we send a 50% duty cycle PWM signal at 50 Hz to an LED, it will be on for 10ms, then be off for 10ms, then be on for 10ms and so on. Since the 50 Hz frequency of the PWM signal is faster than 24 Hz, the maximum sensitivity of the average human eye, you won't actually see the LED turning on and off, you'll perceive the LED as being dimmer.

 

## Building the Circuit

We're going to be providing power to the LED just like we did in the two previous experiments. The only difference is the speed at which we turn the LED on and off! 

Go ahead and build the same circuit we used in the previous two experiments:
* Plug the LED into the breadboard, with the anode and cathode in different rows
* Connect the LED's 
We'll need the same LED circuit we used in the previous two experiments. 

### Hooking up the Components



## Writing the Code

// need to see if we should use fast-gpio or the PWM pins


### What to Expect



### A Closer Look at the Code


#### Fancy For Loops

// have a for loop that increments the PWM and then halfway through starts decrementing the PWM

