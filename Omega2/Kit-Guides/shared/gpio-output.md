### GPIOs as Outputs

The Omega has fifteen General Purpose Input/Output pins (commonly referred to as GPIOs) that can be fully controlled by you, the user. For now, let's focus on using GPIOs in the output direction.

Once a GPIO is set to the output direction, you can have it output either a logical LOW or a logical HIGH. The exact voltage of each will depend on the system that's being used; on the Omega, logical LOW is 0V and logical HIGH is about 3.3V.

<!-- // DONE: IMAGE: descriptive image showing 0V and 3.3V outputs -->
![GPIO outputs](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/gpio-out-graph.png)

These logical HIGH and LOW signals can be used to control external circuits that are separate from the Omega, and are the foundation for your digital circuits!
