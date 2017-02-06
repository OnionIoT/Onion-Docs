## Communicating with One-Wire Devices {#communicating-with-1w-devices}

The One-Wire protocol is a bus-based protocol that, as the name implies, uses jsut one data wire to transmit data between devices. It allows controllers and processors like the Omega2 to easily communicate with peripheral devices like:

* Sensors, such as temperature, humidity
* Programmable Input/Output chips
* Small relays

### The One-Wire Protocol

One Wire is similar to [the I2C protocol](#communicating-with-i2c-devices) (which is coincidentally sometimes called TWI - Two Wire Interface). One Wire has a lower data transmission rate than I2C but it makes up for it with a longer range.

It follows a master-slave architecture with each bus allowing for one master, in this case the Omega, and many slave devices. Every device type has its own unique single-byte (8 bit) identifier, eg. `0x8f`. Each device in turn has its own unique 8-byte (64-bit) serial number that includes a byte to describe the device type, known as the **family code**, as the Least Significant Byte (LSB).

An example of a One-Wire device serial number is shown below:

![one-wire-serial-number](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/one-wire-serial-number.jpg)

One Wire is also referred to as **1W, 1-Wire, W1** etc.

### The Omega & One-Wire

Interacting with One-Wire devices with the Omega is slightly different from [I2C](#communicating-with-i2c-devices), [SPI](#communicating-with-spi-devices), and [Serial](#uart1) devices, but you'll see that it's not a big deal. Since there is no dedicated hardware One-Wire controller on the Omega, your One-Wire device can be connected to any GPIO. We will then register a One-Wire master in Linux associated with the selected GPIO that will allow us to communicate with the One-Wire slave devices.

**Note that you need to be on firmware b151 or higher!**


### Connecting the Hardware

One-Wire devices will have three available connectors:

* Vcc (usually 3.3V)
* GND
* Data Line

Take a look at your specific sensor's datasheet to identify the pins and determine the recommended voltage.

Make the following connections to your Omega:


| Pin  | Omega Connection |
|------|------------------|
| Vcc  | 3.3V             |
| GND  | GND              |
| Data | GPIO19           |

> Note that making these connections is very easy if you have a [Expansion](#expansion-dock), [Power](#power-dock), or [Arduino](#arduino-dock-2) Dock since they all expose the Omega's GPIOs.

Most GPIOs will work, but for now, let's use GPIO19. Some One-Wire devices will require a **pull-up resistor** on the Data line. For example, the popular DS18B20 temperature sensor, requires a 4.7 kΩ pull-up resistor on the Data line to operate properly. Some One-Wire devices have built-in pull-up resistors or can require different resistance values, check the datasheet of your device to be sure!

> A pull-up resistor is a connection between, in this case, the data line and the voltage line. When the Data line is inactive, the pull up resistor will "pull" the signal to a logical high. Then when the Data line goes active, it will override the pull-up. It essentially ensures the logical level is always valid.

<!-- TODO: expand on pull up resistors -->


### Registering the One-Wire Master

We will need to let our Linux operating system know that we intend to act as a One-Wire Master on GPIO19. So let's run the following command:

```
insmod w1-gpio-custom bus0=0,19,0
```

This command does the following:

* Tells Linux to load the `w1-gpio-custom` kernel module that will allow the Omega to act as a One-Wire master
* It defines that this will be `bus0`
* The `0,19,0` means:
  * This is for bus number `0`
  * Use `GPIO19` as the data pin to communicate with the One-Wire devices
  * The final `0` indicates that we will **not** be setting the data pin to open drain mode

If this command is successful, the following folder will become available:

```
/sys/devices/w1_bus_master1
```

Take a look inside this directory, it will be our One-Wire command centre!

<!-- TODO: test and then add a note about persistence after reboot -->


#### Removing a One-Wire Master

If you're done using your One-Wire device and would like to have your GPIO back, you can disable the One-Wire Master by running the following command:

```
rmmod w1-gpio-custom
```


### Finding One-Wire Slave Devices

Now let's use the new `/sys/devices/w1_bus_master1` directory to find our slave devices.

First let's check to see if there are any slave devices at all:

```
cat /sys/devices/w1_bus_master1/w1_master_slave_count
```

The output will be a number that will tell us how many slave devices are connected:

* If it is a `1`, you already have your device plugged in and you're good to go.
* If you see a `0`, go ahead and plug in your device.
  * The One-Wire bus master kernel module scans the data pin every 10 seconds for new devices so wait a little while and try again

#### Finding your Specific Device

If your check of the slave count file reads `1`, your device has been detected. Run `ls /sys/devices/w1_bus_master1` and you should see a directory that looks something like this: `28-000123456789`. That's the directory of your slave device and it is based on the slave's unique serial number.

Note that each device will have a different serial number, so yours might look a little different. This makes it a little difficult to use One-Wire devices programmatically, but don't worry there's a solution!

Running:
```
cat /sys/devices/w1_bus_master1/w1_master_slaves
```
will print a (newline delimited) list of the serial numbers of all connected One-Wire slaves!


### Reading from a One-Wire Device

Reading from an attached One-Wire device is very simple, just run the following:

```
cat /sys/devices/w1_bus_master1/<DeviceID>/w1_slave
```

where `<DeviceID>` is the serial number of your One-Wire device.

Using the DS18B20 temperature sensor from the section above the command would be:

```
cat /sys/devices/w1_bus_master1/28-000123456789/w1_slave
```

And it will print something like:

```
b1 01 4b 46 7f ff 0c 10 d8 : crc=d8 YES
b1 01 4b 46 7f ff 0c 10 d8 t=27062
```

Where the final `t=27062` indicates the temperature is 27.062 ˚C.

To trim and format the output so just the temperature is returned:

```
root@Omega-2970:/# awk -F= '/t=/ {printf "%.03f\n", $2/1000}' /sys/devices/w1_bus_master1/28-000123456789/w1_slave
27.062
```
