### Onion Omega with PHP & PushBullet

Pushbullet is tool for receiving & sending messages, files etc... across platforms.

For example you can send a message aka "note" via your Onion Omega and then the note appears on all your connected devices, eg on your phone, iPad and even in your web browser. It's a bridge between them all!

![PHP & PushBullet Onion Omega Example](https://dl.dropboxusercontent.com/u/12816733/onion-omega-php-pushbullet-example-1.png)

### Possible Uses
What you could do with this is really up to you, here are a couple of ideas:

1. Someone at the door? Use a PIR sensor hooked up to the Onion Omega and when triggered you'll receive a notification on your devices
2. The alarm has gone off, alerts are now everywhere, even if you're abroad
3. Hook it up to IFTTT and create your own custom recipes
4. Oh and someone at the door again? Push a file, which just so happens is a jpg image from a connected USB Webcam to all the devices and unlock the door via a message back or a custom app in the Onion Omega dashboard

This simple example is using PHP, but you can easily do the same with any other programming language as it's just a POST request.

### Setup and Installation  

Before we start, there's some prerequisites to make everything work:

1. You'll need a [pushbullet](https://www.pushbullet.com/) account (free!) and the app installed on one or more devices
2. After that, you'll need a pushbullet API key, you can get this by going to [https://www.pushbullet.com/#settings/account](https://www.pushbullet.com/#settings/account), under "Access Tokens" hit "Create Access Token". Copy this key, you'll need it shortly. Don't let anyone else get access to it though, they'll be able to access your devices through this key!


#### Installing PHP & PHP cURL

If you don't have PHP installed, we've written a [guide](#installing-and-using-php) to get you up to speed.

On top of PHP, you'll need one additional library called "php5-mod-curl". You can install this by running these commands in your Onion Omega console:

```
opkg update
opkg install php5-mod-curl
```

Now restart uhttpd by running:

```
/etc/init.d/uhttpd restart
```

Go to your php folder and create a new file:

```
cd /www/php
vi pushbullet.php
```

Then paste in the code below (look up 'paste mode' in vi to keep the formatting), changing the placeholder to your auth token you got from step 1:

```
<?php
$authToken = "your auth token here!!!";

$curl = curl_init('https://api.pushbullet.com/v2/pushes');
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
curl_setopt($curl, CURLOPT_POST, true);
curl_setopt($curl, CURLOPT_HTTPHEADER, ["Authorization: Bearer $authToken"]);
curl_setopt($curl, CURLOPT_POSTFIELDS, [
		"type" => "note",
		"title" => "Pushbullet Notification",
		"body" => "Howdy, this is a message sent from my from My Onion Omega!"]
		);

$response = curl_exec($curl);
echo "<pre>";
print_r($response);
echo "</pre>";
```

Save the file by hitting `esc` then entering: `:wq`.

Now open your web browser and go to `http://omega-ABCD.local/php/pushbullet.php`

Ta da!!

<!-- TODO: IMAGE upload this to github -->

![PHP & PushBullet Onion Omega Example](https://dl.dropboxusercontent.com/u/12816733/onion-omega-php-pushbullet-example-1.png)

### What's next?

The world is your oyster. How about trying one of the dedicated PHP libraries for Pushbullet to make development faster?

1. [Pushbullet for PHP](https://github.com/ivkos/Pushbullet-for-PHP)
2. [phpushbullet](https://github.com/joetannenbaum/phpushbullet)
