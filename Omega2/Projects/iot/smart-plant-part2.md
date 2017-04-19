<!-- comment: anything in triangle brackets is meant to be replaced with text -->
<!-- comment: see `Omega2/Projects/oled/twitter-feed.md` for an example -->

## <PROJECT TITLE>

// brief intro to the project

// include a photo of the final result

### Overview

**Skill Level:** [Beginner|Intermediate|Advanced]

**Time Required:** <a time estimate to complete the project>

// go into some detail here about how we're going to be implementing the project
//	eg. which programming language we'll be using, APIs
//	include links to any api or module references

### Ingredients

// a numbered list of all physical items used to make this project
//	all items should be linked to a place online where they can be bought
//	the Onion items should be linked to their corresponding Onion store page

1. Onion Omega2 or Omega2+
1. Any Onion Dock that supports Expansions: Expansion Dock, Power Dock, Arduino Dock 2
1. Onion OLED Expansion



### Step-by-Step

Follow these instructions to set this project up on your very own Omega!

// each step should be simple


#### 1. Prepare

You'll have to have an Omega2 ready to go, complete the [First Time Setup Guide](https://docs.onion.io/omega2-docs/first-time-setup.html) to connect your Omega to WiFi and update to the latest firmware.


#### 1. Complete Part 1 of the Project



#### 1. Install Required Software on the Omega

```
opkg update
opkg install mosquitto-client mosquitto-ssl
```

```
cd /root
wget https://raw.githubusercontent.com/Losant/losant-mqtt-ruby/master/lib/losant_mqtt/RootCA.crt
```

#### 1. Register for Losant

#### 1. Create a Losant Application

Application



gateway device

peripheral device

access key

workflow

#### 1.

```
vi /etc/mosquitto/mosquitto.conf
```

Add to the top:
```
### LOSANT BRIDGE CONFIGURATION ###

# For debugging
log_type all

# Bridge to Losant
connection bridge-to-losant
address broker.losant.com:8883
bridge_cafile /root/RootCA.crt
cleansession true
try_private false
bridge_attempt_unsubscribe false
notifications false
remote_clientid <GATEWAY-DEVICE-ID>
remote_username <ACCESS-KEY>
remote_password <ACCESS-SECRET>
topic losant/<PERIPHERAL-DEVICE-ID>/state out 0
topic losant/<PERIPHERAL-DEVICE-ID>/command in 0

### END OF LOSANT BRIDGE CONFIGURATION ###
```

Highlight with photos where to find gateway device id, peripheral device id, and the access key + secret


Restart Mosquitto for the changes to take effect:
```
/etc/init.d/mosquitto restart
```


#### 1. Test Losant Connection

```
mosquitto_pub -t losant/58f43ef3ca2ee50001687620/state -m '{"data":{"soilMoisture":"1234"}}'
```

insert photo of debug

#### 1. Create a Losant Dashboard

photos of creating the Dashboard

#### 1. Report the Smart Plant Data to Losant

// TODO: update code to read an mqtt argument for the topic to which to publish

1. first kill the existing smart plant process (if it's running)

```
root@Omega-F11D:~/smart-plant# ps | grep smart
 3183 root      1184 S    grep smart
```

// TODO: replace the above with running code

2. try it out



### Code Highlight

// one or two paragraphs (max) about something cool we did in the code
//	just give a brief description/overview and provide links to where they can learn more (Onion Docs, online resources, etc)
