## Using DHT11/DHT22 Sensors with the Onion Omega

In this tutorial you'll be reading the temperature & humidity from a DHT sensor using both the console **and** also using PHP.

Let's get started!

### Installing the Sensor Library

Firstly you'll need to download the files for the DHT library that has been compiled for the Omega, to do this in your console run these commands:

```
opkg update
opkg install wget
cd /root
wget https://community.onion.io/uploads/files/1450434316215-checkhumidity.tar.gz
tar -zxvf 1450434316215-checkhumidity.tar.gz
```

Now for us to be able to use the "./checkHumidity" command, we need to make the file executable, so to do this we run this command:

```
chmod -R 755 /root/checkHumidity/bin/checkHumidity
```

We now need to sort a few pins out now.

### Hooking Up the Sensor

DHT11 & DHT22 have the same pin layouts, pin 1 is Vcc, pin 2 is the data pin and pin 4 is GND as shown in the image below:

![DHT Pinout](http://domoticx.com/wp-content/uploads/DHT11-Pinout.png "DHT Pinout")

Connect pin 1 to 5V, connect pin 2 to any spare GPIO pin, in this example we'll be using 20 and connect pin 4 to GND.

**Note:** 3.3V can give unrelaible results, use the 5V pin for Vcc

![DHT Example](https://community.onion.io/uploads/files/1454459150467-img_3184.jpg "DHT Example")


### Test Out the Sensor

For this example I'm using GPIO pin 20 and a DHT11 sensor, if you used a different pin or a DHT22 sensor, change the values as appropriate.

On your command line run the following:

```
cd /root/checkHumidity/bin/
./checkHumidity 20 DHT11
```

You'll now be presented back with the following result:

```
root@Omega-NNNN:~/checkHumidity/bin# ./checkHumidity 20 DHT11
67.000000
22.000000
```

**Note:** If you see 255.00000 values here, check the wiring!

### Making it Work with PHP

This example requires PHP to be installed and setup on your Omega. If it's not, we've provided [a tutorial](#installing-and-using-php) to do just that.

Once PHP is up and running, it's easy as copy & paste, let's go!

On the command line run these commands:

```
cd /www/php
vi dht.php
```

In the editor, paste in this code (look up `paste mode` in vi to keep the formatting):

```
<?php
$result 	= get_dht_values(20, "DHT11");	// change the pin number and DHT type accordingly
$message 	= $result[0];
$temp 		= $result[1];
$humidity 	= $result[2];

if( $message == "success" ) {
	// if successful, happy days let's spill the data out
	echo "<p>The current temperature is <b>" . $temp . "&deg;C</b> and the humidity is . <b>" . $humidity . "%</b>" ;
} else {
	echo "Error: " .  $message;
}

function get_dht_values($pin, $dht_type) {

	if( ( $dht_type != "DHT11" ) && ( $dht_type != "DHT11" )  ) {
		return array("Invalid DHT Type", 0, 0);
	}

	// Run the command using the exec() function, delivers the output in $output
	exec("/root/checkHumidity/bin/checkHumidity $pin $dht_type  2>&1", $output, $return);

	// -255 = bad
	if( $output[0] == "-255.000000" ) {
		return array("Unable to read sensor, check the wiring, pin number!", 0, 0);
	}

	// must be all good, lets return the data
	$output[0]	 =  number_format( (float)$output[0], 2, '.', '' );	// temp
	$output[1]	 =  number_format( (float)$output[1], 2, '.', '' );	// hum
	return array( "success", $output[0], $output[1] );
}
```

Save and quit, now go to your web browser and type in this URL:

```
http://omega-ABCD.local/php/dht.php
```

If all goes well, you should se something like this:

> The current temperature is **66.00°C** and the humidity is . **23.00%**


### What next?

That's up to you!

You can turn your Omega into a weather station, post the data to [https://thingspeak.com/](https://thingspeak.com/) and keep track of your Omega over time.
