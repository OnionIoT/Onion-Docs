---
title: Using a Shift Register
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 7
---

# Using a Shift Register to Control a Bunch of LEDs

Shift registers are very useful tools; using a few GPIOs connected to a shift register, we can increase the number of output data pins that are available to us.

In this experiment, we'll be using a shift register to control eight LEDs, but we'll only be using three GPIOs on the Omega.

<!-- // TODO: update this number if required -->
<!-- should be 3 GPIOs I think -->


## Shift Register
<!-- {{!insert 'shift-register'}} -->


A shift register is an external integrated circuit (IC) that can be used to expand the number of output pins available to us. Essentially they let you take serial inputs (one bit after the other) and output them in parallel.


So how does this work? Well, we use the Omega to send the input to the shift register using one data pin, and the shift register outputs each individual bit to its eight data pins. In order to sync everything up, we also need to connect two of the Omega's GPIOs to the shift register's clock pins. Doing this makes sure that the Omega knows when to send each bit that is to be outputted in parallel.

That last paragraph was pretty technical so as an example if you were to send `1011` from the Omega to the shift register it would get 1, 0, 1, 1, on four of its data output pins. This would be sent out in parallel making it seem like there were 4 data pins connected to the Omega!

<!-- TODO: Add an illustration of the shift register where you send 1011 on data pin, and it shows up as 1, 0, 1, 1 on the output pins -->


<!-- // explanation of a shift register, an external integrated circuit (ic) that takes serial input and provide the data in parallel
// it allows us to essentially expand the number of output pins available to us
// the omega can provide data serially using one data pin, and then the shift register outputs it on its eight data pins

// illustration of how a shift register works
//  - can be simple (clock, serial data in, eight outputs)
//  - explanation of the diagram
//  - the key takeaway should be, pass in 0101 get 0, 1, 0, 1 on the outputs -->



## Controlling a Shift Register
<!-- {{!insert 'shift-register-control'}} -->

There are two clocks on the shift register included in your kit: SRCLK (serial clock) and the RCLK (register clock).

The SRCLK is used to set up the pins on the shift register. When the SRCLK is pulled **high** reads the value on the SER pin. How does this let me control LEDs again? Well, say you have 8 LEDs hooked up to the shift registers outputs, and we want to turn on the 1st, 3rd and the 8th LED. So what we do is clear out the register so all LEDs are off. Then we put in one high (1), four lows (0, 0, 0, 0), one high (1), one low (0), then add another high (1). This leaves us with `10000101`.

>Some quick math to help you out: The first value was placed at position 1, and then moved over 4 times to position 5 using the four lows (0s). Then, when we add the second value, the first value is shifted to position 6. Then we move all the values over by 1 pushing the first value to position 7. Finally, adding the last value shifts all the current values over by 1, resulting in the first value being pushed into position 8.


The RCLK is used as a signal to set the output pins to the values to those of the new shift register values. When this is pulled **high** the values that the SRCLK set up are sent out to the output pins.


