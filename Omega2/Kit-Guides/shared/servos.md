### How Servos Work

Servo motors are controlled by via a pulse width modulated (PWM) signal. Servo motors usually have three wires: power, ground and the control signal.

<!-- // DONE: the following sentence is super unclear, please fix it up, actually describing how a servo works: maximum travel is usually 180 deg, there are minimum, neutral, and maximum pulse widths, pulses in between those correspond to different angles, -->
Most servoes fixedly rotate between 0° and 180° - starting and ending at fixed points relative to the motor. They accept pulses within a fixed range commonly between 500 and 2500us. To put it all together, say we send a 500us width pulse to a servo accepting pulses between 500us and 2500us. The servo will rotate its arm to the 0° position in response - no matter which position the arm was in before. It will respond with approrpiate increments when the pulsewidth is increased up until 2500us, then it will stop moving.

<!-- // DONE: instead of deg use the ° character! Fix this in all of the articles! -->

<!-- // DONE: capitalize PWM everywhere, try to improve on the below sentence -->
When the servo is receiving signals continuously, it will apply force to attempt to stay in the position that is being signalled. When the servo is unpowered and sent no signals, it won't actively try to restore position. Manually moving the servo arm is possible when unpowered, but it should not be done as it can damage the servo.


#### Typical Pulse Width Values

For most servos, providing a 1.5 ms pulse width will place the shaft in the neutral position. Anything greater or less will move the shaft clockwise or counterclockwise. Typical servos can only move 90˚ in either direction from the neutral position. Note that the minimum and maximum shaft positions correspond to minimum and maximum pulse widths, these can vary between servos, so make sure to look at your servo's datasheet.

The recommended PWM frequency for servos is typically in the range of 40-200 kHz, with most servos using 50 Hz.

![pwmServo](http://www.jameco.com/jameco/workshop/howitworks/how-servo-motors-work-fig3.jpg)
