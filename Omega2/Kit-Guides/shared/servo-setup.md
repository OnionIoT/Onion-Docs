### Connecting Servos

We've placed the PWM pins in the same order that most* servo motors have them, so you can plug them right in!

>One exception we've found is Airtronics servos, which may have the Vcc and SIGNAL pins on the outside.

Take a look at your servo's connector. Typically the GND wire is black; line it up with the black GND pin on the servo channel's header. The SIGNAL wire will then plug into the white header pin on the bottom. The photo below shows a Hitec servo properly plugged into channel 1 (SIGNAL is the yellow wire).

![pwm-servomotor](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/pwm-servomotor.jpg)

Check out the PWM Expansion hooked up to the servos on our Spiderbot!

![pwm-spiderbot](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/pwm-spiderbot.jpg)

#### The Barrel Jack adapter

The Omega supplies enough power to move only one or two servos under light load. In order to power projects with a bunch of servos, we've included an onboard DC barrel jack connector that can be used to supply power to any connected servos.

>It is not recommended to attempt to power more than 2 servos without an external power supply.

![barrel-jack](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/pwm-barrel-jack.jpg)

The DC voltage supplied through the barrel jack will be provided on the Vcc (and GND) pins. The PWM voltage will also be stepped up to this voltage. We've safely tested up to 12V, so try not to go beyond that or you risk damaging your Expansion. To get more power at this stage, look for power supplies with higher current ratings rather than higher voltages.

Note that the Omega cannot be powered through this connector and still requires its own power supply.


