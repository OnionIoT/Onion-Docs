---
title: OLED Expansion
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 2
---

## OLED Expansion

// intro to the oled expansion - power efficient, tiny screen, mention the resolution and that it's monochrome
// can write text, draw images, adjust settings, do some little animations (scrolling)

// mention this expansion is controlled with i2c

### The Hardware

// Overview of the hardware:
//  - the screen


#### Connecting to a Dock

// plugged into the expansion Header
// have photos of it plugged into the Exp dock, power dock, and arduino dock 2

// mention that it's headers are blind - can't stack other expansions on top of it, but you wouldn't want to anyways since it would cover your screen?

#### At a Glance

// illustration

#### The Screen

// talk about how it's an OLED screen, mention the size and resolution, and mention resolution in terms of text characters

#### Understanding the Display

// see the following section: https://wiki.onion.io/Documentation/Libraries/OLED-Expansion-C-Library#programming-flow_understanding-the-display

// include it and expand on it/make it sound nice


### Using the OLED Expansion

// give an example of when this would be useful: displaying some data using your omega

// point them to the article on using the oled expansion
// this article can be heavily based on the existing doc: https://wiki.onion.io/Tutorials/Expansions/Using-the-OLED-Expansion
// includes:
//  - command line Usage
//    - initialization
//    - writing text
//    - displaying images
//    - changing settings
//  - link to controlling the screen from  C/C++ and python
