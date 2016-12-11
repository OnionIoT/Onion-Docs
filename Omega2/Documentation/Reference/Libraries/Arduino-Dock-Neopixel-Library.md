# Arduino Dock Neopixel Library

The Omega + Arduino Dock can be used to control Neopixels, with the Omega sending the commands and colour codes, and the Arduino Dock acting as a communication channel. 

![Omega+Arduino Dock w/ Neopixel Array](http://i.imgur.com/l5oVLdi.jpg)

The Onion Arduino Dock Neopixel C & C++ library, `libonionneopixel` provides functions to interact with the Neopixels. Also available is a module for use in Python called `neopixel` that is part of the `OmegaArduinoDock` package.


[[_TOC_]]



[//]: # (Programming Flow)

# Programming Flow

The first action that must be performed is always the initialization of the Arduino Dock for controlling Neopixels. This entails setting which Arduino Dock pin will be used as data output, setting the number of Neopixels, and running the initalization function.

Afterwards, the colours of the Neopixels can be changed at will. The colour changes will be queued up, and a function to show the queued up changes must be run for the changes to take effect on the actual Neopixels.



After each power-cycle, the chip that controls the Relay Expansion must be programmed with an initialization sequence. After the initialization, the relays can be turned on and off at will.



[//]: # (MAJOR HEADING)
[//]: # (The C & C++ Library)

# The C & C++ Library

The dynamic C & C++ library, `libonionneopixel` provides a C++ class and C functions that wrap around this class.


[//]: # (Installing the Library)

## Installing the Library

The library can be installed by running the following commands:
```
opkg update
opkg install libonionneopixel
```

Note that it will automatically be installed when the `neopixel-tool` utility is installed.


[//]: # (Return Values)

## Return Values

All functions follow the same pattern with return values:

If the function operation is successful, the return value will be `EXIT_SUCCESS` which is a macro defined as `0` in `cstdlib.h.`

If the function operation is not successful, the function will return `EXIT_FAILURE` which is defined as `1`. 

A few reasons why the function might not be successful:
* The specified device address cannot be found on the I2C bus (the Expansion is not plugged in)
* The system I2C interface is currently in use elsewhere

An error message will be printed that will give more information on the reason behind the failure.



[//]: # (SUBHEADING)
[//]: # (The C++ Library)

## The C++ Library

The C++ library is implemented around an `onionNeopixel` class. It provides public class functions to perform all of the actions specified in the [Programming Flow section](#Programming-Flow).


[//]: # (The C++ Library: Using the C++ Library)

### Using the C++ Library

**Header File**

To add the Onion Neopixel Library to your program, include the header file in your code:
``` c++
#include <neopixel.h>
```

**Library for Linker**

In your project's makefile, you will need to add the following dynamic libraries to the linker command:
``` c++
-lonionneopixel
```

The dynamic libraries are stored in `/usr/lib` on the Omega.



[//]: # (The C++ Library: Class Functions)

### Class Functions

The `onionNeopixel` class contains all of the routines required to control Neopixels using the Arduino Dock.


[//]: # (The C++ Library Class Functions: Constructor)

#### The Constructor

The constructor for the `onionNeopixel` class will initialize all class variables. It also has an optional argument that sets the I2C device address of the Arduino Dock. By default this address is 0x08 and if you have made no changes to the Onion Arduino Library, there is no need to include this argument.

**Examples**

To initialize an `onionNeopixel` object called `neopixelObj`:
``` c++
onionNeopixel*	neopixelObj	= new onionNeopixel();
```

To initialize an `onionNeopixel` object called `npixel` where the Arduino Dock's I2C address is 0x09:
``` c++
onionNeopixel*	npixel	= new onionNeopixel(0x09);
```


[//]: # (The C++ Library Class Functions: SetPin)

#### Set the Arduino Dock Pin

This class function sets the Arduino Dock pin that will act as the data port for the Neopixels:
``` c++
int SetPin (int input);
```

**Examples**

To set the pin to 6 for an `npixel` object:
``` c++
status = npixel->SetPin(6);	
```


[//]: # (The C++ Library Class Functions: SetLength)

#### Set the Number of Neopixels

This class function programs the total number of Neopixels that are connected to the Arduino Dock pin:
``` c++
int SetLength (int input);
```

**Examples**

For an `npixel` object, set that it controls 64 neopixels:
``` c++
status = npixel->SetLength(64);	
```



[//]: # (The C++ Library Class Functions: Init)

#### Initialize the Arduino Dock and Neopixels

This function will perform an initialization on the Arduino Dock and afterwards, the Neopixels will be ready to use:
``` c++
int Init ();
```

Note that the `SetPin` and `SetLength` functions **must** be called prior to the `Init` function is called.


**Examples**

For an `npixel` object, initialize the Arduino Dock for neopixels:
``` c++
status = npixel->Init();	
```


[//]: # (The C++ Library Class Functions: Init in one step)

#### Initialize the Arduino Dock and Neopixels in a Single Step

This function will perform the functions of `SetPin`, `SetLength`, and `Init` in a single function call:
``` c++
int Init (int pin, int length);
```

It is an overloaded function so it has the same name as the initialization function above. It provides a simplification


**Examples**

For an `npixel` object, initialize the Arduino Dock to use pin 5 and control 32 neopixels:
``` c++
status = npixel->Init(5, 32);	
```


[//]: # (The C++ Library Class Functions: Set Brightness)

#### Set the Maximum Pixel Brightness 

This class function will set the maximum brightness of a pixel by defining a maximum for the colour components:
``` c++
int SetBrightness (int input);
```

The brightness change will not take effect on the physical Neopixels until the [`ShowPixels` function](#the-c-c-library_the-c-library_class-functions_show-all-queued-colour-changes) function is called.


**Arguments**

The `input` argument sets the the maximum colour intensity for all colour components. The range is **0 to 255**.


**Examples**

For an `npixel` object, set the brightness to the maximum:
``` c++
status = npixel->SetBrightness(255);	
```

For an `npixel` object, set the brightness to half the maximum and have it take effect right away:
``` c++
status =  npixel->SetBrightness(127);
status |= npixel->ShowPixels();
```

For an `npixel` object, set the brightness to a quarter of the maximum:
``` c++
status = npixel->SetBrightness(63);
```


[//]: # (The C++ Library Class Functions: Set the Colour of a Pixel)

#### Set the Colour of a Pixel

This class function will queue up a change in the colour intensity of a single pixel:
``` c++
int SetPixel (int pixelId, int red, int green, int blue);
```

The pixels colours changes setup with this function will not be shown on the physical Neopixels until the [`ShowPixels` function](#the-c-c-library_the-c-library_class-functions_show-all-queued-colour-changes) function is called.


**Arguments**

The `pixelId` argument defines which pixel in the Neopixel array is to be controlled, with the first pixel in the strip being pixel 0. Note that this pixel id should be less than the total number of pixels.

The `red`, `green`, and `blue` arguments are the colour intensity values for the respective colour. Neopixels are 8-bits per colour component, so the values can range from **0 to 255**. Experiment with a [colour wheel](http://www.w3schools.com/tags/ref_colorpicker.asp) to find the primary colour intensities for your desired colours.


**Examples**

For an `npixel` object, set the first pixel to white:
``` c++
status = npixel->SetPixel(0, 0xff, 0xff, 0xff);	
```

For an `npixel` object, set the 18th pixel to purple:
``` c++
status = npixel->SetPixel(18, 0xcc, 0x00, 0x99);	
```

For an `npixel` object, set the 64th pixel to orange:
``` c++
status = npixel->SetPixel(63, 0xff, 0x8c, 0x1a);	
```



[//]: # (The C++ Library Class Functions: Set the Colour of Many Pixels)

#### Set the Colour of many Pixels

This class function will queue the change of the colour intensity for many pixels using a buffer of colour components:
``` c++
int SetBuffer (int *buf, int size);
```

The first pixel in the buffer will be displayed on pixel 0 of the physical Neopixels. The pixels colours setup with this function will not be shown on the physical Neopixels until the [`ShowPixels` function](#the-c-c-library_the-c-library_class-functions_show-all-queued-colour-changes) function is called.

**Arguments**

The `buf` argument is an array that should hold colour component triplets for however many pixels are desired:

| `buf` Element | Pixel | Colour Component |
|---------------|-------|------------------|
| `buf[0]`      | 0     | Red              |
| `buf[1]`      | 0     | Green            |
| `buf[2]`      | 0     | Blue             |
| `buf[3]`      | 1     | Red              |
| `buf[4]`      | 1     | Green            |
| `buf[5]`      | 1     | Blue             |
| ...           | ...   | ...              |
| `buf[n*3]`    | n     | Red              |
| `buf[n*3+1]`  | n     | Green            |
| `buf[n*3+2]`  | n     | Blue             |


The `size` argument represents the number of elements in the `buf` array, so it should be the number of pixels multiplied by three colour components.


**Examples**

For an `npixel` object, set 3 pixels to brown:
``` c++
int colours[9] = {0x99, 0x66, 0x00, 0x99, 0x66, 0x00, 0x99, 0x66, 0x00};
status = npixel->SetBuffer(colours, 9);	
```

For an `npixel` object, set 12 pixels to lime:
``` c++
int length 		= 12*3;
int *buffer 	= new int[length];

for (int i = 0; i < length; i += 3) {
	buffer[i]	= 0xcc;
	buffer[i+1]	= 0xff;
	buffer[i+2]	= 0x33;
}

status = npixel->SetBuffer(buffer, length);
```


[//]: # (The C++ Library Class Functions: Show Queued Colour Changes)

#### Show All Queued Colour Changes

This class function will send a command to the Arduino Dock to display all queued colour and/or brightness changes on the physical Neopixels:
``` c++
int ShowPixels ();
```

**Examples**

For an `npixel` object, show all queued colour changes:
``` c++
status = npixel->ShowPixels();	
```


[//]: # (The C++ Library: Example Code)

### Example Code

Example code that uses the `onionNeopixel` class can be found in the source code for [the `neopixel-tool` command line utility](../../Tutorials/Arduino-Dock/Controlling-Neopixels#omega-command-line-tool). Please take a look at the [neopixel-tool GitHub repo](https://github.com/OnionIoT/neopixel-tool). 

The files of interest are:
* [`include/main.h`](https://github.com/OnionIoT/neopixel-tool/blob/master/include/main.h)
* [`src/main.cpp`](https://github.com/OnionIoT/neopixel-tool/blob/master/src/main.cpp)




[//]: # (SUBHEADING)
[//]: # (The C Library)

## The C Library

The C library is a series of C functions that provide wrappers to the C++ `onionNeopixel` class. It provides the same functionality as the C++ class but in code that can be used in C.


[//]: # (The C Library: Using the C Library)

### Using the C Library

**Header File**

To add the Onion Neopixel Library to your program, include the header file in your code:
``` c
#include <neopixel_Cwrapper.h>
```

**Library for Linker**

In your project's makefile, you will need to add the following dynamic libraries to the linker command:
``` c
-lonionneopixel
```

The dynamic libraries are stored in `/usr/lib` on the Omega.



[//]: # (The C Library: Library Functions)

### Library Functions

The following functions implement all of the routines required to control Neopixels using the Arduino Dock.


[//]: # (The C Library Class Functions: Init)

#### Initialize the Arduino Dock and Neopixels

This function will perform the following:
* Set the Arduino Dock pin that will act as the data port for the Neopixels
* Set the total number of Neopixels
* Run the initalization sequence

``` c
int neopixelInit (int devAddr, int pin, int length);
```

**Arguments**

The `devAddr` argument provides the I2C device address of the Arduino Dock. By default this address is 0x08 and if you have made no changes to the Onion Arduino Library, the `NEOPIXEL_I2C_DEVICE_ADDR` macro can be used.

The `pin` argument defines the Arduino Dock pin. And the `length` argument defines the number of Neopixels.

**Examples**

Initialize the Arduino Dock to use pin 9 and control 12 neopixels:
``` c
status = neopixelInit (NEOPIXEL_I2C_DEVICE_ADDR, 9, 12);
```

Initialize the Arduino Dock to use pin 10 and control 128 neopixels:
``` c
status = neopixelInit (NEOPIXEL_I2C_DEVICE_ADDR, 10, 128);
```


[//]: # (The C Library Class Functions: Set Brightness)

#### Set the Maximum Pixel Brightness 

This function will set the maximum brightness of a pixel by defining a maximum for the colour components:
``` c
int neopixelSetBrightness (int brightness);
```

The brightness change will not take effect on the physical Neopixels until the [`neopixelShowPixels` function](#the-c-c-library_the-c-library_library-functions_show-all-queued-colour-changes) function is called.


**Arguments**

The `brightness` argument sets the the maximum colour intensity for all colour components. The range is **0 to 255**.


**Examples**

Set the brightness to the maximum:
``` c
status = neopixelSetBrightness(255);	
```

Set the brightness to half the maximum and have it take effect right away:
``` c
status =  neopixelSetBrightness(127);
status |= neopixelShowPixels();
```

Set the brightness to a quarter of the maximum:
``` c
status = neopixelSetBrightness(63);
```


[//]: # (The C Library Class Functions: Set the Colour of a Pixel)

#### Set the Colour of a Pixel

This function will queue up a change in the colour intensity of a single pixel:
``` c
int neopixelSetPixel (int pixelId, int red, int green, int blue);
```

The changes to the pixel will not show up on the physical Neopixels until the [`neopixelShowPixels` function](#the-c-c-library_the-c-library_library-functions_show-all-queued-colour-changes) function is called.


**Arguments**

The `pixelId` argument defines which pixel in the Neopixel array is to be controlled, with the first pixel in the strip being pixel 0. Note that this pixel id should be less than the total number of pixels.

The `red`, `green`, and `blue` arguments are the colour intensity values for the respective colour. Neopixels are 8-bits per colour component, so the values can range from **0 to 255**. Experiment with a [colour wheel](http://www.w3schools.com/tags/ref_colorpicker.asp) to find the primary colour intensities for your desired colours.


**Examples**

Set the first pixel to white:
``` c
status = neopixelSetPixel(0, 0xff, 0xff, 0xff);	
```

Set the 18th pixel to purple:
``` c
status = neopixelSetPixel(18, 0xcc, 0x00, 0x99);	
```

Set the 64th pixel to orange:
``` c
status = neopixelSetPixel(63, 0xff, 0x8c, 0x1a);	
```



[//]: # (The C Library Class Functions: Set the Colour of Many Pixels)

#### Set the Colour of many Pixels

This function will queue the change of the colour intensity for many pixels using a buffer of colour components:
``` c
int neopixelSetBuffer (int *buf, int size);
```

The first pixel in the buffer will be displayed on pixel 0 of the physical Neopixels.
The changes to the pixels will not show up on the physical Neopixels until the [`neopixelShowPixels` function](#the-c-c-library_the-c-library_library-functions_show-all-queued-colour-changes) function is called.


**Arguments**

The `buf` argument is an array that should hold colour component triplets for however many pixels are desired:

| `buf` Element | Pixel | Colour Component |
|---------------|-------|------------------|
| `buf[0]`      | 0     | Red              |
| `buf[1]`      | 0     | Green            |
| `buf[2]`      | 0     | Blue             |
| `buf[3]`      | 1     | Red              |
| `buf[4]`      | 1     | Green            |
| `buf[5]`      | 1     | Blue             |
| ...           | ...   | ...              |
| `buf[n*3]`    | n     | Red              |
| `buf[n*3+1]`  | n     | Green            |
| `buf[n*3+2]`  | n     | Blue             |


The `size` argument represents the number of elements in the `buf` array, so it should be the number of pixels multiplied by three colour components.


**Examples**

Set 3 pixels to brown:
``` c
int colours[9] = {0x99, 0x66, 0x00, 0x99, 0x66, 0x00, 0x99, 0x66, 0x00};
status = neopixelSetBuffer(colours, 9);	
```

Set 12 pixels to lime:
``` c
int length 		= 12*3;
int *buffer 	= new int[length];

for (int i = 0; i < length; i += 3) {
	buffer[i]	= 0xcc;
	buffer[i+1]	= 0xff;
	buffer[i+2]	= 0x33;
}

status = neopixelSetBuffer(buffer, length);
```


[//]: # (The C Library Class Functions: Show Queued Colour Changes)

#### Show All Queued Colour Changes

This function will send a command to the Arduino Dock to display all queued colour changes on the physical Neopixels:
``` c
int neopixelShowPixels ();
```

**Examples**

Show all queued colour changes:
``` c
status = neopixelShowPixels();	
```


[//]: # (The C Library Class Functions: Clean-Up)

#### Clean-Up

Since the C functions are a wrapper around the C++ class, at the end of your program, it's required to run a function to clean-up any dynamically allocated memory.
``` c
void neopixelFree ();
```

**Examples**

Perform the clean-up:
``` c
neopixelFree();	
```





[//]: # (MAJOR HEADING)
[//]: # (The Python Module)

# The Python Module

The Python module `neopixel` in the `OmegaArduinoDock` package provides a class, `OnionNeopixel` to control Neopixels. It's essentially a wrapper of the C++ library so the functions are very similar.


[//]: # (Installing the Module)

## Installing the Module

The library can be installed by running the following commands:
```
opkg update
opkg install pyNeopixel python-light
```


[//]: # (Return Values)

## Return Values

All functions follow the same pattern with return values:

If the function operation is successful, the return value will be `0`.

If the function operation is not successful, the function will return `1`. 


[//]: # (Using the Module)

## Using the Module

To add the Onion Neopixel Module to your Python program, include the following in your code:
``` python
from OmegaArduinoDock import neopixel
```


[//]: # (The Python Class)

## The Python Class

The Python class, `OnionNeopixel` is very similar to the C++ class; it provides public class functions to perform all of the actions specified in the [Programming Flow section](#Programming-Flow).


[//]: # (The Python Class Functions: Constructor)

### The Constructor

The constructor for the `OnionNeopixel` class will perform the following: 
* initialize all class variables
* Set the Arduino Dock pin that will act as the data port for the Neopixels
* Set the total number of Neopixels
* Run the initalization sequence

It also has an optional argument that sets the I2C device address of the Arduino Dock. By default this address is 0x08 and if you have made no changes to the Onion Arduino Library, there is no need to include this argument.

**Examples**

To initialize an `OnionNeopixel` object called `npixel`:
``` python 
npixel 	= neopixel.OnionNeopixel(6, 64)
```

To initialize an `onionNeopixel` object called `npixel` where the Arduino Dock's I2C address is 0x09:
``` python
npixel 	= neopixel.OnionNeopixel(6, 64, 0x09)
```


[//]: # (The Python Class Functions: Set Brightness)

### Set the Maximum Pixel Brightness 

This function will set the maximum brightness of a pixel by defining a maximum for the colour components:
``` python
setBrightness (int brightness);
```

The brightness change will not take effect on the physical Neopixels until the [`showPixels()` function](#the-python-module_the-python-class_show-all-queued-colour-changes) function is called.


**Arguments**

The `brightness` argument sets the the maximum colour intensity for all colour components. The range is **0 to 255**.


**Examples**

For an `npixel` object, set the brightness to the maximum:
``` python 
status = npixel.setBrightness(255);	
```

For an `npixel` object, set the brightness to half the maximum and have it take effect right away:
``` python 
status = npixel.setBrightness(127); 
status = npixel.showPixels();
```

For an `npixel` object, set the brightness to a quarter of the maximum:
``` python 
status = npixel.setBrightness(63);
```


[//]: # (The Python Class Functions: Set the Colour of a Pixel)

### Set the Colour of a Pixel

This function will queue up a change in the colour intensity of a single pixel:
``` python
setPixel (pixelId, red, green, blue)
```

Note the changes will not take effect on the physical Neopixels until the [`showPixels()` function](#the-python-module_the-python-class_show-all-queued-colour-changes) is called.

**Arguments**

The `pixelId` argument defines which pixel in the Neopixel array is to be controlled, with the first pixel in the strip being pixel 0. Note that this pixel id should be less than the total number of pixels.

The `red`, `green`, and `blue` arguments are the colour intensity values for the respective colour. Neopixels are 8-bits per colour component, so the values can range from **0 to 255**. Experiment with a [colour wheel](http://www.w3schools.com/tags/ref_colorpicker.asp) to find the primary colour intensities for your desired colours.


**Examples**

For an `npixel` object, set the first pixel to white:
``` python 
status = npixel.setPixel(0, 0xff, 0xff, 0xff);	
```

For an `npixel` object, set the 18th pixel to purple:
``` python 
status = npixel.setPixel(18, 0xcc, 0x00, 0x99);	
```

For an `npixel` object, set the 64th pixel to orange:
``` python
status = npixel.setPixel(63, 0xff, 0x8c, 0x1a);	
```



[//]: # (The Python Class Functions: Set the Colour of Many Pixels)

### Set the Colour of many Pixels

This function will queue the change of the colour intensity for many pixels using a python list of colour components:
``` c
setBuffer (pyBuf)
```

The first pixel in the buffer will be displayed on pixel 0 of the physical Neopixels.
Note the changes will not take effect on the physical Neopixels until the [`showPixels()` function](#the-python-module_the-python-class_show-all-queued-colour-changes) is called.

**Arguments**

The `pyBuf` argument is a Python list that should hold colour component triplets for however many pixels are desired:

| `buf` Element | Pixel | Colour Component |
|---------------|-------|------------------|
| `buf[0]`      | 0     | Red              |
| `buf[1]`      | 0     | Green            |
| `buf[2]`      | 0     | Blue             |
| `buf[3]`      | 1     | Red              |
| `buf[4]`      | 1     | Green            |
| `buf[5]`      | 1     | Blue             |
| ...           | ...   | ...              |
| `buf[n*3]`    | n     | Red              |
| `buf[n*3+1]`  | n     | Green            |
| `buf[n*3+2]`  | n     | Blue             |



**Examples**

Set 3 pixels to brown for an `npixel` object:
``` c
buf = [0x99, 0x66, 0x00, 0x99, 0x66, 0x00, 0x99, 0x66, 0x00]
status = npixel.setBuffer(buf)	
```



[//]: # (The Python Class Functions: Show Queued Colour Changes)

### Show All Queued Colour Changes

This function will send a command to the Arduino Dock to display all queued colour changes on the physical Neopixels:
``` python 
showPixels()
```

**Examples**

Show all queued colour changes for an `npixel` object:
``` python
status = npixel.showPixels();	
```


[//]: # (The Python Module: Example Code)

## Example Code

Example code that uses the `OnionNeopixel` Python class can be found for [download here.](https://downloads.onion.io/arduino-dock/slowColourChange.py)

This is a Python program that shows a single colour on an entire Neopixel strip or array. It slowly loops between seven different colours, with 25 intermediate steps between the colour changes, creating a smooth transition effect.

![slowColourChange Gif](http://i.imgur.com/QFxAq9M.gif)



