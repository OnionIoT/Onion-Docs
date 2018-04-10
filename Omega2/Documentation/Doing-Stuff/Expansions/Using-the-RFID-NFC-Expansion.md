## Using the RFID & NFC Expansion

The NFC & RFID Expansion brings contact-less RFID and NFC communication to the Omega ecosystem. It supports reading and writing with several NDC and RFID protocols at 13.56 MHz. The Expansion is based on the popular `PN532` NFC Chip and communicates with the Omega via `UART1`

### Installation

To use your RFID & NFC Expansion, you'll first need to initialize the the device:

```
opkg update
opkg install nfc-utils
```

`nfc-utils` contains the list of the utilities that will perorm certain operations. 

### Command Usage

Once `nfc-utils` has been installed, the following utilities have been initialized:

```
nfc-emulate-forum-tag4
nfc-jewel
nfc-list
nfc-mfclassic
nfc-mfultralight
nfc-read-forum-tag3
nfc-relay-picc
nfc-scan-device
```

These programs can be accessed from the command line and are used to control the RFID & NFC Expansion. For a print-out of the command’s usage, run it with only a '-h' argument.

#### Scanning the RFID/NFC Tag

To scan the RFID/NFC Tag, you can use the `nfc-list` utility. This tool is used to scan tags and print the result. Tap the tag onto Expansion and issue `nfc-list` command. For example, if you are scanning `Mifare Classic` card tag, it will print the following:

