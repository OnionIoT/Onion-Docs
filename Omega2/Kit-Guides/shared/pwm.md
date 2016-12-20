### PWM

PWM(Pulse Width Modulation) is a technique of producing varying analog signals from a digital source. 

![alt text](http://www.bristolwatch.com/picaxe/images/io43.gif)

#### Duty Cycle

Indicates what percentage of the time a signal is on or high voltage. So a PWM signal with a 25% duty cycle will be high for 25% of the time, and low 75% of the time. The duty cycle can be calculated as follows:

$$DutyCycle = {\frac{T_{on}}{T_{CompleteCycle}}}\times100\%$$

#### Period

Indicates the amount of time (usually in milliseconds) for each part of the cycle.
The Time On, Ton in the diagram above is the time the signal is high. This is also known as pulse width.
Similarly, Time Off, or Toff is the time the signal is low.

The Complete Cycle time corresponds to the overall period of the PWM. Changing the period will also change the frequency of the PWM signal:

$$Frequency = {\frac{1}{Period}}$$

#### Application

The power of PWM signals is that they allow you to deliver a continous range of voltages between the digital Hi and Low values. 