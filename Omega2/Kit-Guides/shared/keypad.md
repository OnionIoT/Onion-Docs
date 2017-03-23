
### Keypad


A keypad allows the user to press a button and the attached computer system will be able to tell which digit was pressed. If keypads were to use a pin for every button, there would be way too many data pins to connect! Instead, keypads only have pins for each horizontal row and pins for each vertical column. In our case we only need 7 (4 rows and 3 columns) instead of 15.

<!-- // DONE: IMAGE graphic of a keypad -->
![12-button keypad](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/shared-keypad.jpg)

<!-- // DONE: potentially reword the next paragraph for clarity -->
However, since the pins are not directly mapped to the buttons, our computer system will have to decode the signals coming from the keypad. When a button is pressed, the corresponding row and column pins will become logical high. So we will have to translate the row and column signal into the value of the button just like how chess positions are recorded.
