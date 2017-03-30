The address switch allows you to change the I2C address of the board. This is needed to differentiate multiple Relay Expansions from each other when connected to the same Omega.

![address-switch](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/relay-address-switch.jpg)

It has 3 switches that can be turned either ON or OFF. See the following table for the address values:

| Switch 1 | Switch 2 | Switch 3 | Binary Value |
|----------|----------|----------|--------------|
| OFF      | OFF      | OFF      | *000*        |
| OFF      | OFF      | ON       | *001*        |
| OFF      | ON       | OFF      | *010*        |
| OFF      | ON       | ON       | *011*        |
| ON       | OFF      | OFF      | *100*        |
| ON       | OFF      | ON       | *101*        |
| ON       | ON       | OFF      | *110*        |
| ON       | ON       | ON       | *111*        |

The I2C addresses corresponding to the different switch positions are shown below:

| I2C Device Address | Switch Binary Setting |
|--------------------|-----------------------|
| 0x27               | 000                   |
| 0x26               | 100                   |
| 0x25               | 010                   |
| 0x24               | 110                   |
| 0x23               | 001                   |
| 0x22               | 101                   |
| 0x21               | 011                   |
| 0x20               | 111                   |
