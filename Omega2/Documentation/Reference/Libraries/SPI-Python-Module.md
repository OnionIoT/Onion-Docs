## SPI Python Module {#spi-python-module}

To interact with SPI devices, we recommend using Python and the `spidev` module. The `spidev` module provides series of functions that implement SPI communication through the Linux device interface. It also provides an Omega2-specific `xfer3` function that implements a half-duplex write-then-read SPI transmission. 

For more information on installing and using the `spidev` module, please see the instructions in our [`python-spidev` GitHub repo](https://github.com/OnionIoT/python-spidev). See the [Installing and Using Python article](#installing-and-using-python) for more details on using Python with the Omega2.
