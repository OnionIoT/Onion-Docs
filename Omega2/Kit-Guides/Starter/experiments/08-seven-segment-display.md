---
title: Seven Segment Display
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 8
---

## Controlling a 7-Segment Display {#starter-kit-07-seven-segment-display}

We've just learned about shift registers, now let's apply that knowledge to control a 7-segment Display so we can display numbers (and a few letters) in the physical world. We'll construct a circuit that connects the Omega to the shift register and the shift register to the 7-segment display. The Omega will send serial signals to the shift register, and those signals will be transformed into numbers and letters by the 7-segment display.

// TODO: add a description of what we're going to do in this experiment: wire up the 7-seg to the shift register from last time, write a program and see how it goes, hint that there's more to be done here

// TODO: add a note that this experiment builds on the previous one, so they should make sure they complete that one before they move on to this one

<!-- seven segment -->
```{r child = '../../shared/seven-segment.md'}
```

### Building the Circuit

Using the shift register and a few additional GPIOs from the Omega, we will control what's displayed on all four digits of the 7-segment display.

// TODO: spice up this sentence, sounds so boring
// TODO: make sure to point out that we need to use the shift register to make up for the fact we have a limited amount of GPIOs on the Omega

// TODO: include a block diagram of the system

#### What You'll Need

// TODO: make this match the rest of the 'What You'll Need' sections

* 1x Omega2 plugged into Expansion Dock
* 1x 7-Segment Display
* 1x Shift Register
* 4x 330Ω Resistors
* Jumpers
    * 12x M-F
    * 13x M-M

#### Hooking up the Components


// TODO: pls fix up this sentence, i changed it but it needs to be nice-ified

First things first, if you've done the previous experiment, keep the shift register wired up just like you had it. If you skipped the previous experiment, we recommend you check it out before moving on to this experiment since we build on what we've done!
 For quick reference, we've included a wiring diagram between the shift register and the Expansion Dock below.

<!-- TODO: IMAGE diagram of shift register/dock/breadboard wiring -->

> TODO: a note about why common ground is important (all components need to have the same baseline for logical low)

1. Connecting your Shift Register

  - Start by plugging in your shift register across the channel so that the each pin has its own row.
  - Connect pin 16 and pin 10 to the positive rail (Vcc)
  - Connect pin 8 and pin 13 to the negative rail (Ground)

// TODO: add explanation of why we need the resistors
When you have the shift register wired up, it's time to connect it to the 7-segment display. First, we recommend you set up the resistors across the center first, and do all the wiring in one go.

We've included a diagram below for reference instead of instructions, as this one has a lot of wiring to do and they end up going every which way. Note that all ends connecting to the 7-segment display require F jumper heads - that's where your M-F jumpers will be used.

<!-- TODO: IMAGE wiring diagram of 7-seg to shift register and dock -->

Once you've connected the 7-segment display to the Omega and shift register, it's all done!

``` {r child = '../../shared/wiring-precautions.md'}
```


### Writing the Code

We'll be developing a program that takes input from command line arguments when it's launched and displays them on the 7-segment display.

// TODO: include a block diagram of the code and a description of what we're going to be doing from a high level

To accomplish this, we will write a new class that uses and builds upon the shift register class from the previous experiment.

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

Now that we have a class to control the 7-seg display, let's write a program to use the class and control the display! Create `STK08-seven-seg-display` and paste the following in it:


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

// TODO: need to describe what we're doing: changing the scan, setting a value, then changing the scan, setting a value, etc


To see it in action, make sure you have `registerClass.py`, `sevenSegDisplay.py` and `STK08-seven-seg-display.py` in your `/root/` directory.

Then run the following:

``` bash
python /root/STK07-seven-seg-display.py
```


### What to Expect

// TODO: this section was 100% phoned-in, rewrite this part with some life and not sentence fragments
The Python code above should ask you for a hex string, then print the digits one by one on to the 7 segment display. Infinite loops here as well, and you can exit with `Ctrl-C`

// TODO: gif: add a gif of what happens
// TODO: include a description of what is expected behaviour

Now you may be wondering if what you saw is expected behaviour - yes. However you probably guessed that it really should be displaying them all at once.

// NOTE: moved the bash script to the bottom




### A Closer Look at the Code

// TODO: let's describe why the Python implementation was slow, and then after this H3 section, describe what is to be done differently and then show the bash implementation

To display numbers on the 7-Segment display, we mapped the outputs to binary using a **dictionary**. We put a class inside a class to better encapsulate the operation of the physical components. However the end result was limited by the software we used: we wanted and expected thed 7-segment display to light up all at once, but our script couldn't make it happen fast enough. In fact there's no way in Python to get our inteded behaviour without basically calling the shell commands used in the script through Python.


#### Software Limitations

