## Communicating with the Microcontroller {#arduino-dock-communicating-via-serial}

One of the method of communicating between the Omega and the microcontroller ATmega is through the serial interface UART1. The UART connection provides two-way communication using two pins on the Omega: TXD (transmitting from Omega) and RXD (receiving from ATmega).

<!-- // DONE: diagram Omega RXD and TXD to ATmega TXD and RXD on UART1 -->
![Serial pin layout on the Arduino Dock](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/Arduino/img/arduino-dock-uart-diagram.png)

There are two UART ports on the Omega: UART0 and UART1. The port UART1 is used to connect the Omega to the ATmega on the Arduino Dock 2.

<!-- // DONE: image of Arduino Dock 2 UART1 -->
![Where the UART1 pins are located on the expansion header](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/Arduino/img/arduino-dock-uart1-labelled.png)

In order to communicate between Omega and the ATmega, we use command line or python script to send and receive data on the Omega. On the ATmega side, we flash the microcontroller with a sketch to read and write data.

One important thing to note is the baud rate, which is the rate at which the data is transferred in bits per second. The baud rate can be varied but the Omega and the ATmega UART must be programmed to have the same baud rate.



### Flashing the ATmega to communicate with the Omega

First we need to flash the ATmega with a sketch, programming it to read and/or write data. Details on flashing the dock can be found in the relevant [article](https://docs.onion.io/omega2-docs/flash-arduino-dock-wirelessly.html#flash-arduino-dock-wirelessly) in the Onion Docs.

<!-- // DONE: reference flashing ATmega -->

We will use the serial library from the Arduino IDE:

https://www.arduino.cc/en/reference/serial

Here is a very simple arduino sketch that will make the ATmega continously send out "ATmega"

``` arduino
void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("ATmega");
}
```


Here is an example arduino program that will make the ATmega continuously read from the Omega. Only after it reads the string "ArduinoDock2", it will send out the string "Received" to the Omega:

``` arduino
String readSerial;

void setup() {
  Serial.begin(9600);           // start serial for output at baud rate 9600
}

void loop() {
  delay(100);
  if (Serial.available() > 0){		// wait until there's serial data
    readSerial = Serial.readString();

    if (readSerial == "ArduinoDock2"){		//check is the received data is "ArduinoDock2"
    	Serial.print("Received");		//send the string "Received" to the Omega
    	readSerial = "";
    }
  }
}

```


### Using Omega2 Command Line

The direct and easy way to send and receive data on the Omega side is to use command lines. The Omega's UART1 can be seen as ttyS1 under the /dev directory:

```
ls /dev
```

ttyS1 can be considered as an intermediary linux file used for serial communication. To send data, for example 'ArduinoDock2', from the Omega we write to ttyS1 using the echo command. By default, the echo command will add new line at the end of the data, use -ne to avoid the new line.

```
echo -ne 'ArduinoDock2' > /dev/ttyS1
```

To show the received data from the ATmega we use the cat command similar to opening a file:

```
cat < /dev/ttyS1
```

We can also use the linux screen command for reading the data from the ATmega:


```
opkg update
```
```
opkg install screen
```
```
screen /dev/ttyS1 9600
```
,where 9600 is the baud rate. Use Ctrl+A+D to exit the screen mode.

### Using Python through pySerial

A more flexible method for handling serial communication is by using a python packaged called pySerial. However, this method will use more storage space. First download and install python2.7 and curl (tool to download files from an url) if they are not already installed:

```
opkg update
```
```
opkg install python curl
```

For easy installation of pySerial we download pip (a package manager for python files) into the python directory:

```
curl https://bootstrap.pypa.io/get-pip.py | python2.7
```

pySerial can be then installed through pip

```
pip install pyserial
```

Now we can start programming in python to send and receive data on the Omega. For the full documentation check out this link:

https://media.readthedocs.org/pdf/pyserial/latest/pyserial.pdf

Here is an example python code that will make the Omega continuously send "ArduinoDock2" until it read the response "Received" from the Atmega:

``` python
import serial

response = ""
while (response != "Received"):
        # Setup serial
        ser = serial.Serial(port='/dev/ttyS1', baudrate=9600, timeout=2)

        # Write string on UART1
        ser.write("ArduinoDock2")

        # Read 8 byte response
        response = ser.read(8)
        ser.cancel_read()
        print repr(response)
```

To run the python script, make a python file using vi editor and paste the code inside:

```
vi serialTest.py
```
and then run the python script:

```
python serialTest.py
```

### Using Omega2 as Serial Monitor

An useful tool on the Arduino IDE is the Serial Monitor, which displays the output of Serial.print(). We can use the Omega as the Serial Monitor by simply using the screen command from the previous section "Using Omega2 Command Line". You can open up two Omega SSH terminals and use one as a Serial Monitor.
