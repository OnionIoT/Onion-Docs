### How Servos Work

Servo motors are controlled by via a pulse width modulated (PWM). For most servos, a given pulse width the motor will either turn 90 degrees in either direction, adding upto a maximum displacement of 180 deg. Servo motors have three wires: power, ground and the control signal.

Also note that servos do not hold their position once the pwm signal has been stopped. To sustain the shaft positon the pwm signal must be repeated. 

#### Typical Pulse Width Values

For must servos providing a 1.5 ms pulse width, will place the shaft in the neutral position, while anything greater or less will move the shaft to the 90 deg clockwise and counterclockwise. The PWM frequency is typically in the range of 40-200kHz.

![pwmServo](http://www.jameco.com/jameco/workshop/howitworks/how-servo-motors-work-fig3.jpg)
