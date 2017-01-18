---
title: Controlling Other Circuits
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 7
---

## Isolated Control with the Relay Expansion {#isolated-control-with-the-relay-expansion}

// this tutorial will go over how an omega with a relay expansion can be used to control other, independent circuits
In this tutorial, we'll use a switch with the Omega Relay expansion to turn a buzzer on or off. Along the way, we'll be looking into why relays are useful, and go into more detail regarding pitfalls when interacting with hardware.


### Circuit Isolation

// explain that the omega's relays are completely isolated from the circuit that is connected to the terminals, it merely acts as a switch

// this is useful since it allows the Omega to control other, larger, more powerful circuits
//  expand along those lines, maybe throw in the max specs of the relays, hint that you can control house-hold appliances

Omega boards and components are not designed to handle much more than 5V circuit and 12V supply. Attempting to directly control 120V appliances like lights, heaters, garage doors will almost certainly fry your Omega. So how can you turn on your lights?

Enter the relay switch a relay is essentially a mechanical switch that is triggered electronically. This physically separates the circuit that triggers the switch and the circuit that the switch actually switches. The relay expansion is designed to isolate the Omega and the dock from high power circuits while allowing it to be controlled by the Omega. 


### Building the Circuit

// 5V buzzer circuit connected to relay
// push button as gpio to toggle the relay
Our goal here is to connect a buzzer to the relay expansion, and then connect a switch to the Omega's expansion headers. 

#### What You'll Need

* 1x Relay Expansion
* 1x Buzzer
* 1x SPDT (or three-way) switch
* 1x Breadboard
* 1x 


#### Hooking up the Components

// detailed explanation of connecting wires to the screw terminals

// wiring up the buzzer so that the connection is interrupted by the relay



#### Writing the Code

// write a script so that when the button is pushed: read the relay state, and flip it


#### What to Expect

// pressing the button will make the buzzer start buzzing, pressing it again will disable the sound


### A Closer Look at the Code

// introduced a good practise: reading then writing

#### Reading then Writing

// often times we will want to switch the state a device is in, reading and then writing (read-modify-write) is the correct way of going about this
