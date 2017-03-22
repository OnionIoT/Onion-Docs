### I2C Device Address {#reference-shared-i2c-device-address}
The Relay Expansion is the only expansion that has a configurable I2C device address. This was done so that up to eight Relay Expansions can be stacked on a single Omega, giving the user the ability to control 16 relay modules independently.

The base device address is 0x20, the dip switches control the offset added to the base address:

 * The 'Off' position for each switch is when the toggle is close to the numbers on the switch, or away from the relay modules.
 * The 'On' position is when the toggle is away from the numbers on the switch, or closer to the relay modules.

The table below defines the relationship:

| Switch 1 | Switch 2 | Switch 3 | I2C Device Address | `addr` Argument |
|:--------:|:--------:|:--------:|:------------------:|:---------------:|
|    Off   |    Off   |    Off   |        0x27        |       `7`       |
|    Off   |    Off   |  **On**  |        0x26        |       `6`       |
|    Off   |  **On**  |    Off   |        0x25        |       `5`       |
|    Off   |  **On**  |  **On**  |        0x24        |       `4`       |
|  **On**  |    Off   |    Off   |        0x23        |       `3`       |
|  **On**  |    Off   |  **On**  |        0x22        |       `2`       |
|  **On**  |  **On**  |    Off   |        0x21        |       `1`       |
|  **On**  |  **On**  |  **On**  |        0x20        |       `0`       |

The `addr` argument is used for library functions to specify which Relay Expansion to act on.

#### Relay Module Select

Each relay expansion has two channel which can be called using binary values.

<!-- TODO: IMAGE reupload this to github -->

![imgur](https://i.imgur.com/Wk6Z9lW.png)
