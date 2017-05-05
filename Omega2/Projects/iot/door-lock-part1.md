## IoT Lock {#internet-lock-p1}

Keys are so last year. With the Omega and the internet, we can unlock things with our keyboard or touchscreen!

In this project, we'll be building an electric lock system with the Omega:

![The omega controlling it](./img/door-lock-p1-1.jpg)

In fact, we use this very setup to control a secondary lock at Onion HQ:

![The lock itself](./img/door-lock-p1-2.jpg)

>Note: in fact, keys are still very useful. We still recommend you to use a normally-open lock and a key-lock in conjunction, as power failure will result in a fail-safe backup instead of locking you out.

**Disclaimer: This security-related project is just that, a *project*. This is not intended to be a fully-featured or robust home security solution. Use your own judgment when applying this project to securing your belongings, property, etc. By doing this project, you accept all risk and Onion cannot be held responsible for any damages or misuse.**

### Overview

**Skill Level:** Intermediate

**Time Required:** 1.5 hours

To accomplish this, we'll use the HTTP server, `uhttpd` on the Omega to listen for the unlock signal through a request and `cgi-bin` scripts to control the lock. When it's set up, we'll be able to to unlock by accessing a web page through a phone, a laptop, or a kerosene powered toaster.


### Ingredients

* Onion Omega2 or Omega2+
* Any Onion Dock that supports Expansions: Expansion Dock, Power Dock, Arduino Dock 2
* Onion Relay Expansion
* An electric lock *
* Lock mounting tools - screws, bolts, extra wires, and appropriate tools
* Appropriate DC power supply for your lock
    * we found 12V/1A DC supply to be compatible with most locks

\* We recommend a simple power locking, normally unlocked lock so you don't get locked out when there's no power.

Here's what our list looked like - minus the mounting tools and parts.
![The components we need](./img/door-lock-p1-ingredients.jpg)

### Step-by-Step

Our instructions will be based on the recommended lock type. If you have an advanced electric lock with multiple settings, you can adjust the instructions as you see fit.

#### 1. Prepare

To get started, we need to set up the Omega and our lock.

First we need an Omega2 ready to go. If you haven't already, complete the [First Time Setup Guide](https://docs.onion.io/omega2-docs/first-time-setup.html) to connect your Omega to WiFi and update to the latest firmware.

Plug in the Relay Expansion, and that's it for the Omega.

![expansion dock and relay expansion](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Hardware-Overview/img/relay-expansion-dock.jpg)

#### 2. Test the lock

Next, read up on the operation of the lock of choice. Our code is based of a simple on/off switch system so it helps to know if it will work with your chosen lock.

It's a good idea to start with a simple circuit to test the hardware. Using a two-wire lock, we'll connect it to our power supply through the Relay Expansion.

>To set up the terminals on the Relay Expansion, turn the screw on the terminal counterclockwise until the metal clamp inside is sitting a bit less than halfway in the bottom of the housing, not too much or the screw might pop out.
>The screw terminal on the barrel jack adapter is a bit different, it will rise and sink depending on the clamp position. When the screw is roughly flush with the top, it is open. To close it, turn clockwise until the screw sinks to about halfway, or until it becomes difficult to continue turning.

* First, connect the **negative (ground) terminal** (usually the black wire) of the lock to the **negative (ground) terminal** of the power supply.
* Next, connect the **positive terminal** of your supply to the **IN** screw terminal of Channel 0 on the Relay Expansion
* Finally, connect the **positive (power) terminal** (usually red) to the **OUT** screw terminal of Channel 0 on the Relay Expansion.

![here's our testing circuit](./img/door-lock-p1-test-circuit.jpg)


Once the lock is wired, connect to the Omega's [command line](https://docs.onion.io/omega2-docs/connecting-to-the-omega-terminal.html#connecting-to-the-omega-terminal) and then switch on the relay:

```
relay-exp -i 0 on
```

If the lock's state changes, you're all set to continue! Before proceeding, Yyu can disable the lock with:

```
relay-exp -i 0 off
```


#### 4. Plan out the Lock Placement

Before getting to software, you should make sure the lock chosen can be mounted to the door with good fit. Take some measurements and plan out the wiring and placement of the Omega/supply so we can quickly follow through once the software is ready to go.

*Measure twice, cut once.*


#### 5. Mount the lock

Now that the pieces work together, it's time to mount your lock! Keep all the components powered off, and take the testing rig apart

![Our wiring setup](./img/door-lock-p1-mounted.jpg)

>At Onion HQ, we've extended the wiring of the lock and routed it to an Omega and power supply right next to the door, but depending on the situation, you may have to do something completely different.

#### 6. Download the Project Code

The code for this project can be found in Onion' [`iot-door-lock` repository](https://github.com/OnionIoT/iot-door-lock) on GitHub. We'll use [`git` to download the code to your Omega](https://docs.onion.io/omega2-docs/installing-and-using-git.html): navigate to the `/root` directory on the Omega, and clone the GitHub repo:

```
opkg update
opkg install git git-http ca-bundle
cd /root
git clone https://github.com/OnionIoT/iot-door-lock.git
```

>If your lock has more modes/controls, feel free to take a look at the code (specially `door.sh`) and make changes that control your lock more effectively.


Now copy the contents of the `www` directory of the repo to the `/www` directory on your Omega, and you should be good to go!

```
cp -r iot-door-lock/www/ www/
```

// TODO: confirm this copy command works


#### 7. Using the IoT Lock

TODO: Need a step on how to access the lock, include a screenshot of the webpage, mention that the omega name works on iphone but not on android (have to use the ip address)


#### Bonus: Automatically Lock/Unlock

We've also included a crontab example, `crontab.txt`, in the repo that sets up the lock to turn on and off at 11AM and 6PM respectively:

```
0 11 * * 1,2,3,4,5 sh /www/cgi-bin/door.sh unlock
0 18 * * 1,2,3,4,5 sh /www/cgi-bin/door.sh lock
#
```

<!-- future TODO: pull the contents of this file from github and then just render it here inside the backticks -->


Here's a quick overview of how it works:

```
# * * * * *  command to execute
# ┬ ┬ ┬ ┬ ┬
# │ │ │ │ │
# │ │ │ │ │
# │ │ │ │ └───── day of week (0 - 7) (0 to 6 are Sunday to Saturday, or use names; 7 is Sunday, the same as 0)
# │ │ │ └────────── month (1 - 12)
# │ │ └─────────────── day of month (1 - 31)
# │ └──────────────────── hour (0 - 23)
# └───────────────────────── min (0 - 59)

# The hash (#) denotes a comment that will be ignored
```




// TODO: teaser on the next step of the project
