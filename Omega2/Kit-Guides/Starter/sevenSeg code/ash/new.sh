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

echo 1 >/sys/class/gpio/export 
echo 3 >/sys/class/gpio/export 
echo 2 >/sys/class/gpio/export 

echo 11 >/sys/class/gpio/export 
echo 18 >/sys/class/gpio/export 
echo 19 >/sys/class/gpio/export 

echo 0 >/sys/class/gpio/export 

echo out >/sys/class/gpio/gpio1/direction
echo out >/sys/class/gpio/gpio2/direction
echo out >/sys/class/gpio/gpio3/direction

echo out >/sys/class/gpio/gpio11/direction
echo out >/sys/class/gpio/gpio18/direction
echo out >/sys/class/gpio/gpio19/direction
echo out >/sys/class/gpio/gpio0/direction

latchSR (){
	echo 1 >/sys/class/gpio/gpio3/value
	echo 0 >/sys/class/gpio/gpio3/value
}

pulseClock (){
	echo 1 >/sys/class/gpio/gpio2/value
	echo 0 >/sys/class/gpio/gpio2/value
}

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


initDigPins (){
	echo 1 >/sys/class/gpio/gpio0/value
	echo 1 >/sys/class/gpio/gpio18/value
	echo 1 >/sys/class/gpio/gpio19/value
	echo 1 >/sys/class/gpio/gpio11/value
}

initDigPins

# sleep 1;

while true; do

echo 0 >/sys/class/gpio/gpio0/value
setOneDig $one
echo 1 >/sys/class/gpio/gpio0/value

echo 0 >/sys/class/gpio/gpio18/value
setOneDig $three
echo 1 >/sys/class/gpio/gpio18/value

echo 0 >/sys/class/gpio/gpio19/value
setOneDig $three
echo 1 >/sys/class/gpio/gpio19/value

echo 0 >/sys/class/gpio/gpio11/value
setOneDig $three
echo 1 >/sys/class/gpio/gpio11/value
done
