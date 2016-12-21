### LCD Screen

<!-- // LCD screen:
//  * 16x2 meaning two rows that can fit 16 characters each
//  * led backlight to illuminate the display
//  * usually these LED screens are controlled by parallel (many) data lines - like 11 usually
//    * this one has additional circuitry that allows devices to use the i2c protocol to control the screen -->

The LCD screen is a **16x2** display, meaning it has **2 rows** of **16 columns (characters)**. It has an LED backlight to illuminate the display even in the dark!

These screens are typically controlled by many parallel data lines, usually 11 or so. However, the one included with the kits has additional circuitry that allows devices to use 4 wires and the I2C protocol to control the screen instead!