// NOTE: this is good, but it's not really a software limitation, it's more of a library specific thing
// * the library needs to:
//  1. take control of the gpio (export the GPIO)
//  2. set the direction to output
//  3. set the output value
//  4. release the gpio (unexport the gpio)
// * each of the above actions requires a file write, so for each segment we set, there are 4 file writes
// TODO: update this section to mention the above (and to go inline with the fact that we haven't yet introduced the bash script)


In this experiment, software and hardware come together to produce behaviour we didn't intend. The code runs as well as it possibly can, and the hardware does its best to operate from the signals its given, but it ultimately doesn't make the result workable. The root cause is the way the libraries are programmed. The GPIOs are operated by reading and writing to files, and the `onionGpio` module operates this in a very safe and consistent way through our C library - meaning it's quite slow.




#### Classes using Classes

// TODO: fix this SEVEN_SEG_CLASS_NAME placeholder

Despite this particular experiment's outcomes, encapsulation is still good practice. The way we implemented the `SEVEN_SEG_CLASS_NAME` and `ShiftRegister` classes is a good demonstration of why.

The `SEVEN_SEG_CLASS_NAME` class makes use of code that already exists, and builds upon that to fulfill a niche functionality. Here, we instantiate the `ShiftRegister` class within the `SEVEN_SEG_CLASS_NAME` class - this means `SEVEN_SEG_CLASS_NAME` can make use of all the functionality of the internal `ShiftRegister` object without being a shift-register.

Logically separating the devices like this makes it easier in complicated projects to think about the pieces working together, instead of what each individual line of code does. Our script can then call on the seven seg functions to display things without needing to bother with the intricasies of the shift register. Vice versa, we can use the shift register to do other things by directly instantiating an object from `ShiftRegister`.

// TODO: need to adjust the above paragraph - it makes good points but they should be better organized to showcase the two ideas below:
// * code-reusability: we wrote an independent class for the shift register and now we're just using it like a lego block to build something new. can just focus on the new code we need for the 7seg.
// * abstraction: the shift register class allows us to use the shift register without needing to know the nitty-gritty of how it works. in this case we just need it to set certain outputs, we use the function to make that happen in one line and don't need to worry about how it happens. this type of thing makes it easier to think about how the different pieces of the project work together

#### Dictionary

// TODO: i like the parallel to real dictionaries but the fact that the key indexes a value needs to be more clear.

// TODO: umm, dictionaries can totally be changed after they're created...

Also known as 'hash tables', though not strictly the same. Dictionaries work in programming much the same way as in real life. By keying a definition to a name or title, you can look it up. Python has a built-in dictionary data type, which we make use of here to map out letters and numbers to the shift. Dictionaries are **immutable** - they cannot be changed after they are created.

// TODO: note that the below was the original
We use a dictionary here as a translation between string characters and the shift register representation of it. We can simply insert `digitMap[<character>]` to the shift register display function and let the `ShiftRegister` object sort out the rest without needing to copy-paste the binary code.
// TODO: this is re-written:
We use a dictionary here as a translation between characters and the value that needs to be written to the 7-segment display in order to display that character. When we insert `digitMap[1]` to the shift register display function, the function is actually getting the value indexed by `1` in the `digitMap` dictionary, so the function will get `00111111`, the value it needs to properly show a `1` on the display, and the code will still be very human readable.
// TODO: need to explain the concepts we're introducing here very clearly, this would be very confusing to a beginner, if you're unsure of how something works, please ask before writting


### A Better Way?

// TODO: reiterate that our Python implementation didn't produce a nice result, include a brief recap as to why,
// TODO: say what we're going to be doing differently:
//  * using bash (need a few sentences about bash, how its basically a bunch of command line utilities and therefore it runs really fast)
//  * we've changed how we're going to be accessing/controlling the GPIOs
If you'd like to see how that looks, we've provided a shell script below that does this properly.


``` bash
#!/bin/sh

input=$1
len=${#input}

pref1="$(echo $input | sed -e 's/^\(.\).*/\1/')"
pref2="$(echo $input | sed -e 's/^.\(.\).*/\1/')"
chr1="$(echo $input | sed -e 's/^..\(.\).*/\1/')"
chr2="$(echo $input | sed -e 's/^...\(.\).*/\1/')"
chr3="$(echo $input | sed -e 's/^....\(.\).*/\1/')"
chr4="$(echo $input | sed -e 's/^.....\(.\).*/\1/')"
# TODO: add a check for chr5; if chr5 is not blank, exit (4 digits only)

if  [[ "$len" -ge "7" || "$pref1" != "0" || "$pref2" != "x" ]]; then
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


// TODO: include a section describing the above code

// TODO: include a note saying that this type of code necessitates a deeper understanding of how the hardware and software interact




Next: [Reading a One-Wire Temperature Sensor](#starter-kit-temp-sensor)
