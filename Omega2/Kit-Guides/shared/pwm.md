### Pulse Width Modulation

PWM (Pulse Width Modulation) is a technique of producing varying analog signals from a digital source. Basically it's just turning a digital signal on and off at regular intervals. It easily allows us to control how much power is supplied to a component. In our case that component will be an LED and the less power we provide, the dimmer the light the LED will produce.

![alt text](http://www.bristolwatch.com/picaxe/images/io43.gif)

#### Duty Cycle

Indicates what percentage of the time a signal is on or high voltage. 

Consider a PWM signal with a 25% duty cycle: it will be **on** for 25% of the time and **off** for 75% of the time. Figuring out the duty cycle is a piece of cake, let's go over the main components:

* The Time On, T<sub>on</sub>, is the amount of time the signal is **on** (also known as the *pulse width*)
* The Time Off, T<sub>off</sub>, is the amount of time the signal is **off**
* The total cycle time, T<sub>cycle</sub>, is the sum of T<sub>on</sub> and T<sub>off</sub>

The duty cycle can be calculated as follows:

$$DutyCycle = {\frac{T_{on}}{T_{CompleteCycle}}}\times100\%$$

#### Period

Indicates the amount of time (usually in milliseconds) for each part of the cycle.
The Time On, Ton in the diagram above is the time the signal is high. This is also known as pulse width.
Similarly, Time Off, or Toff is the time the signal is low.

The Complete Cycle time corresponds to the overall period of the PWM, or Ton + Toff. 

The **frequency** is the inverse of period:

$$Frequency = {\frac{1}{Period}}$$

For example, a PWM signal with a total cycle time of 20ms has a frequency of 50 Hz. All this means is that the signal will complete 50 full cycles in a second.

#### Application

The power of PWM signals is that they allow you to deliver a continous range of voltages between the digital Hi and Low values. 