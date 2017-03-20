---
title: Using a Shift Register
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 7
---

## Using a Shift Register to Control a Bunch of LEDs {#starter-kit-using-shift-register}

Shift registers are very useful tools; using a few GPIOs connected to a shift register, we can increase the number of output data pins that are available to us.

In this experiment, we'll be using a shift register to control eight LEDs, but we'll only be using three GPIOs on the Omega.

<!-- // DONE: update this number if required -->


<!-- Shift Register -->
```{r child = '../../shared/shift-register.md'}
```

### Building the Circuit {#starter-kit-using-shift-register-building-the-circuit}

This circuit is quite involved but we're going to split it up into 3 parts:

1. Connecting the shift register
1. Connecting the LEDs
1. Connecting your Omega

It's going to be similar to the second experiment, but this time we're going to use 8 LEDs and a shift register. Refer to the [circuit building instructions in Experiment 2](#starter-kit-multiple-leds-building-the-circuit), except you will be connecting 8 LEDs to the shift register instead of the Omega's GPIOs.

The GPIOs that are going to be used in this experiment are:

* 1
* 2
* 3

These have been highlighted in the image below:

<!-- TODO: IMAGE of expansion dock with correct pins highlighted -->

#### What You'll Need

We'll be building a circuit on your breadboard using the following components:

* Omega2 plugged into Expansion Dock
* Breadboard
* Shift Register
* 8x LEDs
* 17x M-M Jumper Wires
* 8x 200Ω Resistors

#### Hooking up the Components

Before we get to working with our fancy chip, we need to learn how to properly orient them on the breadboard so we don't plug them in upside-down!

<!-- IC direction marker -->
```{r child = '../../shared/ic-direction-marker.md'}
```

When plugging in any IC into a breadboard, it should be plugged in across the gap in the middle. If you don't do this, you will short-circuit the pins of your IC (remember that the rows on each side are all shorted). 

You may need to bend the pins just a bit in order to get it to fit. Don't worry about it so much; electronics are actually pretty tough and won't be hurt by a little bit of manual pin bending.

There are several wiring connections you'll need to hook up, so we'll go through it step by step. We'll be referring to each pin by the numbers provided in the pinout diagram above.

##### Connecting your Shift Register

```{r child = '../../shared/shift-register-wiring-instructions.md'}
```

<!-- TODO: IMAGE picture of this stage -->

##### Connecting your LEDs

1. Connect 8 LEDs the same way we did in experiment 2, starting at row 16 on the breadboard and going down.
1. When connecting them, do it the other way around: with the cathodes on the **right** side and the anodes on the **left** side. This will make our wiring easier later.
1. Connect the jumper wires from the shift register's data lines according to the following table:

| Pin Name | Pin # | LED # |
|-|-|-|
| QA | 15 | 1 |
| QB | 1  | 2 |
| QC | 2  | 3 |
| QD | 3  | 4 |
| QE | 4  | 5 |
| QF | 5  | 6 |
| QG | 6  | 7 |
| QH | 7  | 8 |

The wire for QA starts on the right side of the chip and goes to the 1st LED, while the wires for the other 7 start on the left side and should go straight down the breadboard. 

<!-- TODO: IMAGE picture of this stage -->

##### Connecting your Omega to the Shift Register

1. Connect the GND pin on the Expansion Dock to the Vcc rail.
1. Connect GPIO1 to `SER` (pin 14).
1. Connect GPIO2 to `SRCLK` (pin 11).
1. Connect GPIO3 to `RCLK` (pin 12).
1. Connect the 3.3V pin on the Expansion Dock to the ground rail.

  <!-- TODO: IMAGE picture of this stage -->

And there you have it, it's all wired up and ready to run! Now let's take a look at the code we're going to write.

<!-- //  DONE: * talk about how the IC should be plugged in across the channel of the breadboard (have this note in a markdown file so it can be easily reused)

//  * explain all of the wiring from omega->shift reg
//    * explain each of the lines running from the Omega and what they do - according to the names from the controlling a shift register section
-->

### Writing the Code

Our code will be split into two files; one for our main program, and one for our shift register. We'll start with the shift register file. Create a file in your root directory named `registerClass.py` and copy the code below into its contents:

``` python
import onionGpio

class shiftRegister:
    #Initializes the GPIO objects based on the pin numbers
    def __init__(self, dataPin, serialClock, registerClock):
        self.ser = onionGpio.OnionGpio(dataPin)
        self.srclk = onionGpio.OnionGpio(serialClock)
        self.rclk = onionGpio.OnionGpio(registerClock)
        self.setup()

    #Pulses the latchpin
    def latch(self):
        self.rclk.setValue(0)
        self.rclk.setValue(1)
        self.rclk.setValue(0)
    # Pulses the Serial Clock 8 times in and then latches to clear all the LEDs
    def clear(self):
        self.ser.setValue(0)
        for x in range(0, 8): #Clears out all the values currently in the register
            self.srclk.setValue(0)
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
        self.srclk.setValue(0)
        self.srclk.setValue(1)
        self.srclk.setValue(0)
        

    #Splits the input values into individual values and inputs them. Then pulses the latch pin to show the output.
    def outputBits(self, inputString):
        bitList = list(inputString) # Splits the string into a list of individual characters ("11000000" -> ["1","1","0","0","0","0","0","0"])
        bitList = bitList[::-1]      # reverses the string to 
        for bit in bitList:
            bit = int(bit) # Transforms the character back into an int ("1" -> 1)
            self.inputBit(bit)
        self.latch()
```

This file contains a single class that allows us to use and reuse it wherever we like. The main component here is the `__init__` function which initializes the class object.

Now let's write the main script. Create a file in the same directory called `STK06-using-shift-register.py` and paste the following code in it:

<!-- TODO: this code doesn't actually work, it lights up one LED then shifts the light in one direction. Then it goes blank for a while then repeats again from the top -->

``` python
from registerClass import shiftRegister
import signal

# Data pin is GPIO 1, serial clock pin is GPIO 2, Latch pin is GPIO 3
shiftRegister = shiftRegister(1,2,3)

# Signal interrupt handler to exit after the animation has finished when Ctrl-C is pressed
def signal_handler(signal, frame):
    global interrupted
    interrupted = True

signal.signal(signal.SIGINT, signal_handler)


# To create the animation on the LEDs through the shift register,
# we use a binary number instead of a string. We can move the lights
# around by bitshfting instead of string operations.
value = 0b11000000
interrupted = False

while True:
    # this animation has 12 different frames, so we'll loop through each one
    for x in range(0, 12):
        # we need to transform the binary value into a string only when sending it to the shift register
        bytestring = format(value, '08b')
        shiftRegister.outputBits(bytestring)
        # now we are free to manipulate the binary number using bitshifts

        # if in the first half (6 frames) of the animation, move the LEDs to the right
        if x < 6:
            value >>= 1 # Shifts all digits right by one (11000000 -> 01100000)
        # else we must be in the second half, so move the LEDs to the left
        else:
            value <<= 1 # Shifts all digits left by one (01100000 -> 11000000)
    # interrupt (Ctrl-C) handler
    if interrupted:
        shiftRegister.clear() # turn off the LEDs
        break
```

The main program loads the class we wrote and creates a `shiftRegister` object. We then use that object to control our LEDs through the shift register.


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

#### What to Expect

What this will do is light up two of your LEDs, and then move them all the way to one side, and back again (think Kitt from Knight Rider).

You can terminate the code by pressing `Ctrl-C` or `Cmd-C` on Mac OS.

<!-- // explain that the animation will be Knight Rider Kitt style: maybe throw in a gif for nostalgia
//  - it will run all the way left and then all the way right over and over again -->

### A Closer Look at the Code

<!-- // an overview of the code -->

We've introduced some new and important concepts in this experiment.

We've created and imported **modules**, files containing code that can be loaded and reused in other scripts without us having to re-type them again. We've also introduced **classes** which are blueprints for Python objects. Python objects are collections of data that are meant to help you wrap up low-level grunt-work code into simpler, more usable functions and variables.

Modules and classes are a crucial part of writing clean and maintainable software. It's best practice to write your code to make use of modules or classes and avoid retyping the same code over and over again so you can update or make fixes much more easily.

During the code, we used **bitshifting** as an optimization to avoid slow String operations.

Finally, we introduced **safely exiting from an infinite loop**, to ensure that the Omega's GPIOs are properly freed from the Python script once you want to end the program.

#### Creating and Importing Modules

<!-- // DONE: describe how the import process works, make sure to note how the directory structure has to fit -->

A **module** is a file containing Python definitions and statements. This can be used to split your project into multiple files for easier maintenance. The `registerClass.py` file is an example of a self-made module that we've imported. Some modules are built in to Python; some examples are `time` which you may have used before, and `signal` which is used in our main program.

Some modules are built into the Python system and can be imported by name no matter what directory your script is in, such as `time` or `sys`. However, if you create your own module file, you can import it by name only if it is in the **same directory** as the script that calls it. Otherwise you will need to use a slightly different command where you must provide the filepath to the module file.

In order to keep things simple, we will be creating module files in the same directories as the main scripts for all of these experiments.

#### Creating and Using Classes {#starter-kit-using-shift-register-creating-classes}

<!-- // DONE: mention how we've used the onionGpio class before, now we're going one step further and creating our own class -->

As a refresher, classes are a way to create a template for creating reusable objects in our code. So far, we've been using the `onionGpio` class that we at Onion made to make your development experience easier. This class includes clean, easy-to-use functions such as `setValue()` that hide away boring and time-consuming system calls from you, the up-and-coming programmer who wants to get to the fun stuff!

Here, we've gone one step further by creating our own class called `shiftRegister` that also uses the `onionGpio` class in order to create our shift register objects. This is because in this case, we're more interested in the **data** we send to the shift register than controlling the shift register's GPIOs!

If we wanted to connect another shift register to our circuit, we can control it as easily as the first by creating another `shiftRegister` object.

After creating an object, we get access to the functions defined by the object's class. We can call these functions through our instantiated object like in this example:

``` python
shiftRegister.outputBits(bytestring)
```

This function is defined in the `shiftRegister` class file:

``` python
def outputBits(self, inputString):
    bitList = list(inputString) # Splits the string into a list of individual characters ("11000000" -> ["1","1","0","0","0","0","0","0"])
    for x in bitList:
        x = int(x) # Transforms the character back into an int ("1" -> 1)
        self.inputBit(x)
    self.latch()
```

You'll also notice that we include `self` in our Python class functions. This is necessary so that we are always working with variables or functions pertaining to the current object. This is called **explicit self** in Python.

<!-- // explanation of Classes
//  - definition of Classes
//  - using classes
//  - each class becomes an object when you instantiate it
//    - can call functions from the object, etc
//    - if we had two shift registers, we could have two objects to run the two different ones
//  - talk about how class functions can use other class functions -->

#### Binary Numbers

Binary numbers are numbers whose digits can only be **0 or 1**. Similar to how the decimal or base 10 system where each digit is a power of ten, each digit (or **bit**) in binary is a power of 2. Take a look at some of the conversions from binary to decimal below:

| Binary | Decimal |
|---:|---------|
| 1      | 1       |
| 10     | 2       |
| 100    | 4       |
| 1000   | 8       |

When writing binary numbers in code, they're typically prefixed with a `0b`, like `0b11010`. When assigning integers such as 42 to variables, the computer actually stores them as binary numbers (`42` = `0b101010`); you can then work with them in either binary, decimal, or even a different base if you wish!

A **byte** is an 8-bit binary number, for example `0b11000000`. A **bytestring** is a string representation that we can perform string operations on, such as reading each bit one at a time.

#### Bitshifting

You'll notice we do some funky operations with the `value` variable like so:

``` python
value >>= 1 # Shifts all digits right by one (11000000 -> 01100000)
...
value <<= 1 # Shifts all digits left by one (01100000 -> 11000000)
```

Th `>>` operation by itself is known as the  **bitshift** operator.

Bitshifting is a pretty low level operation that moves the bits of a binary value left or right. In our script, our shift register command starts off as the number `0b11000000`. For example, to bitshift one digit to the right, we move both of the two `1`s right one place to get `0b00110000`. Bitshifting is a fast operation for computers to do, and is easier than trying to convert the number into a binary string and moving the characters around by hand.

The added `=` sign means the same thing as in the increment operator `+=`. It performs the bitshift operation on the variable and updates it without you having to explicitly reassign it.

On a side note, when we bitshift a number to the left or right, we're actually **multiplying or dividing it by 2** respectively! This is like multiplying or dividing by 10 in the decimal system where the digits shift left and right.

>While it's usually a good deal faster, bitshifting isn't always the most readable code - since the purpose of the shift is not often clear. Remember to comment your code so you and others can understand why it's there!

#### Exiting Infinite Loops

When using GPIOs, it's important that you exit your code properly to free the GPIOs back to the filesystem for use by other programs. This can be quite difficult when we create an infinite loop so we've included a solution to that.

When inspecting our main program we see a function defined as `signal_handler`. We also see an signal listener in the form of:

```
signal.signal(signal.SIGINT, signal_handler)
```

This listener is waiting for an interrupt from the user in order to run the signal handler code. When you enter `Ctrl-C` or `Cmd-C` you are sending a **keyboard interrupt** which is then handled by the interrupt **handler** function in order to exit the program in a safe way. This way your code will always finish the current left-right animation before exiting, thus making sure that your GPIOs are properly freed by the time the program exits.

<!-- // nowhere did we explain this part of the main program:
```
for x in range(0, 12):
  bytestring = "{0:08b}".format(value) # Transforms the value into a binary number (192 = 11000000)
  shiftRegister.outputBits(bytestring) # Sends the 8 bit value to be output by the shift register
  if x < 6:
    value >>= 1 #Shifts the value right by one (11000000 -> 01100000)
  else:
    value <<= 1 #Shifts the value left by one (01100000 -> 11000000)
```
// DONE: please add a section (AND COMMENTS IN THE CODE) describing what this will accomplish
Gabe: addressed, see above sections-->
