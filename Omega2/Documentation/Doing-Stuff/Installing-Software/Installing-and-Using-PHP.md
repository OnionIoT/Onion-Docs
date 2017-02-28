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
opkg install php7 php7-cgi
```

This installs the required PHP packages.

Optionally you can also install the CLI version of PHP using the command below. This allows you to run PHP scripts from the commandline using "php-cli scriptname.php"

```
opkg install php7-cli
```

### Using PHP

In order to make use of our installed PHP package, we need to do a couple of things:
* Edit the config file for `uhttpd`.
* Restart the server to update the configuration.
* Create a PHP script and put in where `uhttpd` can find it.
* Start making awesome things!


#### Editing the Configuration

We recommend you do the editing with Omega's built-int text editor - `vi`. The alternative is you can copy the file, edit it on your own computer, then copy it back.

If you have never used `vi`, know that it **does not** work like other text editors. We recommend you to brush up on the [basics](http://vim.wikia.com/wiki/New_to_Vim) before continuing. If you decide to forge on, remember this: hit `ESC` and type `:q!` to quit without saving!

Without further ado, let's get to configuring our PHP installation.

To use `vi` to edit, simply run the following:

```
vi /etc/config/uhttpd
```

You'll see something like this:

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

To let uhttpd know where our PHP is and what pages to send, add the following lines to the last line of that block of text:

```
        list interpreter ".php=/usr/bin/php-cgi"
        option index_page 'index.php'
```

Press `ESC` on keyboard, and then `:wq` & `Enter` to save changes. If you're editing this on your own computer, simply copy it back to `/etc/config/uhttpd` and make sure to overwrite it.

Every time the configuration is edited we need to restart the web server if we want the changes to take effect. We do this by running this command:

```
/etc/init.d/uhttpd restart
```

And that's it, the uhttpd server is now capable of parsing PHP files!


#### Testing the Installation

Create a test file & directory by executing the following command:

``` bash
mkdir /www/php
cd /www/php
vi index.php
```

And paste this code into the file & save:

```php
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
This example runs a very simple PHP app through the onion web interface enabling you to fiddle with the RGB LED, and a Relay Expansion. This example works best if you have a Relay Expansion and an Expansion Dock. The webpage should display properly regardless of your setup - it just might throw some errors your way when you try to interact with it.


#### Getting the Code

First, let's copy the code from GitHub. If you have git already installed on your Omega, simply run the following commands:

```bash
cd /www/php/
git clone https://github.com/ageeweb/php_onion
```

If you don't have git installed on your Omega, we'll copy it to a local directory. If you're using OSX or Linux, you can navigate to where you wish to store it, and call the `git clone` command as above:

```bash
git clone https://github.com/ageeweb/php_onion
```

Next, we'll copy the file to the `/www/php` directory.

If you're on Linux or OSX, navigate to the directory where you cloned the github code (wherever you put the `php_onion` folder), then run the following:

```bash
scp -r ./php_onion/ root@omega-ABCD.local:/www/php
```

#### Final Result

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
