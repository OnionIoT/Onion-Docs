## Installing and Using PHP {#installing-and-using-php}

The Onion Omega runs a webserver called uhttpd. It does the heavy lifting for the Omegas built-in running PHP!

We've already set up some basic examples of getting PHP to run, including proof-of-concept scripts and installation instructions. This tutorial walks you through the steps of getting these to work.

<!-- TODO: reupload this to github -->

![PHP example and the Onion Omega](https://dl.dropboxusercontent.com/u/12816733/onion-omega-php-example-1.png)

All you need is a little imagination on how you can use and abuse this with you Onion Omega.

Here are some ideas to get your brain noodling:

1. You could post updates to Thingspeak.com
2. And push updates to PushBullet, so events appear across multiple devices such as a web browser, your iphone, ipad and/or droid
3. Build a security alarm that takes snapshots using a USB webcam


### Installing PHP

Let's get started

First we need to install the required packages. You can use the console, or ideally via SSH:

```
opkg update
opkg install php5 php5-cgi
```

This installs the required PHP packages.

Optionally you can also install the CLI version of PHP using the command below. This allows you to run PHP scripts from the commandline using "php-cli scriptname.php"

```
opkg install php5-cli
```

### Using PHP

In order to make use of our installed PHP package, we need to edit the uhttpd file. You can do this by using this command:

```
vi /etc/config/uhttpd
```

Alternatively, you can copy and paste the changes below from your computer.

```
config uhttpd 'main'
        list listen_http '0.0.0.0:80'
        list listen_http '[::]:80'
        list listen_https '0.0.0.0:443'
        list listen_https '[::]:443'
        option redirect_https '1'
        option home '/www'
        option rfc1918_filter '1'
        option max_requests '3'
        option max_connections '100'
        option cert '/etc/uhttpd.crt'
        option key '/etc/uhttpd.key'
        option cgi_prefix '/cgi-bin'
        option script_timeout '60'
        option network_timeout '30'
        option http_keepalive '20'
        option tcp_keepalive '1'
        option ubus_prefix '/ubus'
```

Add this to the last line of that block of text (there is another block of text after this, I've left that out for simplicity)

```
list interpreter ".php=/usr/bin/php-cgi"
option index_page 'index.php'
```

Press 'ESC' on keyboard, and then ':wq' & 'Enter' to save changes.

Now we need to restart the web server, we do this by running this command:

```
/etc/init.d/uhttpd restart
```

And that's it, the uhttpd server is now capable of parsing PHP files.

#### Testing the Installation

Create a test file & directory by executing the following command:

```
mkdir /www/php
cd /www/php
vi index.php
```

And paste this code into the file & save:

```
<?php
  echo "hello world, I'm PHP running on my Onion Omega!";
?>
```

Press 'ESC' on keyboard, and then ':wq' & 'Enter' to save changes.

Now open your web browser and go to http://omega-ABCD.local/php/

**Note:** If you receive a directory or file permissions issue, run the following command and try again.

```
chmod -R 755 /www/php
```

### A More In-Depth Example

<!-- TODO: this example isn't well documented  -->
This example runs a very simple PHP app through the onion web interface enabling you to fiddle with the RGB LED, and a Relay Expansion. This example works best if you have a Relay Expansion and an Expansion Dock. The webpage should work regardless of your setup - it just might throw some errors your way when you try to interact with it.

First, make sure you have [git installed](#installing-and-using-git).

Next, we'll pull the code from GitHub into `/www/php` so it'll work properly out of the box:

```
cd /www/php/
git clone https://github.com/ageeweb/php_onion
```

Finally, visit your Omega through the browser and see it running!

```
http://omega-ABCD.local/php/php_onion/HowToUse.php
```

It should look something like this:

![PHP example and the Onion Omega](https://dl.dropboxusercontent.com/u/12816733/onion-omega-php-example-1.png)

### Going Further

We've included some links and projects to do with PHP below to give you some inspiration and experience to make Really Cool Stuff!


#### Editing `php.ini`

By default, the PHP configuration file is installed under `/etc/php.ini`.

You can edit the php.ini file by running this command:

```
vi /etc/php.ini
```

#### Community Resources

Ringmaster has kindly provided a [PHP Helper](https://github.com/ringmaster/GPIOHelperPHP) for GPIO. You can read more about this in the [community thread](https://community.onion.io/topic/39/simple-php-web-gpio-example-switching-leds/10).


<!-- TODO: uncomment when projects section up and running -->
<!-- #### Onion Tutorials

We've written some tutorials integrating PHP with various things:

* [PHP and PushBullet](#php-pushbullet-example)
* [DHT11 and DHT22 Temperature Sensors](#php-dht11-dht22-sensor-examples) -->


<!-- TODO: fast-gpio not working, uncomment when fixed -->

<!-- ### `fast-gpio` and PHP


Onion Community member [Chris McCaslin](https://community.onion.io/user/chris-mccaslin) developed a PHP wrapper for the `fast-gpio` package.

#### Installing the Library

First download the library with wget from a [GitHub Gist](https://gist.github.com/Immortal-/a18f58ac5c21ba27921b7626b5a8b06e)

```
wget https://gist.githubusercontent.com/Immortal-/a18f58ac5c21ba27921b7626b5a8b06e/raw/df8e70665523c2a06b503954d10943560d5c189f/OmegaPHP.php
```


#### Using the Library

Here's a quick demo on using the library:

```
<?php
  require 'OmegaPHP.php'; //Require the library from the step above

  $gpio = new OmegaPHP();
  //Turns pin 0 to On or HIGH or 1
  $pin = (int)0; //This is just for my testing purposes You do not have to cast to an int.

  $gpio->SetPIN($pin,HIGH);// Set's the pin to 1 or HIGH
  $returned = $gpio->ReadPin($pin);

  print_r($returned);

  // Prints to screen:
  // 1
?>
``` -->