```
nfc-list uses libnfc reboot-3483-gd1bcad0
NFC device: pn532_uart:/dev/ttyS1 opened
1 ISO14443A passive target(s) found:
ISO/IEC 14443A (106 kbps) target:
    ATQA (SENS_RES): 00  04
       UID (NFCID1): c0  a8  f6  73
      SAK (SEL_RES): 08
```
`ATQA` and `SAK` indicate the manufacturer and tag type, and `UID` is the Unique Identification Number. You can compare your tags to the following table:
```
| Card Type         | ATQA  | SAK | UID Length |
|-------------------|-------|-----|------------|
| Mifare Classic 1K | 00 04 | 08  | 4 Bytes    |
| Mifare Classic 4K | 00 02 | 18  | 4 Bytes    |
| Mifare Ultralight | 00 44 | 00  | 7 Bytes    |
```
<!-- [official `ISO14443A` table](http://nfc-tools.org/index.php?title=ISO14443A) -->


#### Configuring Mifare Classic Type Cards

`nfc-mfclassic` Program is used to configure the `Mifare Classic` type cards. You can read from/write to the tag, wipe the card and modify the keys. Mifare Classic cards are loaded with EEPROM memory of 1K or 4K. Each card has its own UID, Block Check Character (BCC), Access Condition with two keys (A and B) and blocks of user data that can be configured with different access condition. Please see the chart below for characteristics of the cards:
```
|     Card Type     | # of Sectors | # of Blocs per Sector |
|:-----------------:|:------------:|:---------------------:|
| Mifare Classic 1K |      16      |           4           |
| Mifare Classic 4K |      32      |           4           |
```

Ther are several operations that can be done with this command:
* Scan the tag and store it to a binary file (`.mfd` format)
* Modify the user data and the key
* Write new binary file to the tag

##### Reading the Mifare Classic Tag

In order to scan the tag and store it to a file using key A, please run the following command:

```
nfc-mfclassic r a mycard.mfd
```
The card has been read and stored in a file called `mycard.mfd` using key `A`. Now, the `.mfd` binary file has been saved in your filesystem. This file is populated with a binary content that is difficult to understand. However, it is possible to convert it to a Hex format. You can apply [LEDE packages](https://docs.onion.io/omega2-docs/using-opkg.html#using-opkg-switch-to-lede-repos) to your Omega and install the utility called `xxd`:
```
opkg update
opkg install xxd
```
Uisng this utility you can view the content of your tag data using the following command:
```
xxd mycard.mfd
```
And you will be presented with the following:
```
00000000: 70e2 f773 1688 0400 0000 0000 0000 0000  p..s............
00000010: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000020: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000030: ffff ffff ffff ff07 8069 0000 0000 0000  .........i......
00000040: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000050: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000060: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000070: ffff ffff ffff ff07 8069 0000 0000 0000  .........i......
00000080: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000090: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000000a0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000000b0: ffff ffff ffff ff07 8069 0000 0000 0000  .........i......
...
```

The first 4 lines represent 1 Sector and each line in the sector - 1 block. The very first block of that file determines the UID and Manufacturer Data. In this case the `UID` of this card is `70e2f773`, `BCC` is `16`, `ATQA` is `8804` and the rest is the manufacturer data. Every sector has it's own Keys and Access points stored at the last block of each sector. See the representation below:

<!-- PICTURE HERE -->


##### Modifying the Tag

You can also modify the content of the stored tag. The process is as follows:

1. Convert the `.mfd` binary into `.hex` 
2. Edit the `.hex` file using any code editor (e.g vim, nano, etc)
3. Conver the `.hex` back to the `.mfd` file

The `xxd` utility could be used in order to convert the `.mfd` to `.hex`:
```
xxd mycard.mfd > mycard.hex
```
You can modify any User Data Block (2nd or 3rd block of each sector). Change bytes that you'd like to edit and save it. For example you can do the following:
```
Block 1: 0001 0203 0405 0607 0809 0a0b 0c0d 0e0f
```
Save your modified file and convert it back to the `.mfd` format using the following command:
```
xxd -r mycard.hex mycard.mfd
```

##### Writing to the Tag

Now, you can write the updated data back to the card, using key A:
```
# nfc-mfclassic w a newdata.mfd
NFC reader: pn532_uart:/dev/ttyS1 opened
Found MIFARE Classic card:
ISO/IEC 14443A (106 kbps) target:
    ATQA (SENS_RES): 00  04
       UID (NFCID1): 70  e2  f7  73
      SAK (SEL_RES): 08
Guessing size: seems to be a 1024-byte card
Writing 64 blocks |...............................................................|
Done, 63 of 64 blocks written.
```
Now the card contains updated data and could be used for different purpose.

#### Configuring Mifare Ultralight Type Cards

`nfc-mfultralight` program is used to configure the `Mifare Ultralight` type cards. You can read from the tag and write to it. Mifare Ultralight tags are loaded with EEPROM memory of 64 Bytes. Each card has its own UID, Internal Memory, One-Time Programmable Memory and blocks of user data. 

There are several operations that can be done with this program:
* Scan the tag and store it to a binary file (`.mfd` format)
* Modify the user data
* Write new binary file to the tag

In order to scan the tag and store it to a file, please run the following command:

```
nfc-mfultralight r mycardUltra.mfd
```
The card has been read and stored in a file called `mycardUltra.mfd`. Now, the `.mfd` binary file has been saved in your filesystem. This file is populated with a human-unreadible content. Now, uisng `xxd` utility you can view the content of your tag data using the following command:
```
xxd mycardUltra.mfd
```
And you will be presented with the following:

<!--- DIAGRAM BELOW
-->

#### nfc-scan-device

The `nfc-scan-device` is the utility to check whether the RFID/NFC device is presented. While your RFID/NFC Expansion is plugged to the dock, you can scan it and make sure that it is recongizable:
```
# nfc-scan-device
nfc-scan-device uses libnfc reboot-3483-gd1bcad0
1 NFC device(s) found:
- pn532_uart:/dev/ttyS1:
    pn532_uart:/dev/ttyS1
```

From this, you can see that the Expansion is up and running under `/dev/ttyS1`.

#### Troubleshooting Tips

Sometimes the issued `nfc` command could not finish its process and if you terminate it using `Ctrl + C` it will run on the background. If you try to perfomrm other nfc related operations you may face the following error:
```
error   libnfc.driver.pn532_uart        Serial port already claimed: /dev/ttyS1
nfc-mfultralight: ERROR: Error opening NFC device
```
That means that the RFID/NFC Expansion is still busy processing previous command. The `screen` utility will be used to stop it. Issue the following commands to install the `screen` utility and stop the background process:
```
opkg update
opkg install screen
screen /dev/ttyS1
```
You will be presented with the balck blank screen. To stop the process, hit `Ctrl + a + k` and at the following propmt `Really kill this wundow [y/n]` hit `y`. This will stop the process and will allow you to continue the expansion.


