### What is UART?

A UART is used for serial communication between devices. UART has no master-slave architecture and allows you to set the transmissions speeds of your data. The transmission speed is known as the **baud rate**, and it represents the time spent holding each bit high or low.

>If you've connected to the Omega via serial before you'll remember that we set the baud rate to 115200 bits-per-second, meaning that the time spent holding each bit high or low is 1/115200bps or 8.6µs per bit.

The UART on the Omega formats the data using the **8N1 configuration**, in which there are **8** data bits, **No** parity bit, and **one** stop bit.

![uart data frame](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/uart-data-frame.png)

<!-- // * include What is a UART section from https://docs.onion.io/omega2-docs/uart1.html -->
<!-- //  -> it prob makes most sense to separate those sections into their own files and include them here -->
