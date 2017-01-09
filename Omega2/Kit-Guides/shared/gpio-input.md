### GPIOs as Inputs

Now let's talk about the I in GPIO: using GPIOs in the input direction. This will allow you to read the logical level of circuits that are connected to the Omega{{#if Omega2}}2{{/if}}.

Meaning:

- If a signal is connected to an input GPIO and its voltage is 0V, the Omega{{#if Omega2}}2{{/if}} will read a logic low
- If a signal with a voltage of around 3.3V is connected to an input GPIO, the Omega{{#if Omega2}}2{{/if}} will read a logic high

// TO DO: IMAGE: add illustrations of: 1) gpio connected to ground, reading logical low, 2) gpio connected to Vcc, reading logical high

Using GPIOs in the input direction, allows us to sample the state of any circuit connected to the Omega{{#if Omega2}}2{{/if}}. As you'll see, this is going to be very useful.