You can refer to [the SN74hc595 datasheet](http://www.ti.com/lit/ds/symlink/sn74hc595.pdf) for more information. The clock cycles can be found on page 8.

<!-- // introduce the idea of a clock, explain that it provides the shift register with a signal to read the data that's currently on the serial data in pin. make sure to note that the data on the serial data in pin needs to be settled before the clock edge!

// show how changing the data on the serial data pin will affect the outputs
// good place to introduce the latching register ie displaying the values of each step. mention that this can be used to set up your output values (pass in all of the serial data) before actually outputting it -->


## Building the Circuit

This circuit is quite involved but we're going to split it up into 3 parts: connecting the shift register, connecting your Omega, and connecting the LEDs.
It's going to be essentially the same thing as the second experiment but we're going to use 8 LEDs and a shift register.


The GPIOs that are going to be used in this experiment are:

* 1
* 2
* 3

These have been highlighted in the image below:

<!-- TODO: add image of expansion dock with correct pins highlighted -->

### What You'll Need

We'll be building a circuit on your breadboard using the following components:

* Omega2 plugged into Expansion Dock
* 8x LEDs
* 17x Jumper Wires
* 8x <!-- TODO: Find resistance value --> Resistors
* Breadboard
* Shift Register

### Hooking up the Components


The IC should be plugged in across the channel of your breadboard (the slot running down the middle separating the `abcde` columns from the `fghij` columns). If you don't do this you will short out the pins across your IC. You may need to bend the pins just a bit in order to get it to fit.

Now there are a lot of connections you'll need to make in order to power the IC and use it with the Omega, so we'll go through it step by step. We'll be referring to each pin by the numbers provided in the diagram above.

>Note: Your IC will have a semi-circle indentation that indicates "up". Make sure that you plug it in properly.

1. Connecting your Shift Register

  - Start by plugging in your shift register across the channel so that the each pin has its own row.
  - Connect pin 16 and pin 10 to the positive rail (Vcc)
  - Connect pin 8 and pin 13 to the negative rail (Ground)

  <!-- TODO: Insert picture of this stage -->

2. Connecting your Omega

  - Connect GPIO 1 to pin 14 on the shift register
  - Connect GPIO 2 to pin 11 on the shift register
  - Connect GPIO 3 to pin 12 on the shift register
  - Connect the Ground header to the negative rail on the breadboard
  - Connect the 3.3V header to the positive rail on the breadboard

  <!-- TODO: Insert picture of this stage -->


3. Connecting your LEDs

  - Connect 8 LEDs the same way we did in experiment 2, (cathod in ground, anode connected to resistor)
  - Connect the jumper wires from the LEDs to the output pins on the shift register. In order from first to last these are pin 15 (QA), followed by pin 1(QB) to pin7(QH)

  <!-- TODO: Insert picture of this stage -->

And there you have it, it's all wired up and ready to run. Now let's take a look at the code we're going to use to control our shift register.

<!-- //  * talk about how the IC should be plugged in across the channel of the breadboard (have this note in a markdown file so it can be easily reused)

//  * explain all of the wiring from omega->shift reg
//    * explain each of the lines running from the Omega and what they do - according to the names from the controlling a shift register section
 -->



## Writing the Code

We're going to split our code into two files; one for our main program, and one for our shift register. We'll start with the shift register file. Create a file in your root directory named `registerClass.py` and copy the code below into its contents:

``` python
import onionGpio

class shiftRegister:
		#Initializes the GPIO objects based on the pin numbers
		def __init__(self, dataPin, serialClock, registerClock):
			self.ser = onionGpio.OnionGpio(dataPin)
			self.srclk = onionGpio.OnionGpio(serialClock)
			self.rclk = onionGpio.OnionGpio(registerClock)

		#Pulses the latchpin
		def latch(self):
			self.rclk.setValue(1)
			self.rclk.setValue(0)

		# Pulses the Serial Clock 8 times in and then latches to clear all the LEDs
		def clear(self):
			self.ser.setValue(0)
			for x in range(0, 8): #Clears out all the values currently in the register
				self.srclk.setValue(1)
				self.srclk.setValue(0)
			self.latch()


		#Sets the GPIOs to output with an initial value of zero
		def setup(self):
			self.ser.setOutputDirection(0)
			self.srclk.setOutputDirection(0)
			self.rclk.setOutputDirection(0)

			self.clear()

		#Sets the serial pin to the correct value and then pulses the serial clock to shift it in
		def inputBit(self, inputValue):
			self.ser.setValue(inputValue)
			self.srclk.setValue(1)
			self.srclk.setValue(0)

		#Splits the input values into individual values and inputs them. The pulses the latch pin to show the output.
		def outputBits(self, inputValues):
			inputValues = str(inputValues) # Converts the binary value into a string (11000000 -> "11000000")
			mylist = list(inputValues) # Splits the string into a list of individual characters ("11000000" -> ["1","1","0","0","0","0","0","0"])
			for x in mylist:
				x = int(x) # Transforms the character back into an int ("1" -> 1)
				self.inputBit(x)
			self.latch()
```

This file contains a single class that allows us to write a really clean main program. The main component here is the `__init__` function which initializes the class object.

The next component of our code is the main program, you can name this file whatever you'd like but make sure its in the same directory as `registerClass.py`:

``` python
from registerClass import shiftRegister
import signal

shiftRegister = shiftRegister(1,2,3) #Data pin is GPIO 1, serial clock pin is GPIO 2, Latch pin is GPIO 3

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

signal.signal(signal.SIGINT, signal_handler)


shiftRegister.setup()
value = 192
interrupted = False
while 1:

	for x in range(0, 12):
		binValue = "{0:08b}".format(value) # Transforms the value into a binary number (192 = 11000000)
		shiftRegister.outputBits(binValue) # Sends the 8 bit value to be output by the shift register
		if x < 6:
			value >>= 1 #Shifts the value right by one (11000000 -> 01100000)
		else:
			value <<= 1 #Shifts the value left by one (01100000 -> 11000000)
	if interrupted:
		shiftRegister.clear()
		break
```

The main program imports the class we wrote and creates an object `shiftRegister` using the class. We then use that object to control our LEDs through the shift register.


<!-- // create a class to abstract away all of the shift register operations
//  * input 8 data bits, the function will take care of the eight data shifts, then latch the output at the end
//  * setup function to let the object know which gpios correspond to which functionality
//  * separate functions for:
//    - inputting a single data bit
//    - latching the output
//    - clearing the values
//  * use all of these functions in that one function to pass in 8 different outputs

// note that the class should be in its own file and imported in the final program

// for loop using the object to display on all the leds
//  there should be two leds on at a time, have it run all the way to the left, and then all the way to the right -->


### What to Expect


What this will do is light up two of your LEDs, and then move them all the way to one side, and back again (think Kitt from Knight Rider).

You can terminate the code by pressing `ctrl+c` or `cmd+c` for MACs.

<!-- // explain that the animation will be Knight Rider Kitt style: maybe throw in a gif for nostalgia
//  - it will run all the way left and then all the way right over and over again -->

### A Closer Look at the Code

<!-- // an overview of the code -->

We've introduced some new concepts in this experiment in order to create cleaner and more robust code. Let's examine some of these concepts.


#### Creating and Importing Modules

<!-- // describe how the import process works, make sure to note how the directory structure has to fit -->

A **Module** is a file containing Python definitions and statements. This can be used to split your project into multiple files for easier maintenance. The `registerClass.py` file is an example of a self-made module that we've imported. Some modules are built in to Python; some examples are `time` which you may have used before, and `signal` which is used in our main program.


#### Creating and Using Classes

Classes are a way to create a template for creating objects in our code. For example the class we created is a code template that represents having a shift register on our circuit. If we wanted to we could connect another shift register to our circuit, and easily create a new object using our shiftRegister class.

When we've created our class object we also get access to the functions defined by the class. We can call these functions through our instantiated object:

``` python
shiftRegister.outputBits(binValue)
```

``` python
def outputBits(self, inputValues):
  inputValues = str(inputValues) # Converts the binary value into a string (11000000 -> "11000000")
  mylist = list(inputValues) # Splits the string into a list of individual characters ("11000000" -> ["1","1","0","0","0","0","0","0"])
  for x in mylist:
    x = int(x) # Transforms the character back into an int ("1" -> 1)
    self.inputBit(x)
  self.latch()
```

You'll also notice that we include `self` in our Python class functions. This is necessary so that we are always referencing the variable or function that pertains to the current object.

Finally, you can import other modules into your self-made modules. In our shiftRegister class we use `onionGpio` in order to create our GPIO objects, which is made possible by importing `onionGpio`.

<!-- // explanation of Classes
//  - definition of Classes
//  - using classes
//  - each class becomes an object when you instantiate it
//    - can call functions from the object, etc
//    - if we had two shift registers, we could have two objects to run the two different ones
//  - talk about how class functions can use other class functions -->

#### Exiting Infinite Loops

When using GPIOs it is important that you exit your code properly so that your GPIOs are properly freed and you don't get locked out of using them. This can be quite difficult when we create an infinite loop so we've included a solution to that.

When inspecting our main program we see a function defined as `signal_handler`. We also see an signal listener in the form of

```
signal.signal(signal.SIGINT, signal_handler)
```

This listener is listening for an interrupt from the user in order to run the signal handler code. So when you enter `ctrl+c` or `cmd+c` you are sending a *Keyboard Interrupt* which is then handled by the function. This way your code will always finish a cycle before exiting, thus making sure that your GPIOs are properly freed.
