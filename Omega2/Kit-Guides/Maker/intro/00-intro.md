Welcome to the Guide for the Onion Omega2 Maker Kit!

![Maker Kit](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/Maker/img/maker-kit-icon.png)

### What We're Going to Learn

<!-- DONE: // a listing of what this kit will teach the reader
//	* How to put together circuits on a breadboard (essential skill for electronics prototyping)
//	* Get comfortable reading circuit diagrams
//	* Using Python to control external circuits with the Omega
//		* From the ground-up programming
//		* Using existing Python modules
//		* Object Oriented programming
//			* Using classes
//			* Writing our own classes
//	* -->

We're going to learn about the following:

* How to put together circuits on a breadboard  
    * This is an essential skill for electronics prototyping!
* Get comfortable reading circuit diagrams
* Using the Omega's command line interface
* Using the Omega PWM, Relay, and OLED Expansions
* Writing Python scripts on the command line
* Using Python to control external circuits with the Omega
	* Programming from the ground-up
	* Learning If statements, For loops, While Loops
	* Writing our own functions
	* Programming existing Python modules
	* Controlling Omega Expansions using Python
	* Object Oriented programming
		* Using classes
		* Writing our own classes

### What's Included

<!-- DONE: // overview of what the Kit contains
// * include the image that was printed with the kits (ask Zheng for this) -->

Your Maker Kit contains the following items; we've labelled them here for your convenience.

![Parts list](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/Maker/img/maker-kit-parts-list.png)

### How to Use This Guide

<!-- // * setup your Omega (link to #first-time-setup)
// * install some of the software packages we'll need for our experiments (link to our software installation article)
// * we recommend working your way linearly through the experiments as they usually build on what we've just learned -->
Before getting started on the experiments, set up your Omega by following the [First Time Setup Guide](#first-time-setup).

Then you can learn more on:

1. [Connecting to the Omega's Command Line](#connecting-to-the-omega-terminal)
1. [An introduction to using the command line](#the-command-line)
1. [Installing the software we need for the experiments](#maker-kit-intro-installing-software)

Once you've done those, we recommend working your way through the experiments in order as they usually build on what we've learned in each one.

### What Exactly Will I Learn?


Here's a list of all of the experiments we're going to build with your Kit:

```{r child='../../Starter/intro/experiment-listing.md'}
```

**COMING SOON!** 

And a list of tutorials on using the PWM, OLED, and Relay Expansions:

1. Dimming LEDs
    * Learn about Pulse Width Modulation and controlling LEDs
1. Controlling Servos
	* Use the PWM Expansion to control Servos and pick up some Python skills along the way
1. Run a DC Motor with an H-Bridge
	* We'll get really creative and use the PWM Expansion to control an H-Bridge chip which will in turn drive a DC motor
1. Writing text to the screen
    * We'll use Python to programmatically write text to the screen
1. Changing the screen's settings
	* Learn how we can use user input to change display settings
1. Draw lines!
	* Prompt the user for input and use it to draw lines on the screen
1. Controlling isolated circuits
    * Learn how to control circuits electrically isolated from the Omega's circuits


<!-- TODO: remove the above list when the articles are done -->

<!-- TODO: put this back in when articles are done!

```{r child='./pwm-tutorial-listing.md'}
```
```{r child='./oled-tutorial-listing.md'}
```
```{r child='./relay-tutorial-listing.md'}
``` -->
