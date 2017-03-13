
### Keypad


A keypad allows the user to press a button and the attached computer system will be able to tell which digit was pressed. If keypads were to use a pin for every button, there would be way too many data pins to connect! Instead, keypads only have pins for each horizontal row and pins for each vertical column. In our case we only need 7 (4 rows and 3 columns) instead of 15.

<!-- // TODO: IMAGE graphic of a keypad -->

// TODO: potentially reword the next paragraph for clarity
However, since the pins are not directly mapped to the buttons, our computer system will have to decode the signals coming from the keypad. When a button is pressed, the corresponding row and column pins will become logical high. Our code will have to define the location of each button based on its row and column intersection.