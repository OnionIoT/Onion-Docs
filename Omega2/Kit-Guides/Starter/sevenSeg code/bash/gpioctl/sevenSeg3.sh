#!/bin/bash
## declare an array variable
declare -a one=(0 0 0 0 0 1 1 0)
declare -a two=(0 1 0 1 1 0 1 1)

latchSR (){
	gpioctl dirout-high 3
	gpioctl dirout-low 3
}

pulseClock (){
	gpioctl dirout-high 2
	gpioctl dirout-low 2
}

# use for loop to read all values and indexes
setOneDig(){
	
	array=($@)
	for (( i=0; i<8; i++ ));
	do
	  ## echo $i " : " ${one[$i]}
	  if [ ${array[$i]} = 1 ]; then
	  	gpioctl dirout-high 1
	  else
	  	gpioctl dirout-low 1
	  fi
	  pulseClock
	done
	latchSR
}

initDigPins(){
	gpioctl dirout-high 11
	gpioctl dirout-high 18
	gpioctl dirout-high 19
	gpioctl dirout-high 0
}


initDigPins

while true; do
gpioctl dirout-low 11
setOneDig ${one[@]}
gpioctl dirout-high 11
gpioctl dirout-low 0
setOneDig ${two[@]}
gpioctl dirout-high 0
done
