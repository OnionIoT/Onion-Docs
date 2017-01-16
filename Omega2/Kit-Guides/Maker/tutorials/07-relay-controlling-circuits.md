---
title: Controlling Other Circuits
layout: guide.hbs
columns: two
devices: [ Omega , Omega2 ]
order: 7
---

# Controlling Other Circuits with the Relay Expansion

// this tutorial will go over how an omega with a relay expansion can be used to control other, independent circuits

## Circuit Isolation

// explain that the omega's relays are completely isolated from the circuit that is connected to the terminals, it merely acts as a switch

// this is useful since it allows the Omega to control other, larger, more powerful circuits
//  expand along those lines, maybe throw in the max specs of the relays, hint that you can control house-hold appliances




## Building the Circuit

// 5V buzzer circuit connected to relay
// push button as gpio to toggle the relay

### Hooking up the Components

// detailed explanation of connecting wires to the screw terminals

// wiring up the buzzer so that the connection is interrupted by the relay



## Writing the Code

// write a script so that when the button is pushed: read the relay state, and flip it


### What to Expect

// pressing the button will make the buzzer start buzzing, pressing it again will disable the sound


### A Closer Look at the Code

// introduced a good practise: reading then writing

#### Reading then Writing

// often times we will want to switch the state a device is in, reading and then writing (read-modify-write) is the correct way of going about this
