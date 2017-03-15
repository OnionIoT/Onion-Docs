## Controlling Servos {#arduino-kit-using-a-servo}

<!-- // intro to using pwm to control servos, this experiment will involve controlling servos using physical buttons -->

In this tutorial, we will use two push buttons to control two servos: a sub-micro sized servo and a standard sized servo. In addition, we will learn about object oriented programming by creating our own class for servo motors. Nearly all servo motors accept PWM as input, so we'll be going a bit deeper down that rabbit hole here.

<!-- pwm -->
```{r child = '../../shared/pwm.md'}
```

```{r child = '../../shared/pwm-details.md'}
```

<!-- servo -->
```{r child = '../../shared/servos.md'}
```

### Building the Circuit

For the circuit, we will need a small (sub-micro size) servo motor (MicroServo DXW90) and a standard size servo motor (Futaba S3003). In addition, we will need two push buttons, each with their own debounce circuits setup on a breadboard. When one button is pressed, both servos will turn to one direction; when the other button is pressed, they both turn to the other direction.

#### What You'll Need

Prepare the following components from your kit:

* Omega plugged into Arduino Dock
* USB Micro-B cable for power
* Breadboard
* Jumper wires
* Resistors
    * 2x 5.1kΩ
    * 2x 51kΩ
* 2x 100nF Capacitor
* 2x Tactile button
* 1x Servo Motor (Sub-micro size)
* 1x Servo Motor (Standard size)

#### Hooking Up the Components

<!-- // DONE: add an intro (d)-->
<!-- // TODO: IMAGE add a circuit diagram of the circuit we will be building -->

Now that you got everything, let's build!

