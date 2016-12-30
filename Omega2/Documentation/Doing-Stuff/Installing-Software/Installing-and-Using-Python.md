---
title: Using Python
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 2
---

<!-- // refer to the existing article for guidance -->

## Installing and Using Python {#software-installing-and-using-python}

<!-- // brief intro to Python (scripting language, easy to write) -->

Python is a widely used scripting language that emphasizes code readability and simplicity. It's an excellent language for developing programs on the Omega, and it's incredibly easy to get started.


### Installing Python

The Omega supports Python, we recommend installing the light version to save on space.

The light version takes about 2.5MB of space on the Omega, whereas the full version is approximately 6.3MB.

<!-- // LATER: TODO: point to root overlay article -->
<!-- >You can increase the storage space on your Omega using an external USB Storage device. For a guide on how to do that you can read our tutorial on [how to use a USB storage device on the Omega](#usb-article) -->

#### Python 2.7
We are going to use `opkg` to install Python 2.7. Enter the following command to update your package manager:

```
opkg update
```

Now you can install python-light:

```
opkg install python-light
```

or the full version of python:

```
opkg install python
```


#### Python3

The light and full version of Python3 are also available via `opkg`. To install Python3, start by updating your package manager:
```
opkg update
```

Now you can install python3-light:

```
opkg install python3-light
```

or the full version of python3:

```
opkg install python3
```


#### Installing Additional Python Modules

You can choose to install the light version of Python or Python3, and then install the individual packages that you require.

To see a list of the python packages available via `opkg`, enter the following commands:

```
opkg update
opkg list | grep python
```
*Note: enter `opkg list | grep python3` to get the packages specific to python3*


This will list all the available packages with python in their name. You can run:

```
opkg install <PACKAGE NAME>
```

To install the desired package.

>For more on `opkg` you can check out our [guide to using opkg](#software-using-opkg)

<!-- // DONE: add note about installing python3 packages -->

<!-- TODO: LATER: talk about pip -->

### Using Python

Since the Omega is a Linux computer, it's really easy to get started with Python on the Omega. You can enter `python` in your command-line to start the interpreter.

>If you've installed python3, you'll need to enter `python3` in your command-line to get started.

Note that the interpreter is a good tool for quickly testing some code, but the real power of Python comes from writing reusable scripts.


#### Writing a Python Script on the Omega

<!-- // example of writing a basic python script that changes the trigger of the Omega LED -->
<!-- // example of how to run it from the command line -->

<!-- // DONE: change the os.system calls to actually open the file, write to it, and then close it -->

<!-- //DONE: reorder the text so that it's logical and friendly -->

Let's begin writing our Python script by creating the file:

```
vi /root/greeting.py
```

Now we'll copy the following code into the file:


```Python
# Importing packages
import os, datetime, time


## Set the Omega LED trigger to "timer" so that it blinks
with open("/sys/class/leds/onion:amber:system/trigger", "w") as trigger:
          trigger.write("timer")


## Print a gretting based on the time of day
# Gets the current time
currentTime = datetime.datetime.now()

# Sets the Omega LED trigger to "default-on"
if currentTime.hour < 12:
        print 'Good morning.'
elif 12 <= currentTime.hour < 18:
        print 'Good afternoon.'
else:
        print 'Good evening.'


## Wait 5 seconds and then set the Omega LED back to being always on
# Waits for 5 seconds
time.sleep(5)

# Set the Omega LED back to being always on
with open("/sys/class/leds/onion:amber:system/trigger", "w") as trigger:
        trigger.write("default-on")

```

>To save and exit your file, hit `ESC` and then enter `:wq`.

You can execute the script using the following command:

```
python /root/greeting.py
```

>Note: If you installed python3, you would enter `python3` instead of `python`.


And you'll see the following output:

```
root@Omega-2757:~# python /root/greeting.py
Good evening.

```

During this time your Omega's LED will be blinking on and off.


### Going Further

This section will give you more information on how you can use Python on the Omega to create fantastic projects.

#### Learning Python

<!-- // link to some python documentation and guides for more info on getting started with python -->
[Python 2.7 documentation](https://docs.python.org/2/)<br>
[Python 3 documentation](https://docs.python.org/3/)

<!-- #### Omega Python Modules -->

<!-- // there are a bunch of python packages created by onion to control anything from omega gpios to Expansions -->
<!-- // have a list of articles with links -->
<!-- // note: we will create a fourth documentation section, reference, to house all of the existing documentation -->



<!-- ### Using Pip - Python's package manager -->

<!-- // it's possible to use pip to get additional python packages, just not for packages that need to be compiled -->
<!-- // ask michael for implementation details -->
