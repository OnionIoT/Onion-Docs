## Circuit Diagram Introduction

<!--
// intro:
//	* most if not all of our experiments will use circuit diagrams to describe the circuits we will be building
// 	* use this as a reference when reading the circuit diagrams

// circuit diagrams can also be referred to as schematics or circuit schematics
-->

Nearly all of our experiments will use a circuit diagram to precisely express the circuit that will be built. Also referred to as schematics, or circuit schematics, we use them as an additional way to ensure we're on the right track. Beyond that, learning how to read them is a very useful skill for all kinds of electrical projects down the line!

This article is intended to be used as a reference when reading circuit diagrams, keep it bookmarked somewhere handy if you think you'll check back!

### General Structure
<!--
// show an example circuit diagram, briefly cover the following:
//	* the lines mean connections
//	* the various symbols mean different components
//		* the components are usually labelled with values
-->

Generally, circuit diagrams look a little like this:

![Sample circuit diagram](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/sample-circuit-diagram.png)

This is a circuit from one of our expriments, and it follows the gist of a circuit diagram: lines connecting symbols.

In a circuit diagram, any straight lines mean an electrical connection between things - no matter through a jumper, a wire, or a big metal plate, as long as electricity can flow. The various symbols represent the components that are being connected by the wires. What each symbol mean we'll cover in detail just below.

<!--

////
// Listing of components used in this Kit,
// should look something like this: https://learn.sparkfun.com/tutorials/how-to-read-a-schematic/schematic-symbols-part-1
 
// each component should have a section that shows:
//	* the name of the component
//	* the symbol
//	* a brief description that includes:
//		* how many terminals it has
//		* if there are any values associated with the diagram, explain what it means
//		* a photo of the real component
-->

```{r child = '../circuit-components/led.md'}
```

```{r child = '../circuit-components/resistor.md'}
```

```{r child = '../circuit-components/capacitor.md'}
```

```{r child = '../circuit-components/power-supply.md'}
```

```{r child = '../circuit-components/ground.md'}
```

```{r child = '../circuit-components/spst.md'}
```

```{r child = '../circuit-components/spdt.md'}
```

```{r child = '../circuit-components/integrated-circuit.md'}
```

```{r child = '../circuit-components/omega-pin.md'}
```

```{r child = '../circuit-components/device-pin.md'}
```


<!-- // NOTE FROM LAZAR: only include symbols for components included in this kit, can use separate files for each component,
// see `Omega2/Kit-Guides/shared/circuit-components/resistor.md` for an example
// lets put all of the components in that directory, `Omega2/Kit-Guides/shared/circuit-components/`
-->
