Generate a software-based Pulse Width Modulated (PWM) signal on a selected pin. Specify the desired duty cycle and frequency of the PWM signal.

```
fast-gpio pwm <gpio> <freq in Hz> <duty cycle percentage>
```

This will launch a background process that will generate the PWM signal.

> Software-based PWM is implemented by a program that usually waits for a defined amount of time before toggling the GPIO output. This has the potential to be **inaccurate** since the CPU might be interrupted with other processes and tasks. Software PWM is generally good enough for dimming an LED but not for something requiring more accuracy, such as driving a servo.

To stop the PWM signal, set the GPIO's value:

```
fast-gpio set <gpio> 0
```
