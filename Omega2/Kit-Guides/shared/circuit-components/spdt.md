### Switch - Single Pole, Double Throw {#circuit-components-spdt}

A single pole, double throw switch is a switch with two inputs that switch into one output.

![Circuit symbol of an SPDT switch](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/spdt-symbol.png)

The switch has three terminals, one for each of the inputs (labelled `L1`, `L2`) and one for the output (labelled `COM` here). The inputs will never be connected, and one input is always exclusively connected to the output. This kind of switch is useful for logic circuits, because one input can reference logical `HIGH` and the other logical `LOW` without the ambiguity of open circuit.

The 'single pole' in SPDT refers to the only output, while the 'double throw' refers to the two exclusive inputs.

![A SPDT sliding switch included in our kit](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/switches-slide.jpg)
