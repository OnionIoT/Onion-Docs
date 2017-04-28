## Internet Lock - Part 2 {#internet-lock-p2}

Let's take what we did in Internet Lock - Part 1, and add a program to control it from Twitter!

<!-- comment: anything in triangle brackets is meant to be replaced with text -->
<!-- comment: see `Omega2/Projects/oled/twitter-feed.md` for an example -->

// brief intro to the project

// include a photo of the final result

**Disclaimer: This security-related project is just that: a *project*. This is not intended to be a fully-featured nor robust home security solution. Use your own judgment when applying this project to securing your belongings, property, etc. By doing this project, you accept all risk and Onion cannot be held responsible for any damages or misuse.**

### Overview

**Skill Level:** Intermediate

**Time Required:** 30 minutes

The code will be written in Python and we'll be making use of [Twitter's Streaming APIs](https://dev.twitter.com/streaming/overview) to grab Tweet data. Specifically, the code uses the [Tweepy library](http://www.tweepy.org/) to manage authentication and keeping a persistent HTTP connection to Twitter.

Same as before, the code used to handle this setup can be found in the [iot-door-lock repository](https://github.com/OnionIoT/iot-door-lock) on GitHub.

### Ingredients

Unlike Part 1, the dependencies for the Python Twitter software requires more space than is available on the Omega2 standard model by default. You will either have to [boot from external storage](https://docs.onion.io/omega2-docs/boot-from-external-storage.html) or use an Omega2+ instead.

We will be using the same hardware components as in Part 1:

1. Onion Omega2+, or Omega2 with external storage
1. Any Onion Dock that supports Expansions: Expansion Dock, Power Dock, Arduino Dock 2
1. Onion Relay Expansion
1. An electric lock *
1. Lock mounting tools - screws, bolts, extra wires, and appropriate tools
1. Appropriate power supply for your lock
    * we found 12V/1A DC supply to be compatible with most locks

\* We recommend a simple power locking, normally unlocked lock so you don't get locked out when there's no power.

Here's what our list looked like - minus the mounting tools and parts.
![The components we need](./img/door-lock-p1-ingredients.jpg)

### Step-by-Step

Follow these instructions to control the smart lock from Twitter on your very own Omega!

#### 1. Prepare

You'll have to have an Omega2 ready to go, complete the [First Time Setup Guide](https://docs.onion.io/omega2-docs/first-time-setup.html) to connect your Omega to WiFi and update to the latest firmware.


#### 1. Complete Part 1 of the Project

This project builds on the first part of the Smart Plant project. If you haven't already completed the [first part](#smart-plant-p1), go back and do it now!

#### 4. Create a Twitter Application

We'll need to create a Twitter Application in order to be able to use Twitter's APIs to grab Tweets. Specifically, our code needs an API Key and API Secret in order to authenticate with Twitter before we can use the APIs:

1. Head over to https://apps.twitter.com and sign in with your Twitter handle

  ![twitter apps splash screen](../oled/img/twitter-feed-screenshot-0.png)

1. Fill in the form details for your application. Twitter app names must be unique globally, so try calling it `omega-ABCD-door-lock`, where ABCD are the 4 digits in your Omega's hostname.

  ![twitter apps create app](../oled/img/twitter-feed-screenshot-1.png)

1. Read and agree to the Twitter Developer Agreement and hit Create your Twitter application.

  ![twitter apps create app part 2](../oled/img/twitter-feed-screenshot-2.png)

  > Note that your Twitter account must have an associated mobile phone number before Twitter will allow you to create an application!

1. Your Application is now created!

  ![twitter app created](../oled/img/twitter-feed-screenshot-3.png)

1. Head over to the **Keys and Access Tokens** tab to grab the info we need

  ![twitter app keys](../oled/img/twitter-feed-screenshot-4.png)

1. Scroll down to the section called "Your Access Token", and click "Create my access token".

    // TODO: screenshot
  ![twitter app access token](./img/door-lock-access-token.png)

#### Install Dependencies

On your Omega, run the following commands:

```
opkg update
opkg install python-pip

### Code Highlight

// one or two paragraphs (max) about something cool we did in the code
//	just give a brief description/overview and provide links to where they can learn more (Onion Docs, online resources, etc)
