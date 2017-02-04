#!/bin/bash

declare -a one=(0 0 0 0 0 1 1 0)
declare -a two=(0 1 0 1 1 0 1 1)

latchSR (){
	fast-gpio set 3 1

	fast-gpio set 3 0
}

pulseClock (){
	fast-gpio set 2 1

	fast-gpio set 2 0
}

# use for loop to read all values and indexes
setOneDig(){
	
	array=($@)
	for (( i=7; i>-1; i-- ));
	do
	  echo $i " : " ${one[$i]}
	  if [ ${array[$i]} = 1 ]; then
	  	fast-gpio set 1 1
	  else
	  	fast-gpio set 1 0
	  fi
	  pulseClock
	done
	latchSR
}

initDigPins(){
	fast-gpio set 11 1
	fast-gpio set 18 1
	fast-gpio set 19 1
	fast-gpio set 0 1
}


initDigPins                                  
                                             
while true; do                               
fast-gpio set 11 0                  
setOneDig ${one[@]}                    
fast-gpio set 11 1                
fast-gpio set 0 0                  
setOneDig ${two[@]}                    
fast-gpio set 0 1                  
done
