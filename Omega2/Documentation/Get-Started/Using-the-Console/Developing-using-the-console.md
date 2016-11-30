---
title: Developing using the Console
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 5
---


# Developing using the Console

// this article will show how you can use the console to develop code for the Omega using the Omega (pls reword so this makes sense)
// as an example project, we're going to write a script that will blink the Omega's LED in morse code based on user input

// section on using the editor to create a bash script
//  - installing the editor app
//  - small background on bash scripting
//  - walkthrough on navigating the file system and creating a new script
//    - make sure to mention that the best place for project files is in /root (since it won't be overwritten during firmware updates)
// - explanation of a script that controls the Omega's LED
//    - setting the led trigger to morse code (`echo morse > /sys/class/leds/onion:amber:system/trigger`)
//    - getting input from command line argument for the text to be converted to morse code
// note that there's an article about this already, can borrow heavily

// section on using the terminal app
//  - installing the terminal app
//  - logging in to the terminal
//  - navigating through the filesystem
//    - cd and ls commands, introduce ls -l
//    - have links to getting started with linux - check existing linux basics articles for these links
//  - using the echo command to read the available triggers in `/sys/class/leds/onion:amber:system/trigger`
//  - running the script we wrote using the editor app
