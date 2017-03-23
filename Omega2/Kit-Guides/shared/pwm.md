### Pulse Width Modulation

Pulse Width Modulation (PWM) is a technique of producing varying analog signals from a digital source.

Digital signals can only be either HIGH or LOW, where the HIGH voltage is some fixed value depending on the circuit. On the Omega, HIGH on the Omega is 3.3V.

On the other hand, an **analog** signal can be any voltage between HIGH and LOW. Normally, digital circuits can't freely vary voltage signals, but they can use PWM to get close enough. It works by repeatedly pulsing a HIGH digital signal on and off so that the **average** voltage coming from the circuit over time would be equivalent to an analog signal between HIGH and LOW. To change the analog voltage, you can vary how fast the HIGH signal is pulsed.

There are some limitations to this method depending on how the driving circuit is built, but it's relatively simple to implement and can be accurate enough for most cases.

![A few difference PWM signals, at varing duty cycles](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/shared-pwm-signals.jpg)

<!-- // TODO: would be nice if this graphic also had the Duty Cycle % -->
