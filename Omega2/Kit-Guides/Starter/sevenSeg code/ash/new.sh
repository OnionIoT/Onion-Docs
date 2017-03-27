#!/bin/sh

zero="0 0 1 1 1 1 1 1"
one="0 0 0 0 0 1 1 0"
two="0 1 0 1 1 0 1 1"
three="0 1 0 0 1 1 1 1"
four="0 1 1 0 0 1 1 0"
five="0 1 1 0 1 1 0 1"
six="0 1 1 1 1 1 0 1"
seven="0 0 0 0 0 1 1 1"
eight="0 1 1 1 1 1 1 1"
nine="0 1 1 0 1 1 1 1"

a="0 1 1 1 0 1 1 1"
b="0 1 1 1 1 1 0 0"
c="1 0 0 1 1 1 0 0"
d="0 1 1 1 1 0 1 0"
e="1 0 0 1 1 1 1 0"
f="1 0 0 0 1 1 1 0"

# setup shift register pins
echo 1 >/sys/class/gpio/export # data
echo 3 >/sys/class/gpio/export # latch
echo 2 >/sys/class/gpio/export # clock

# setup digit pins
# all directions are from left
echo 11 >/sys/class/gpio/export # digit 1
echo 18 >/sys/class/gpio/export # digit 2
echo 19 >/sys/class/gpio/export # digit 3
echo 0 >/sys/class/gpio/export # digit 4

# set direction for the pins above (out/input)
echo out >/sys/class/gpio/gpio1/direction
echo out >/sys/class/gpio/gpio2/direction
echo out >/sys/class/gpio/gpio3/direction

echo out >/sys/class/gpio/gpio11/direction
echo out >/sys/class/gpio/gpio18/direction
echo out >/sys/class/gpio/gpio19/direction
echo out >/sys/class/gpio/gpio0/direction

# write out values from the SR's buffer to the outputs
latchSR (){
	echo 1 >/sys/class/gpio/gpio3/value
	echo 0 >/sys/class/gpio/gpio3/value
}

# pulse the SR clock and shift in one bit from the data line
pulseClock (){
	echo 1 >/sys/class/gpio/gpio2/value
	echo 0 >/sys/class/gpio/gpio2/value
}

# set one digit
setOneDig(){
	  	
	echo out >/sys/class/gpio/gpio1/direction

	for i in $1 $2 $3 $4 $5 $6 $7 $8
	do
		#echo  
		echo $i >/sys/class/gpio/gpio1/value
		pulseClock
	done

	latchSR
}

# turn off all the pins (enable pins are active LOW)
initDigPins (){
	echo 1 >/sys/class/gpio/gpio0/value
	echo 1 >/sys/class/gpio/gpio18/value
	echo 1 >/sys/class/gpio/gpio19/value
	echo 1 >/sys/class/gpio/gpio11/value
}

initDigPins

# sleep 1;

# write the number "3133" to the display
# play around with this to see how the gpio#s correspond to the digits
while true; do

echo 0 >/sys/class/gpio/gpio0/value
setOneDig $three
echo 1 >/sys/class/gpio/gpio0/value

# enable the digit
echo 0 >/sys/class/gpio/gpio19/value
setOneDig $one
echo 1 >/sys/class/gpio/gpio19/value

echo 0 >/sys/class/gpio/gpio11/value
setOneDig $two
echo 1 >/sys/class/gpio/gpio11/value

echo 0 >/sys/class/gpio/gpio18/value
setOneDig $four
echo 1 >/sys/class/gpio/gpio18/value
done
