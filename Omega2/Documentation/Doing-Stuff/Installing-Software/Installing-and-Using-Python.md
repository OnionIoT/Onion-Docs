---
title: Using Python
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 2
---

<!-- // refer to the existing article for guidance -->

## Installing and Using Python {#installing-and-using-python}

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


### Getting More Python Modules

There's two ways to install additional Python modules on the Omega, either using `opkg` to install precompiled packages, or using `pip`, the Python package manager.

### Using `opkg` to Install Python Modules

Once you've installed Python (or Python3), you can use `opkg` to install additional Python packages. This is probably the quicker method, but the selection of available packages is likely smaller than when using `pip`.

To see a list of the python packages available via `opkg`, enter the following commands:

```
opkg update
opkg list | grep python
```
> Note: use `opkg list | grep python3` to get the packages specific to Python3


This will list all the available packages with python in their name. You can run:

```
opkg install <PACKAGE NAME>
```

To install the desired package.

>For more on `opkg` you can check out our [guide to using opkg](#using-opkg)

For example, if you would like your script to make HTTP requests, you will need the `urllib3` package:

```
opkg update
opkg install python-urllib3
```

And then your scripts can import the module:

```
import urllib3
```

### Using `pip` to Install Python Modules

The official Python package manager, `pip`, is the standard way of installing Python modules on a system. You will get a large selection of available packages from which to choose.

#### Installing `pip`

We'll need to first install `pip` on the Omega:

```
opkg update
opkg install python-pip
```

> Note: use `opkg install python3-pip` to install `pip` for Python3

#### Installing Modules

To install a module:

```
pip install <module name>
```

Let's say I'm writing a script that uses MQTT and would like to use the `paho-mqtt` module:

```
pip install paho-mqtt
```

> Much like `opkg`, `pip` is a feature-complete package manager. Run `pip --help` to see more usage options or look up their [documentation](https://packaging.python.org/installing/).



#### Fixing "No space left on device"

If you're trying to install a Python module with `pip` and get an error like the following:

```
root@Omega-C71D:/# pip3 install boto3
Collecting boto3
...
Collecting botocore<1.25.0,>=1.24.13 (from boto3)
  Downloading https://files.pythonhosted.org/packages/a5/34/567e87ece4328f51a6db92db8c58584aa9525603c86aff5eb77bfc713b41/botocore-1.24.13-py3-none-any.whl (8.6MB)
    100% |████████████████████████████████| 8.6MB 262kB/s 
Could not install packages due to an EnvironmentError: [Errno 28] No space left on device
```

This is due to pip using the /tmp directory for work by default.  The tmpfs /tmp directory is too small for very large packages.  This can be overridden with the TMPDIR environment variable.  It is recommended to [boot from external storage](#boot-from-external-storage).

```
mkdir /root/temp
export TMPDIR=/root/temp
pip3 install <large_package>
```


#### Fixing the Setup Tools Issue

If you're trying to install a Python module with `pip` and get an error like the following:

```
root@Omega-296A:~# pip install paho-mqtt
Collecting paho-mqtt
  Downloading paho-mqtt-1.2.tar.gz (49kB)
    100% |████████████████████████████████| 51kB 215kB/s
Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-cHKrSf/paho-mqtt/
```

Don't worry! It's just a small configuration issue with the `setuptools` module and cab be **easily fixed** with the following command:

```
pip install --upgrade setuptools
```

Now you'll be able to successfully use `pip`:

```
root@Omega-296A:~# pip install --upgrade setuptools
Collecting setuptools
  Downloading setuptools-34.2.0-py2.py3-none-any.whl (389kB)
    100% |████████████████████████████████| 399kB 109kB/s
Collecting appdirs>=1.4.0 (from setuptools)
  Downloading appdirs-1.4.0-py2.py3-none-any.whl
Collecting packaging>=16.8 (from setuptools)
  Downloading packaging-16.8-py2.py3-none-any.whl
Collecting six>=1.6.0 (from setuptools)
  Downloading six-1.10.0-py2.py3-none-any.whl
Collecting pyparsing (from packaging>=16.8->setuptools)
  Downloading pyparsing-2.1.10-py2.py3-none-any.whl (56kB)
    100% |████████████████████████████████| 61kB 343kB/s
Installing collected packages: appdirs, pyparsing, six, packaging, setuptools
Successfully installed appdirs-1.4.0 packaging-16.8 pyparsing-2.1.10 setuptools-34.2.0 six-1.10.0
root@Omega-296A:~# pip install paho-mqtt
Collecting paho-mqtt
  Using cached paho-mqtt-1.2.tar.gz
Installing collected packages: paho-mqtt
  Running setup.py install for paho-mqtt ... done
Successfully installed paho-mqtt-1.2
```

<!-- TODO: maybe get rid of the preceding printout? -->


### Using Python

Since the Omega is a Linux computer, it's really easy to get started with Python on the Omega. You can enter `python` in your command-line to start the interpreter.

>If you've installed Python3, you'll need to enter `python3` in your command-line to get started.

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
import os, datetime, time, subprocess

# find the path to the Omega LED
ledName = subprocess.check_output(["uci", "get", "system.@led[0].sysfs"])
ledTriggerPath = "/sys/class/leds/%s/trigger"%(ledName.rstrip())

## Set the Omega LED trigger to "timer" so that it blinks
with open(ledTriggerPath, "w") as trigger:
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
with open(ledTriggerPath, "w") as trigger:
        trigger.write("default-on")

```

>To save and exit your file, hit `ESC` and then enter `:wq`.

You can execute the script using the following command:

```
python /root/greeting.py
```

> Note: If you installed Python3, you would enter `python3` instead of `python`.


And you'll see the following output:

```
root@Omega-2757:~# python /root/greeting.py
Good evening.

```

During this time your Omega's LED will be blinking on and off.



### Onion Python Modules

We've developed modules for controlling the Omega's GPIOs and several Expansions. Check out the documentation for the Modules for more details:

* [Controlling the Omega's GPIOs](#gpio-python-module)
* [Controlling the OLED Expansion](#oled-expansion-python-module)
* [Controlling the PWM Expansion](#pwm-expansion-python-module)
* [Controlling the Relay Expansion](#relay-expansion-python-module)


### Going Further

This section will give you more information on how you can use Python on the Omega to create fantastic projects.

#### Learning Python

<!-- // link to some python documentation and guides for more info on getting started with python -->
[Python 2.7 documentation](https://docs.python.org/2/)<br>
[Python 3 documentation](https://docs.python.org/3/)
