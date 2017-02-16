#!/bin/sh

input=$1

pref1="$(echo $input | sed -e 's/^\(.\).*/\1/')"
pref2="$(echo $input | sed -e 's/^.\(.\).*/\1/')"
chr1="$(echo $input | sed -e 's/^..\(.\).*/\1/')"
chr2="$(echo $input | sed -e 's/^...\(.\).*/\1/')"
chr3="$(echo $input | sed -e 's/^....\(.\).*/\1/')"
chr4="$(echo $input | sed -e 's/^.....\(.\).*/\1/')"
# todo: add a check for chr5; if chr5 is not blank, exit (4 digits only)

if ! [[ "$pref1" == "0" && "$pref2" == "x" ]]; then
    echo "Please input a hex number in the following format: 0x12ab"
    exit
fi

mapDigit(){
    if [ "$1" == "0" ]; then
        echo "0 0 1 1 1 1 1 1"
    elif [ "$1" == "1" ]; then
        echo "0 0 0 0 0 1 1 0"
    elif [ "$1" == "2" ]; then
        echo "0 1 0 1 1 0 1 1"
    elif [ "$1" == "3" ]; then
        echo "0 1 0 0 1 1 1 1"
    elif [ "$1" == "4" ]; then
        echo "0 1 1 0 0 1 1 0"
    elif [ "$1" == "5" ]; then
        echo "0 1 1 0 1 1 0 1"
    elif [ "$1" == "6" ]; then
        echo "0 1 1 1 1 1 0 1"
    elif [ "$1" == "7" ]; then
        echo "0 0 0 0 0 1 1 1"
    elif [ "$1" == "8" ]; then
        echo "0 1 1 1 1 1 1 1"
    elif [ "$1" == "9" ]; then
        echo "0 1 1 0 1 1 1 1"
    elif [[ "$1" == "a" || "$1" == "A" ]]; then
        echo "0 1 1 1 0 1 1 1"
    elif [[ "$1" == "b" || "$1" == "B" ]]; then
        echo "0 1 1 1 1 1 0 0"
    elif [[ "$1" == "c" || "$1" == "C" ]]; then
        echo "0 1 0 1 1 0 0 0"
    elif [[ "$1" == "d" || "$1" == "D" ]]; then
        echo "0 1 0 1 1 1 1 0"
    elif [[ "$1" == "e" || "$1" == "E" ]]; then
        echo "1 0 0 1 1 1 1 0" # fix
    elif [[ "$1" == "f" || "$1" == "F" ]]; then
        echo "1 0 0 0 1 1 1 0" # fix
    else
        echo "Invalid hex digit $1."
        exit
    fi
}

dig1=$(mapDigit $chr1)
dig2=$(mapDigit $chr2)
dig3=$(mapDigit $chr3)
dig4=$(mapDigit $chr4)

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

# play around with this to see how the gpio#s correspond to the digits
while true; do

echo 0 >/sys/class/gpio/gpio0/value
setOneDig $dig3
echo 1 >/sys/class/gpio/gpio0/value

# enable the digit
echo 0 >/sys/class/gpio/gpio19/value
setOneDig $dig1
echo 1 >/sys/class/gpio/gpio19/value

echo 0 >/sys/class/gpio/gpio11/value
setOneDig $dig2
echo 1 >/sys/class/gpio/gpio11/value

echo 0 >/sys/class/gpio/gpio18/value
setOneDig $dig4
echo 1 >/sys/class/gpio/gpio18/value
done
