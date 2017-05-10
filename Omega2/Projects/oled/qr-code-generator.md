## QR Code Generator {#qr-code-generator}

QR Codes are essentially two dimensional barcodes that can easily be scanned with any camera and a little bit of processing power. The average smartphone will make short work of any QR code it comes across.

![Onion QR Code](./img/qr-code-example.png)

In this tutorial, we'll go through how you can use Python to encode text into a QR Code and display it on your OLED Expansion:

![QR Code on OLED Exp](./img/oled-qr-code-photo.jpg)

The resulting code can then be scanned to read the encoded text. If it's a URL that's encoded, most smartphone QR code readers will open the browser to this URL. Useful if you have a complicated URL!

### Overview

**Skill Level:** Beginner

**Time Required:** 10 minutes

This project is mostly code based, all of the code can be found on this Onion GitHub Repo: https://github.com/OnionIoT/oledQrCodeGenerator

### Ingredients

* Onion [Omega2](https://onion.io/store/omega2/) or [Omega2+](https://onion.io/store/omega2p/)

* Any Onion Dock that supports Expansions: [Expansion Dock](https://onion.io/store/expansion-dock/), [Power Dock](https://onion.io/store/power-dock/), [Arduino Dock 2](https://onion.io/store/arduino-dock-r2/)
* Onion [OLED Expansion](https://onion.io/store/oled-expansion/)


### Step-by-Step

Ok, here we go! First we'll install some required packages to make everything run smoothly, and then we'll grab the code for this tutorial from GitHub.

#### 1. Prepare your Ingredients

You'll have to have an Omega2 ready to go, complete the [First Time Setup Guide](https://docs.onion.io/omega2-docs/first-time-setup.html) to connect your Omega to WiFi and update to the latest firmware.


#### 2. Installing Required Packages

We will need to have support for git, Python, and the [Onion OLED Expansion Python Module](https://wiki.onion.io/Documentation/Libraries/OLED-Expansion-Library). [Connect to the Omega's command line](https://docs.onion.io/omega2-docs/connecting-to-the-omega-terminal.html) and run the following command:

```
opkg update
opkg install python-light python-codecs pyOledExp git git-http ca-bundle
```



#### 3. Downloading the Code

Now we need to download the Python code from GitHub that actually does all the work. [Connect to the Omega's command line](https://docs.onion.io/omega2-docs/connecting-to-the-omega-terminal.html) and [clone the project repo from GitHub](https://docs.onion.io/omega2-docs/installing-and-using-git.html) with the following command:

```
cd /root
git clone https://github.com/OnionIoT/oledQrCodeGenerator.git
```


#### 4. Running the Code

Finally, we get to make some QR codes!
Navigate into the repo directory:

```
cd oledQrCodeGenerator
```

And run the program, the argument to the script is the text that will be encoded in the QR code pattern:

```
root@Omega-18C2:~/oledQrCodeGenerator# python main.py 'Wow, my first QR Code'
> Encoding 21 characters
> Generated QR Code: 31x31 pixels
> Doubled QR Code size: 62x62
> Initializing display
> Setting display mode to inverted
> Writing buffer data to display
```

This will encode the data and display the resulting QR code on the OLED Expansion:

![QR Code on OLED Exp](./img/oled-qr-code-photo.jpg)



##### Program Details

Behind the scenes, the Python code does the following:

* Encodes the input text into a matrix representing the QR Code
	* The size of the QR code is based on the amount of input text
* Converts the QR code matrix into data that can be displayed on the OLED
* Displays the resulting image on the OLED display
	* Performs display initialization
	* Inverts the display colors
	* Displays the generated image file

An additional feature was added for easier scanning: if the QR code is small (less than half the height of the OLED display), the image will be doubled in size so that each QR code pixel shows up as four pixels on the OLED display.

The default generated QR code will be a Version 3 code with the Low error correction setting and a one-pixel border, creating a code that is 31x31 pixels. If the amount of text to be encoded cannot fit in a Version 3 code, the program will select the next version that will fit the amount of data to be encoded. Check out the [Wikipedia entry on QR Codes](https://en.wikipedia.org/wiki/QR_code) for more details on QR code versions.




#### 5. Using the code as a Python Module (Optional)

The `oledQrCodeGenerator` code can also be imported as a module into your own Python projects!

The `dispQrCode()` function will perform the same actions described above.


**Example Code**

A small example showing how to use this module:
``` python
import sys
sys.path.append("/root")
import oledQrCodeGenerator

print 'Now using the oledQrCodeGenerator'
oledQrCodeGenerator.dispQrCode('Hello!')

print 'All done!'
```

> Note that the above code assumes the project code can be found at `/root/oledQrCodeGenerator`. It appends `/root` to the `sys.path` list that Python uses when looking for modules that need to be imported. If the `sys.path.append("/root")` line is not present, Python will return an error saying `ImportError: No module named oledQrCodeGenerator` since it cannot find the module in the usual places it looks.


### Reading QR Codes

It's no fun to just display QR codes and not be able to read them, right?

Don't worry, your smartphone is perfectly capable of reading the code from the OLED:

* On Android, we've used the [QR Code Reader](https://play.google.com/store/apps/details?id=tw.mobileapp.qrcode.banner) and [QR Barcode Scanner](https://play.google.com/store/apps/details?id=appinventor.ai_progetto2003.SCAN&hl=en) apps successfully
* On iOS, we've had success with the [QR Reader App](https://itunes.apple.com/us/app/qr-code-reader-and-scanner/id388175979?mt=8)

For QR codes that encode a lot of text, your phone might take a little while longer to scan the code. Trial and error works best in this scenario: try moving your phone to different distances and angles from the OLED.




### Acknowledgements

The code in the `qrcode` directory is a stripped-down version of lincolnloop's `python-qrcode` repo:
https://github.com/lincolnloop/python-qrcode
