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

## Building the Circuit

// simple circuit with both the small and regular servo attached - when one button is pressed, they both turn to one direction, when the other button is pressed, they both turn to the other direction

For the circuit, we will need a small servo motor(MicroServo DXW90) and a standard servo motor(Futaba S3003). In addition, we will need two push buttons, each with their own debounce circuits setup on a breadboard. When one button is pressed, both servos will turn to one direction; when the other button is pressed, they both turn to the other direction.


### Hooking Up the Components

// wiring the servos: vcc, gnd, and a separate signal wire for each servo
// wiring the two push-button switches: can reuse the wiring push button text from previous articles

First we will connect the two push buttons with their seperate debounce circuits same as previous tutorials. We will connect the first debounce ciruit to pin 2 for increasing the servo angle and the other debounce circuit to pin 3 for decreasing the servo angle. Don't forget to connect the 5V and ground of the both debounce circuit.

Next we will connect the servo motors. The small servo has 3 wires: connect the black wire to GND, the red wire to 5V, and the orange (signal) wire to pin 9. Don't worry if the servo rotates a bit when you power it on.

The standard servo also has 3 wires: connect the black wire to GND, the red wire to 5V, and the white (signal) wire to pin 10. The Arduino Sketch will set the servo motors at 90 degree initially. After flashing the arduino sketch and wait until the servos settle on their initial position, attach your favourite servo horn on each servo at 90 degrees.


## Writing the Code

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
  Servo servo;    // 
  float rate;    // rate of pulse width change per degree
  float minPW, maxPW;   // min and max pulse width in microseconds (uS)
  int minAngle = 0;
  int maxAngle = 180;
  int pin;

  public:     //  variables or functions which can be called outside in the main program
  // constructor with same name as class, will be automatically called when a class object is declared
  // pass in the pin number, max and min pulse width and calculate the pulse width change for each degree
  ServoMotor(int pinNumber, float minPWus, float maxPWus){
      // calculate the pulse width change for each degree
      rate = (maxPWus - minPWus)/(maxAngle - minAngle);

      // pass in the pin number, max and min pulse width to private variables
      minPW = minPWus;
      maxPW = maxPWus; 
      pin = pinNumber;
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

### What to Expect

// description of how both servos will turn in a particular direction while a button is depressed, the buttons control the direction of rotation

### A Closer Look at the Code

// introduced object oriented programming for the first time in this code

#### Object Oriented Programming

// talk about how we're using two servos, they operate in the same way but some parameters are slightly different. So we wrote a class that can be used to control both servos independently.
// this is accomplished by instantiating two objects of the class - talk about the constructors and how we input the pertinent values

// talk about constructors and class members

// can borrow from the starter kit - 7seg article
