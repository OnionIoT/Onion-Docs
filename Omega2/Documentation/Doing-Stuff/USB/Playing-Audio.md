## Playing Audio with USB Devices {#usb-playing-audio}

This article outlines the steps required to play audio on your Omega2 with any USB-based audio board or adapter.

### Install the Required Packages

We'll need some packages in order to play audio:

```
opkg update
opkg install alsa-utils alsa-lib
```

We've tested this with the following:

* `alsa-lib` - 1.0.28-1
* `alsa-utils` - 1.0.28-2



### Adjusting Volume

Should the audio output be too loud or quiet, we can adjust this using another utility, called alsamixer.

To start it, simply enter the name in the command line, like so:

```
alsamixer
```

![alsamixer](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/audio-alsamixer.jpg)


The `alsamixer` program controls some functions of the audio output, mainly volume.

This presents a more graphical view of the volume and information regarding the USB audio device. Using the arrow keys on your keyboard, select the volume column and adjust the volume higher or lower, dependent on your needs. Where possible, keep the volume level below 80–90% to avoid any distortion.



### Playing Audio

To play audio, we'll use the `aplay` utility. It is a command line program that uses the sound file header to automatically determine the sound file formats, the sampling rate, bit depth, etc. It can accept multiple sound files as arguments.

[Transfer an audio file to your Omega](#transferring-files), let's use the `/tmp` directory to hold it. Then play the music by using the following command:

```
cd /tmp
aplay <the name of music file>     // For example, I have this song called Imagine.wav
```

![aplay](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/audio-aplay.jpg)

Press Ctrl+c to stop the music.

With `aplay`, you can only play .wav audio files. Convert music files to .wav online: http://audio.online-convert.com/convert-to-wav



### Recording Audio

To record audio, we'll use `arecord`, a command-line sound file recorder for the ALSA  sound card driver. It supports several file formats and multiple sound cards with multiple devices.

To start recording:

```
arecord output.wav
```

You'll get a printout with something along these lines:

```
Recording WAVE '<name>.wav' : Unsigned 8 bit, Rate 8000 Hz, Mono.
```

Without any arguments, `arecord` will record microphone input to wav format with a sample rate of 8000 Hz, unsigned 8 bit depth, and single mono channel. It will continue to capture a stream of microphone input until it's terminated by Ctrl+C.

To play back a recorded wav file, you can use the `aplay` ALSA utility.

```
aplay <name>.wav
```

![arecord](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/audio-arecord.jpg)

For more options, run `arecord –h` for help.

#### Customizing the Recording

If you want, you can customize the output wav format as follows.

```
arecord -f cd <name>_stereo.wav
Recording WAVE '<name>.wav' : Signed 16 bit Little Endian, Rate 44100 Hz, Stereo
```

or

```
arecord -r 16000 -f S16_LE <name>.wav
Recording WAVE '<name>.wav' : Signed 16 bit Little Endian, Rate 16000 Hz, Mono
```
