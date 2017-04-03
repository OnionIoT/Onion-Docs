### UART on the Omega

A **universal asynchronous receiver/transmitter (UART)** is a device used for serial communication between two devices. The Omega comes with two UART devices: `UART0`, and `UART1`. `UART0` is largely used for outputting the Omega's command line, and `UART1` is free to communicate with other devices.

Only **two devices** can communicate with each other per UART connection. This is different from other communication protocols, such as I2C or SPI, where there may be 3, 10, or many more devices connected to the same data lines.

