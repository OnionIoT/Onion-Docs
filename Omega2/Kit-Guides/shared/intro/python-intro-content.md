As an introduction, this article will cover some of the basics so we can hit the ground running!

Python is a high-level, interpreted language designed for scripting. It supports Object Oriented Programming - which is a handy framework that we’ll be using quite a bit.

The high-level part means that Python reads closer to English than machine instructions and abstracts away many of the low-level hardware intricacies. The interpreted part means that Python code is executed line-by-line by the computer as it’s being run - as opposed to languages like C where it is first compiled before it can be run.

### How we'll use Python

<!-- // * this guide will provide complete python scripts which can be copied to your Omega and executed. each experiment will describe the script and will focus on interesting parts of the code -->

The experiments will provide code that works out of the box that can be directly copied to the Omega and run. We'll also discuss more interesting sections of the code in detail.


### Python Syntax Overview

<!--
// give an example blocks of code to describe the following concepts:
//	* indentation syntax for if, for, while statements
//		* describe which is the statement and which is the body, can be accomplished with a screenshot with some writing over-top
//	* indentation syntax for functions
//		* same as above
//	* comments in the code
-->

``` python
import time

# print ('This line will not be printed')

greeting = 'Hello world!'

print (greeting)

for count in range(0,10):
    if (count % 2 == 0):
        print ('Tick')
    else:
        print ('Tock')
    print (count)
    time.sleep(0.5)
```

The above is a block of Python code with all the basic building blocks of the language. Let's go through it bit by bit.

#### Variables


``` python
greeting = 'Hello world!'
```

The equals sign (`=`) assigns the string 'Hello world!' to the variable named `greeting`.

All variables in Python are created this way with the assignment operator.

#### Comments

``` python
# This is a comment
```

Comments in Python start with a `#`. Any text after the hash in the same line will be ignored by the interpreter.

#### Functions

``` python
print ('just a function')
```

Function statements

Functions in Python have two parts: a function name and a list of arguments that are sent to it.


| Name  | Argument          |
|-------|-------------------|
| print | 'just a function' |

The number of arguments that a function takes can be zero. Some functions return a value that you can assign to a variable.


#### Logic

``` python
if (count % 2 == 0):
    print ('Tick')
else:
    print ('Tock')
```

The `if/else` structure is used to evaluate variables and make decisions based on them. All indented lines after the `if` statement will be executed **if the condition is met**. The first un-indented line after the `if` statement ends the statement. For `else`, all indented lines after the `else` line will be executed **when the condition of the if statement is unmet**. So in the code above, only one option gets executed (either 'Tick' or 'Tock') when the interpreter gets to this part. Which one depends on the value of `count`.

Extra evaluation statements can be inserted as an `elif` block like so:

``` python
if (count % 2 == 0):
    print ('Tick')
elif (count == 3):
    print ('Tack')
else:
    print ('Tock')
```
This adds a third option - all indented code after the `elif` statement will be executed if:

* The `if` condition is **unmet**
* AND the `elif` condition is **met**

Now one of **three** options will be executed, printing either 'Tick', 'Tock', or 'Tack' depending on value of `count`.

#### Looping

``` python
# For-loop with a counter variable
for count in range(0,10):
    print (count)

# While-loop - checks condition first, then starts the loop
while (count <= 10):
    print (count)
```

The for-loop can iterate over any list, executing all indented code after the `for` statement as many time as the number of elements in the list. The range function returns a list of integers in the given range. So the for-loop above will run 10 times, same as the example up top. However this loop will print the count of each cycle instead of 'Tick' and 'Tock'.

The while loop checks a single condition every loop, so it's useful for infinite loops and checking unique conditions. Since `count` doesn't change during the while loop, it will run forever assuming `count` is no greater than 10, continuously printing an unchanging value of `count`.


#### Using Libraries

``` python
# Importing a library
import time
```

The `import` statement above adds all the functionality of the `time` standard library to be available in your program.

Calling a function included in the library is done using the `.` notation - `time.sleep()` will call the `sleep()` function in the `time` library.


### Learning More about Python

<!--
// * there is a wealth of tutorials and guides on Python online, if you're unsure of how or why we did something, consult the following resources:
//	* programmers guide for getting started with Python: https://wiki.python.org/moin/BeginnersGuide/Programmers
//	* beginners guide for getting started with python: https://wiki.python.org/moin/BeginnersGuide/NonProgrammers
-->

Python is a very popular language, so there's a tremendous amount of tutorials out there. If you're still unsure of how parts of our code work, we recommend taking a look at the guides over at the Python Wiki for [programmers](https://wiki.python.org/moin/BeginnersGuide/Programmers) or [non-programmers](https://wiki.python.org/moin/BeginnersGuide/NonProgrammers).
