## Controlling Servos

// intro to using pwm to control servos, this experiment will involve controlling servos using physical buttons


// ### What is Pulse Width Modulation?

<!-- pwm -->
```{r child = '../../shared/pwm.md'}
```

// ### Servo-Motors

<!-- servo -->
```{r child = '../../shared/servos.md'}
```

### Building the Circuit

// simple circuit with both the small and regular servo attached - when one button is pressed, they both turn to one direction, when the other button is pressed, they both turn to the other direction

For the circuit, we will need a small (Sub-micro size) servo motor(MicroServo DXW90) and a standard size servo motor(Futaba S3003). In addition, we will need two push buttons, each with their own debounce circuits setup on a breadboard. When one button is pressed, both servos will turn to one direction; when the other button is pressed, they both turn to the other direction.

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

// wiring the servos: vcc, gnd, and a separate signal wire for each servo
// wiring the two push-button switches: can reuse the wiring push button text from previous articles

1. Connect the two push buttons with their seperate debounce circuits same as previous tutorials.
    * Set up two push buttons, each with their own debounce circuit similar to tutorial 4, don't connect to Arduino Dock yet. 
    * Connect the point in the first debounce circuit between the 5kohm resistor and the capacitor to pin 2 of the Arduino Dock.
    * Connect the point in the second debounce circuit between the 5kohm resistor and the capacitor to pin 3 of the Arduino Dock.
    * Connect the Vcc of both debounce circuit to the positive (+) power rail.
    * Connect the ground of both debounce circuit to the negative (-) power rail.
1. Connect the two servo motors.
    * The small servo has 3 wires: connect the black wire to negative power rail, the red wire to positive power rail, and the orange (signal) wire to pin 9. 
    * The standard servo also has 3 wires: connect the black wire to negative power rail, the red wire to positive power rail, and the white (signal) wire to pin 10.
    * The Arduino Sketch will set the servo motors at 90 degree initially. After flashing the arduino sketch and wait until the servos settle on their initial position, attach your favourite servo horn on each servo at 90 degrees.
1. Connect the breadboard power rails to Arduino Dock.
    * Connect the negative power rail to ground (GND).
    * Connect the positive power rail to 5V. Don't worry if the servo rotates a bit when you power it on.

### Writing the Code

// introduce the use of classes in arduino sketches: create a class to control servos
//  - need to pass in the signal pin number & minimum and maximum pulse widths in the constructor
//    -> do this in the setup() function
//    -> the constructor should calculate the pulse width change for each degree - should be a class member
//  - function where you pass in an angle and it programs the duty cycle for the pin of the servo
//  implementation details:
//    - will need to define the class at the beginning of the sketch
//    - have two global objects of the class
//    - instantiate the two global objects in the setup function
//    - will be available for use once the setup function is run

// set the servos to 90˚ in the setup function

// have polling code to increment/decrement the angle of both of the servos while a button is pressed

``` arduino
// import the Arduino Servo library and define it
#include <Servo.h>
  
int incrementButton = 2;
int decrementButton = 3;
int currentAngle = 90;

// class to control servo motors
class ServoMotor
{
  private:      // variables or functions that can only be used within the ServoMotor class
  Servo servo;    // Servo object from the Arduino Servo library
  float rate;    // rate of pulse width change per degree
  float minPW, maxPW;   // min and max pulse width in microseconds (uS)
  int minAngle = 0;
  int maxAngle = 180;
  int pin;

  public:     //  variables or functions which can be called outside in the main program
  // constructor with same name as class, will be automatically called when a class object is declared
  // pass in the pin number, max and min pulse width and calculate the pulse width change for each degree
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
    if (angle > maxAngle || angle < minAngle){
       if (angle > maxAngle){
          Serial.println("Servo angle over maximum. Please press decrease button");
          return;
       }
       else{
          Serial.println("Servo angle lower than minimum. Please press increase button");
          return;
       }
    }

    // convert the angle to pulse width in microseconds(uS) using the rate previously calculated in the constructor
    float PWus = minPW + rate * angle;
    
    // initialize the servo pin using the Arduino Servo library
    servo.attach(pin);
    
    // set the servo angle by sending the calculated pulse width to the servo motor using the Arduino Servo library
    servo.writeMicroseconds(PWus);
  }
};

// initalize two servo objects, one for each motor attached
ServoMotor smallServo (9, 500, 2000);     // initialize DXW90 small servo (500us to 2000us) at pin 9
ServoMotor standardServo (10, 0, 2500);     // initialize S3003 standard servo (0us to 2500us) at pin 10
      
void setup() {    // codes to be ran once
  Serial.begin(9600);  // initializing serial communication with the Omega
  
  // initialize the pins connected to the increment and decrement buttons
  pinMode(incrementButton, INPUT);
  pinMode(decrementButton, INPUT);
  
  // set the initial angle of the two servos to the 90 degrees
  smallServo.setAngle(currentAngle); 
  standardServo.setAngle(currentAngle);
}

void loop() {   // codes to be ran continously
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
    delay(200);  // if either button is pressed and hold down, either increase or decrease the angle 5 degrees every 0.2 second
}
```

