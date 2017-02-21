---
title: Seven Segment Display
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 8
---

## Controlling a 7-Segment Display {#starter-kit-07-seven-segment-display}

We've just learned about shift registers, now let's apply that knowledge to control a 7-segment Display so we can display numbers (and a few letters) in the physical world.

<!-- seven segment -->
```{r child = '../../shared/seven-segment.md'}
```

### Building the Circuit

Using the shift register and a few additional GPIOs from the Omega, we will control what's displayed on all four digits of the 7-segment display.

#### What You'll Need

* 1x Omega2 pluged into Expansion Dock
* 1x 7-Segment Display
* 1x Shift Register
* Resistors
    * 4x 330Ω
* Jumpers
    * 12x M-F
    * 13x M-M

#### Hooking up the Components

<!-- TODO: write out critical instructions -->
<!-- TODO: consider explaing the need for resistors (common gnd) -->

First things first, if you've done the previous experiment, keep the shift register wired up just like you had it. If you didn't, [check it out](#STK06-building-the-circuit) and wire the Shift Register to the Expansion Dock and Breadboard exactly the same way. For quick reference, we've included a wiring diagram between the shift register and the Expansion Dock below.

<!-- TODO: IMAGE diagram of shift register/dock/breadboard wiring -->


When you have the shift register wired up, it's time to connect it to the 7-segment display. First, we recommend you set up the resistors across the center first, and do all the wiring in one go.

For each resistor:

1. Pick a column.
1. Connect one end of the resistor to row `g`
1. Connect the other end to row `d`

We've included a diagram below for reference instead of instructions, as this one has a lot of wiring to do. All ends connecting to the 7-segment display require F jumper heads.

<!-- TODO: IMAGE wiring diagram of 7-seg to shift register and dock -->


### Writing the Code

We'll be developing a program that takes input from command line arguments when it's launched and displays them on the 7-segment display.

To accomplish this, we will write a new class that uses the shift register class we wrote for the previous experiment and introduces it's own variables and functions.

<!-- // [notes on the code]
// create a class that uses the shift reg class but specifically to control the 7seg display
//  * the 7seg class has self.shiftReg
//  functions:
//  * setup function to let the object know which gpios correspond to which functionality
//  * writing a single digit (have a dictionary in the 7seg class that maps each hex digit to a binary to be mapped to the segments)
//  * selecting which digit to write to (controls scan pins)
//  * function to write a value to a specific digit (combines the two above functions)
// command line arguments:
//  * make sure to check that a command line argument is present, if not, print an error message and exit the program
//  * input sanitization to ensure they only enter hex numbers (really good practise)
//  * write the sanitized input to the 7seg

-->

<!-- TODO: change numbering for removal of 06 -->

Now let's create a class named `STK07-sevenSegDisplay.py`.

``` python
import registerClass
import onionGpio
import time

class sevenSegment:
    digitMap = {
    "0": "00111111",
    "1": "00000110",
    "2": "01011011",
    "3": "01001111",
    "4": "01100110",
    "5": "01101101",
    "6": "01111101",
    "7": "00000111",
    "8": "01111111",
    "9": "01101111",
    "a": "01110111",
    "b": "01111100",
    "c": "10011100",
    "d": "01111010",
    "e": "10011110",
    "f": "10001110",
    "off": "00000000",
    "-": "01000000"
    }

	#Initializes the GPIO objects based on the pin numbers
	def __init__(self, dPin):
		self.shiftReg = registerClass.shiftRegister(1,2,3)
        for i in range (0,4):
    		self.digitPin[i] = onionGpio.OnionGpio(dPin[i])
    		self.digitPin[i].setOutputDirection(1)


	def showDigit(self, d, character):
		self.digitPin[d].setValue(0)
		self.shiftReg.outputBits(self.digitMap[character])
		self.digit[d].setValue(1)


	def clear(self):
		self.shiftReg.clear();
        for i in range (0,4):
    		self.digitPin[i] = onionGpio.OnionGpio(dPin[i])
```

Once that's out of the way, create `STK07-seven-seg-display` and paste the following in it:

``` python
import registerClass
from sevenSegDisplay import sevenSegment
import time

sevenDisplay = sevenSegment(11,18,19,0)
sevenDisplay.setup()

def __main__():
    # if script was called with no arguments
    if len(sys.argv) == 1:
        print "Please input a hex string, eg. 0x12ab"
        return -1

    # if script was called with too many arguments
    elif len(sys.argv) > 2:
        print "Too many arguments. Please input only one hex number."
        return -1

    # read the hex string from the argument
    inputHexString = sys.argv[1]
    inputLen = len(inputHexString)

    # attempt to print out the hex string
    while True:
        for i in range(inputLen):
        	sevenDisplay.showDigit(i,inputHexString[i])
```

To see it in action, make sure you have `registerClass.py`, `sevenSegDisplay.py` and `STK07-seven-seg-display.py` in your `/root/` directory.

Then run the following:

``` bash
python /root/STK07-seven-seg-display.py
```


#### What to Expect

The Python code above should ask you for a hex string, then print the digits one by one on to the 7 segment display. Infinite loops here as well, and you can exit with `Ctrl-C`

Now you may be wondering if what you saw is expected behaviour - yes. However you probably guessed that it really should be displaying them all at once.

If you'd like to see how that looks, we've provided a shell script below that does this properly.


``` bash
#!/bin/sh

input=$1

pref1="$(echo $input | sed -e 's/^\(.\).*/\1/')"
pref2="$(echo $input | sed -e 's/^.\(.\).*/\1/')"
chr1="$(echo $input | sed -e 's/^..\(.\).*/\1/')"
chr2="$(echo $input | sed -e 's/^...\(.\).*/\1/')"
chr3="$(echo $input | sed -e 's/^....\(.\).*/\1/')"
chr4="$(echo $input | sed -e 's/^.....\(.\).*/\1/')"
# TODO: add a check for chr5; if chr5 is not blank, exit (4 digits only)

if ! [[ "$pref1" == "0" && "$pref2" == "x" ]]; then
    echo "Please input a hex number in the following format: 0x12ab"
    exit
fi

mapDigit(){
    if [ "$1" == "0" ]; then
        echo "0 0 1 1 1 1 1 1"
    elif [ "$1" == "1" ]; then
        echo "0 0 0 0 0 1 1 0"
    elif [ "$1" == "2" ]; then
        echo "0 1 0 1 1 0 1 1"
    elif [ "$1" == "3" ]; then
        echo "0 1 0 0 1 1 1 1"
    elif [ "$1" == "4" ]; then
        echo "0 1 1 0 0 1 1 0"
    elif [ "$1" == "5" ]; then
        echo "0 1 1 0 1 1 0 1"
    elif [ "$1" == "6" ]; then
        echo "0 1 1 1 1 1 0 1"
    elif [ "$1" == "7" ]; then
        echo "0 0 0 0 0 1 1 1"
    elif [ "$1" == "8" ]; then
        echo "0 1 1 1 1 1 1 1"
    elif [ "$1" == "9" ]; then
        echo "0 1 1 0 1 1 1 1"
    elif [[ "$1" == "a" || "$1" == "A" ]]; then
        echo "0 1 1 1 0 1 1 1"
    elif [[ "$1" == "b" || "$1" == "B" ]]; then
        echo "0 1 1 1 1 1 0 0"
    elif [[ "$1" == "c" || "$1" == "C" ]]; then
        echo "0 1 0 1 1 0 0 0"
    elif [[ "$1" == "d" || "$1" == "D" ]]; then
        echo "0 1 0 1 1 1 1 0"
    elif [[ "$1" == "e" || "$1" == "E" ]]; then
        echo "1 0 0 1 1 1 1 0" # fix
    elif [[ "$1" == "f" || "$1" == "F" ]]; then
        echo "1 0 0 0 1 1 1 0" # fix
    else
        echo "Invalid hex digit $1."
        exit
    fi
}

dig1=$(mapDigit $chr1)
dig2=$(mapDigit $chr2)
dig3=$(mapDigit $chr3)
dig4=$(mapDigit $chr4)

# setup shift register pins
echo 1 >/sys/class/gpio/export # data
echo 3 >/sys/class/gpio/export # latch
echo 2 >/sys/class/gpio/export # clock

# setup digit pins
# all directions are from left
echo 11 >/sys/class/gpio/export # digit 1
echo 18 >/sys/class/gpio/export # digit 2
echo 19 >/sys/class/gpio/export # digit 3
echo 0 >/sys/class/gpio/export # digit 4

# set direction for the pins above (out/input)
echo out >/sys/class/gpio/gpio1/direction
echo out >/sys/class/gpio/gpio2/direction
echo out >/sys/class/gpio/gpio3/direction

echo out >/sys/class/gpio/gpio11/direction
echo out >/sys/class/gpio/gpio18/direction
echo out >/sys/class/gpio/gpio19/direction
echo out >/sys/class/gpio/gpio0/direction

# write out values from the SR's buffer to the outputs
latchSR (){
	echo 1 >/sys/class/gpio/gpio3/value
	echo 0 >/sys/class/gpio/gpio3/value
}

# pulse the SR clock and shift in one bit from the data line
pulseClock (){
	echo 1 >/sys/class/gpio/gpio2/value
	echo 0 >/sys/class/gpio/gpio2/value
}

# set one digit
setOneDig(){

	echo out >/sys/class/gpio/gpio1/direction

	for i in $1 $2 $3 $4 $5 $6 $7 $8
	do
		#echo  
		echo $i >/sys/class/gpio/gpio1/value
		pulseClock
	done

	latchSR
}

# turn off all the pins (enable pins are active LOW)
initDigPins (){
	echo 1 >/sys/class/gpio/gpio0/value
	echo 1 >/sys/class/gpio/gpio18/value
	echo 1 >/sys/class/gpio/gpio19/value
	echo 1 >/sys/class/gpio/gpio11/value
}

initDigPins


# play around with this to see how the gpio#s correspond to the digits
while true; do

echo 0 >/sys/class/gpio/gpio0/value
setOneDig $dig3
echo 1 >/sys/class/gpio/gpio0/value

# enable the digit
echo 0 >/sys/class/gpio/gpio19/value
setOneDig $dig1
echo 1 >/sys/class/gpio/gpio19/value

echo 0 >/sys/class/gpio/gpio11/value
setOneDig $dig2
echo 1 >/sys/class/gpio/gpio11/value

echo 0 >/sys/class/gpio/gpio18/value
setOneDig $dig4
echo 1 >/sys/class/gpio/gpio18/value
done
```

To run it, copy the code to `/root/STK07-seven-seg-display.sh` then run the following with a hex number as the first argument:

```
sh /root/STK07-seven-seg-display.sh [hex number]
```

Trust us when we say these two scripts are intended to be doing the same thing. If you're wondering why? Read on!


### A Closer Look at the Code

To display numbers on the 7-Segment display, we mapped the outputs to binary using a **dictionary**. We put a class inside a class to better encapsulate the operation of the physical components. However the end result was limited by the software we used: we wanted and expected thed 7-segment display to light up all at once, but our script couldn't make it happen fast enough. In fact there's no way in Python to get our inteded behaviour without basically calling the shell commands used in the script through Python.


#### Software Limitations

In this experiment, software and hardware come together to produce behaviour we didn't intend. The code runs as well as it possibly can, and the hardware does its best to operate from the signals its given, but it ultimately doesn't make the result workable. The root cause is the way the libraries are programmed. The GPIOs are operated by reading and writing to files, and the `onionGpio` module operates this in a very safe and consistent way through our C library - meaning it's quite slow.

The reason why the shell scripted works is because it skips a bunch of unnecessary safety steps in writing to the GPIO outputs. If your code is trying to push the boundaries of the hardware, it necessitates a deeper understanding of the hardware.


#### Classes using Classes

Despite this particular experiment's outcomes, encapsulation is still good practice. The way we implemented the `SEVEN_SEG_CLASS_NAME` and `ShiftRegister` classes is a good demonstration of why.

The `SEVEN_SEG_CLASS_NAME` class makes use of code that already exists, and builds upon that to fulfill a niche functionality. Here, we instantiate the `ShiftRegister` class within the `SEVEN_SEG_CLASS_NAME` class - this means `SEVEN_SEG_CLASS_NAME` can make use of all the functionality of the internal `ShiftRegister` object without being a shift-register.

Logically separating the devices like this makes it easier in complicated projects to think about the pieces working together, instead of what each individual line of code does. Our script can then call on the seven seg functions to display things without needing to bother with the intricasies of the shift register. Vice versa, we can use the shift register to do other things by directly instantiating an object from `ShiftRegister`.


#### Dictionary

Also known as 'hash tables', though not strictly the same. Dictionaries work in programming much the same way as in real life. By keying a definition to a name or title, you can look it up. Python has a built-in dictionary data type, which we make use of here to map out letters and numbers to the shift. Dictionaries are **immutable** - they cannot be changed after they are created.

We use a dictionary here as a translation between string characters and the shift register representation of it. We can simply insert `digitMap[<character>]` to the shift register display function and let the `ShiftRegister` object sort out the rest without needing to copy-paste the binary code.



Next: [Reading a One-Wire Temperature Sensor](#starter-kit-reading-one-wire-temperature-sensor)
