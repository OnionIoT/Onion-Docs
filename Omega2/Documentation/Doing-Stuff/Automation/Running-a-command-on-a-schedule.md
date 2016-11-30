---
title: Running a Command on Boot
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 1
---

# Running a Command on Boot

// explain this article will show how to run a command on Boot

// give an example for when this would be useful: for example, writing something to the OLED expansion as soon as the Omega boots

## Implementation

// explain that it's all based on the `/etc/rc.local` file
// run through a non-trivial example with the OLED

### Text Output
// TODO: change the header title
// note that text output from the commands will not be saved anywhere by default
// introduce the concept of piping to a file

## Troubleshooting

// note the things that may stop the script from executing, if any
// steps on how to debug their issue: try running the commands one-by-one, try just manually running the `/etc/rc.local` file
