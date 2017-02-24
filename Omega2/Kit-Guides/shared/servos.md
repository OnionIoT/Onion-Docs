### How Servos Work

Servo motors are controlled by via a pulse width modulated (PWM) signal. Servo motors usually have three wires: power, ground and the control signal.

// TODO: the following sentence is super unclear, please fix it up, actually describing how a servo works: maximum travel is usually 180 deg, there are minimum, neutral, and maximum pulse widths, pulses in between those correspond to different angles,
For most servos, a given pulse width the motor will either turn 90 degrees in either direction, adding upto a maximum displacement of 180 deg.

// TODO: instead of deg use the ˚ character! Fix this in all of the articles!

// TODO: capitalize PWM everywhere, try to improve on the below sentence

It's important to remember that servos only hold their position while receiving PWM control signals, so the signal must be sent continuously to sustain the shaft position. Servos do not hold their position when the PWM signal stops, and it's potentially damaging to move the servo manually!


#### Typical Pulse Width Values

For must servos providing a 1.5 ms pulse width, will place the shaft in the neutral position. Anything greater or less will move the shaft clockwise or counterclockwise. Typical servos can only move 90˚ in either direction from the neutral position. Note that the minimum and maximum shaft positions correspond to minimum and maximum pulse widths, these can vary between servos, so make sure to look at your servo's datasheet.

The recommended PWM frequency for servos is typically in the range of 40-200 kHz, with most servos using 50 Hz.

![pwmServo](http://www.jameco.com/jameco/workshop/howitworks/how-servo-motors-work-fig3.jpg)