#### What to Expect

// description of how both servos will turn in a particular direction while a button is depressed, the buttons control the direction of rotation

When one button is pressed, both servos will turn to one direction; when the other button is pressed, they both turn to the other direction. If either button is pressed and hold down, either increase or decrease the angle 5 degrees every 0.2 second.

#### A Closer Look at the Code

// introduced object oriented programming for the first time in this code

In this code, we introduce a new concept: the object oriented programming (OOP). We will take a look at some of the key elements of OOP: classes, objects, constructors and class members.

// introduce the use of classes in arduino sketches: create a class to control servos
//  - need to pass in the signal pin number & minimum and maximum pulse widths in the constructor
//    -> do this in the setup() function
//    -> the constructor should calculate the pulse width change for each degree - should be a class member
//  - function where you pass in an angle and it programs the duty cycle for the pin of the servo
//  implementation details:
//    - will need to define the class at the beginning of the sketch
//    - have two global objects of the class
//    - instantiate the two global objects in the setup function
//    - will be available for use once the setup function is run

##### Object Oriented Programming

// talk about how we're using two servos, they operate in the same way but some parameters are slightly different. So we wrote a class that can be used to control both servos independently.
// this is accomplished by instantiating two objects of the class - talk about the constructors and how we input the pertinent values

// talk about constructors and class members

// can borrow from the starter kit - 7seg article

In our experiment, we have two servos, they operate in the same way but some attributes (parameters) are slightly different: attached pin number, minimum pulse width, maximum pulse width. This is where object oriented programming (OPP) becomes handy. In OPP, a class is similar to a template and a object is defined based on the class template with its own specific attributes. For our example. We setup our template inside "class ServoMotor{...};". After that we defined two objects smallServo and standardServo, each with their own specific and different attributes. 

These attributes are defined in the constructor of the ServoMotor class. A constructor is function of the class that have the exact same name as the class and will be automatically called when a class object is declared. Think of the constructor as a initialization function whose main purpose is to pass in all the class parameter (attributes). Our constructor also calculates the rate of the pulse width change for each degree. Also notice there is no "void" in front of our constructor function.

A class member is a variable or a function declared as a part of the class template. It can be either a private, which can only be used within the class or a public, which can be called outside the class. For our ServoMotor class, we have seven private members (six variables and one object)declared under "private:" and two public member functions defined under "public:". Our public member functions include the constructor ServoMotor() and another function setAngle(). 

To use our ServoClass template, we declared our two objects in the global scope similar to declaring global variables:

ServoMotor smallServo (9, 500, 2000);
ServoMotor standardServo (10, 0, 2500);

However, our ServoMotor objects can only be called after our ServoMotor class has being defined. In addition, We can call setAngle() in our main program by 

smallServo.setAngle(90);
standardServo.setAngle(90);

This is because setAngle() member function is defined under "public:".

Furthermore, notice we have seven private member variables but we only use passed in three parameters (pinNumer,  minPWus, maxPWus) to three private member variable (pin, minPW, maxPW) in our constructor. This is because the three parameters are the only different parameters between different servo objects. The (rate) variable is calculated from the three parameters. The minimum and maximum servo angle (minAngle and maxAngle) are set to 0 degree and 180 degree for all servo objects. Lastly, we can even use an Servo object from the Arduino Servo library within our own ServoMotor class! Just remember to include the library: #include <Servo.h>