Let's first set up the two push buttons with their seperate debounce circuits same as previous tutorials:
1. Set up two push buttons, each with their own debounce circuit similar to [tutorial 4](#arduino-kit-reading-a-push-button), don't connect to Arduino Dock yet.
1. Instead of connecting 51kΩ resistor to an empty row, we'll connect them to the `Vcc` rail.

Now that the buttons are set up, we'll connect the two servo motors:
1. The small servo has 3 wires: connect the brown wire to the `GND` rail, the red wire to the `Vcc` rail. We'll connect the orange (signal) wire in a bit.
	* Repeat for the standard sized servo.

Now that our components are set up, we'll connect them to the Arduino Dock:
1. Connect the negative power rail to ground (GND).
1. Connect the point in the first debounce circuit between the 5.1kΩ resistor and the capacitor to pin `2` of the Arduino Dock.
	* Repeat for the second debounce circuit, but plug the jumper into pin `3` instead
1. Connect the orange wire of small servo to pin `9` on the Arduino Dock, and the signal of the standard servo to pin `10`.
1. Connect the positive power rail to 5V. Don't worry if the servo rotates a bit when you power it on - this is expected.

<!-- // TODO: IMAGE add a photo of the completed circuit and a blurb about 'this is more or less how your circuit should look' -->

### Writing the Code

<!-- // DONE: intro to the code, in broad strokes talk about what we hope to accomplish -->

Now that the circuit is wired, it's time to write the code that makes it go!

In order to drive the servo, we'll create a servo class conforming to the limits of our motors in the sketch by leveraging the functions provided by the `Servo.h` Arduino Library. This allows us to reuse the code for the future, in addition to making our `setup()` and `loop()` functions much more readable.

To get your servos turning, copy the code below into `SKA08-usingServo.ino` and flash it to your Arduino Dock.

``` c++
// import the Arduino Servo library and define it

#include <Servo.h>

int incrementButton = 2;
int decrementButton = 3;
int currentAngle = 90;

// class to control servo motors
class ServoMotor
{
	private:               // variables or functions that can only be used within the ServoMotor class
	Servo servo;           // Servo object from the Arduino Servo library
	float rate;            // rate of pulse width change per degree
	float minPW, maxPW;    // min and max pulse width in microseconds (uS)
	int minAngle = 0;
	int maxAngle = 180;
	int pin;

	public:     //  variables or functions which can be called outside in the main program

	// ServoMotor() - constructor for a class with the same name
    // - will be automatically called when a class object is declared
	// - to use, pass in the pin number, max and min pulse width for the motor
    // - the class has functions to use given input to rotate the motor by
    //   arbitrary degrees
	ServoMotor(int pinNumber, float minPWus, float maxPWus){

		// pass in the pin number, max and min pulse width to private variables
		minPW = minPWus;
		maxPW = maxPWus;
		pin = pinNumber;

		// calculate the pulse width change for each degree
		rate = (maxPWus - minPWus)/(maxAngle - minAngle);
	}

	// function where you pass in an angle and it sets the servo motor to that angle
	void setAngle(float angle){

		// if the angle is greater than max angle or less than min angle, print the correct error message and exit the function
		if (angle > maxAngle){
			Serial.println("Servo angle over maximum. Please press decrease button");
			return;
		}
		else{
			Serial.println("Servo angle lower than minimum. Please press increase button");
			return;
		}

		// convert the angle to pulse width in microseconds(uS) using the rate previously calculated in the constructor
		float PWus = minPW + rate * angle;

		// TODO: LAZAR: look into this, can potentially move this to the constructor
		// initialize the servo pin using the Arduino Servo library
		servo.attach(pin);

		// set the servo angle by sending the calculated pulse width to the servo motor using the Arduino Servo library
		servo.writeMicroseconds(PWus);
	}
};

// instantiate two servo objects, one for each motor attached
ServoMotor smallServo (9, 500, 2000);     // initialize DXW90 small servo (500us to 2000us) at pin 9
ServoMotor standardServo (10, 0, 2500);     // initialize S3003 standard servo (0us to 2500us) at pin 10

void setup() {    // codes to be run once
	Serial.begin(9600);  // initializing serial communication with the Omega

	// initialize the pins connected to the increment and decrement buttons
	pinMode(incrementButton, INPUT);
	pinMode(decrementButton, INPUT);

	// set the initial angle of the two servos to 90 degrees
	smallServo.setAngle(currentAngle);
	standardServo.setAngle(currentAngle);
}

void loop() {   // code to be run continuously
    // read the state of the two push buttons (1 - not pressed, 0 - pressed) at the pins defined at the start of code
    int increment = digitalRead(incrementButton);
    int decrement = digitalRead(decrementButton);

    // if the increment button is pressed, increase the current angle by 5 degree and set both servos at the new angle
    if (increment == 0){
        currentAngle=currentAngle+5;
        Serial.print("Current angle: "); Serial.println (currentAngle);			//print the current angle
        smallServo.setAngle(currentAngle);
        standardServo.setAngle(currentAngle);
    }

     // if the decrement button is pressed, decrease the current angle by 5 degree and set both servos at the new angle
    if (decrement == 0){
        currentAngle=currentAngle-5;
        Serial.print("Current angle: "); Serial.println (currentAngle);			//print the current angle
        smallServo.setAngle(currentAngle);
        standardServo.setAngle(currentAngle);
    }        
    delay(200);  // if either button is pressed and held down, either increase or decrease the angle 5 degrees every 0.2 second
}
```

### What to Expect

<!-- // description of how both servos will turn in a particular direction while a button is depressed, the buttons control the direction of rotation -->

When one button is pressed, both servos will turn to one direction; when the other button is pressed, they both turn to the other direction. If either button is pressed and held down,
the servos' shaft position will either increase or decrease by 5 degrees every 0.2 seconds.

<!-- TODO: IMAGE video of the servos turning -->

### A Closer Look at the Code

<!-- // introduced object oriented programming for the first time in this code -->

In this code, we introduce a very important, new concept: Object Oriented Programming (OOP). We will take a look at some of the key elements of OOP: classes, objects, constructors and class members.


#### Object Oriented Programming

<!-- // DONE: this is a huge block of text, see if we can add some descriptive headers so it doesn't seem like an intimidating thing that will take forever to read -->

In our experiment, we have two servos, they operate in the same way but some attributes (parameters) are slightly different: attached pin number, minimum pulse width, maximum pulse width. This is exactly the kind of scenario that spurred the creation of Object Oriented Programming. Ultimately, the goal of OOP is to model programmatic interactions as objects interacting with each other.

To that end, we create **objects** with attributes (what it is) and methods that act on the attributes (how it behaves). Objects are constructed out of templates called **classes** in which we define what attributes the object will have, and the functions that will interact with them.

<!-- // DONE: before the next sentence, we need to go into further detail about what a class really is, and how it defines methods (functions) -->
<!-- // DONE: after that we need to drive home the point that an object is an instance of a particular class. the existing text touches on this but we need to emphasize it! -->

#### Classes

So if classes are templates, what exactly do they do?

Let's take it back to our code above. First thing you'll notice relating to our class is probably:

```c++
class ServoMotor
{
    ...
};
```

This is our class definition! All the code inside defines what an object of `ServoMotor` would encompass. It's got attributes, methods, `public`'s, and `private`'s. One interesting thing about the class is that no attribute inside a class actually exist in memory. That is until we make an object out of it.


>Most object oriented languages allow functions inside classes to be executed without an object under certain conditions.

#### Objects

Where in our code do we create objects? Right here:

```c++
ServoMotor smallServo (9, 500, 2000);     // initialize DXW90 small servo (500us to 2000us) at pin 9
ServoMotor standardServo (10, 0, 2500);     // initialize S3003 standard servo (0us to 2500us) at pin 10
```

The syntax to create objects from a class is very similar to creating variables of a certain type. In fact that's one way to think about classes and objects - types and variables with fancier internals.

Unlike variables, we work with objects by calling the methods (functions) defined by the class. The variables inside objects are not normally manipulated from 'outside' the object.

Let's look back to the objects and classes to variables and types analogy. If objects are like variables of a class, then why do we have brackets and pass in arguments like a function?

This is because the attributes of an object are fancier than `int`s or `char`s - objects can have other objects as variables. So in order to provide the flexibility needed, a function is called to create an object by setting up all the things needed for it to work as expected. The syntax in the snippet above is actually short-hand for a two-step process:

* Call a function to create an object and set up the internals, returning a reference to the created object.
* Give that reference a name (`smallServo` and `standardServo` above)

Then if you want an object, what function should you call?

#### Constructors

Let's take a look at this snippet:

```c++
	ServoMotor(int pinNumber, float minPWus, float maxPWus){

		// pass in the pin number, max and min pulse width to private variables
		minPW = minPWus;
		maxPW = maxPWus;
		pin = pinNumber;

		// calculate the pulse width change for each degree
		rate = (maxPWus - minPWus)/(maxAngle - minAngle);
	}
```

This is the constructor of `ServoMotor` class. Whenever the code demands that a `ServoMotor` object be created,

More formally, a constructor is function of the class that have the exact same name as the class and will be automatically called when a class object is declared.

#### Class Members

You'll occasionally hear people refer to 'members' of a class. A class member is a variable or a function declared as a part of the class template.

In most object oriented languages, class members have access rights - either `private` or `public`. A `private` member can only be used within the class. While a `public` member can be called outside the class. For our `ServoMotor` class, we have seven private members (six variables and one object) declared under `private:` and two public member functions defined under `public:`. Our public member functions include the constructor `ServoMotor()` and another function `setAngle()`.

#### Putting it Together

To use our `ServoClass` template, we declared our two objects in the global scope similar to declaring global variables:

```
ServoMotor smallServo (9, 500, 2000);
ServoMotor standardServo (10, 0, 2500);
```

However, our `ServoMotor` objects can only be defined after our `ServoMotor` class has been defined. In addition, We can call `setAngle()` on either of the two objects in our main program:

```
smallServo.setAngle(90);
standardServo.setAngle(90);
```

This is because `setAngle()` member function is defined under `public:`.

Furthermore, notice we have seven `private` member variables but we only use passed in three parameters (`pinNumer`,  `minPWus`, `maxPWus`) to three private member variable (`pin`, `minPW`, `maxPW`) in our constructor. This is because the three parameters are the only different parameters between different servo objects. The `rate` variable is calculated from the three parameters. The minimum and maximum servo angle (`minAngle` and `maxAngle`) are set to `0` degree and `180` degree for all `ServoMotor` objects.

Lastly, we use a `Servo` object from the Arduino Servo library within our own `ServoMotor` class to interface with our Arduino Dock pins directly, so we don't have to directly handle the PWM driver of the Arduino Dock!
