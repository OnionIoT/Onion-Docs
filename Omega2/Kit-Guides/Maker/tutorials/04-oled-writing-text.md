---
title: Writing Text to the OLED Display
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 4
---
// TODO: fix capitalization and emphasis
## Writing Text to the OLED Display {#writing-text-to-oled-display}

In this tutorial, we'll be figuring out how to start up the OLED Expansion's screen and writing some text to it using Onion's python library.


### The OLED Display
// TODO: IMAGE upload the imgur pngs to github!
The oled display has a resolution of 128x64 pixels. It is addressable by 128 vertical columns and 8 horizontal pages.
![display](http://i.imgur.com/4JsaahS.png)

Each page consists of 8 horizontal pixel rows. When a byte is written to the display, the Least Significant Byte (LSB) corresponds to the top-most pixel of the page in the current column. The Most Significant Byte (MSB) corresponds to the bottom-most pixel of the page in the current column.

![display](http://i.imgur.com/8DIiN2n.png)

The display keeps a cursor pointer in memory that indicates the current page and column being addressed. The cursor will automatically be incremented after each byte is written, the cursor can also be moved by the user through functions discussed later. When writing text to the display, each character is 6 columns wide and 1 page long. This means that 8 lines of text each 21 characters long, can be written to the oled display.

### Building the Circuit

This tutorial does not require you to wire anything in as the OLED Expansion is a complete circuit. Plug it into your expansion dock, and you're good to go!


#### What You'll Need

* 1x OLED Expansion


#### Writing the Code

Prior to running the code you will need to have python and the oledExp libraries installed. In case you don't have them, you can get them by running the folllowing commands:

```
opkg update
opkg install python-light
opkg install pyOledExp
```

```
from OmegaExpansion import oledExp
import time
import datetime
import math
from random import randint

# -*- coding: utf-8 -*-


quoteArray = ['Banging your head against a wall burns 150 calories an hour.',
'In the UK, it is illegal to eat mince pies on Christmas Day!',
'When hippos are upset, their sweat turns red.',
'Cherophobia is the fear of fun.',
'If you lift a kangaroos tail off the ground it cannot hop.']

def main():
	dateTimeObj = datetime.datetime.now()
	hour = dateTimeObj.hour
	minute = str(dateTimeObj.minute)
	if(hour/12 == 0):
		day = "AM"
		hour = str(hour % 12)
	else:
		day = "PM"
		hour = str(hour % 12)
	dateTimeStr = hour+":"+minute+" "+day
	if(dateTimeObj.hour < 12):
		greeting = "Good Morning"
	elif(17 > dateTimeObj.hour >= 12):
		greeting = "Good Afternoon"
	else:
		greeting = "Good Evening"
	# Initialize the display
	oledExp.driverInit()
	oledExp.setTextColumns()
	oledExp.setCursor(0,13)
	oledExp.write(dateTimeStr)
	oledExp.setCursor(2,0)
	oledExp.write(greeting)
	oledExp.setCursor(4,0)
	oledExp.write(quoteArray[randint(0,(len(quoteArray)-1))])

if __name__ == '__main__':
	main()

```

#### What to Expect

// TODO: IMAGE add gif of the results

After running the python code, you should see the current current time on the right side of the top row, a greeting on the third row and a random fact on the fifth row.

### A Closer Look at the Code

To get the current time, we use the datetime library that is provided standard with python. We create a datetime object storing the current date and time using the datetime.datetime.now() constructor. We then access the object's hour and min attributes to the retrieve the time values of interest. The we use some logic and mathematical conversion to decide if it is "AM" or "PM" and which greeting to display.

For the fun of it, we decided to display a random quote at the end

#### Generating Random Numbers

To generate a random number, we use the randInt class from the random library. We pass the range of random numbers to choose from, for our purposes the range corresonds to the length of the array. We then use this random integer to decide which quote will be written to the display.

It should be noted that we are using a pseudo-random generator which uses the Mersenne Twister and is completely deterministic. Hence, this method would be unsuitable in an important application where truly random numbers are required, such as cryptography.
