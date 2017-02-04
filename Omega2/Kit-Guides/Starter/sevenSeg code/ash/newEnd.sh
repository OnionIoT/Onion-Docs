#!/bin/sh

echo 1 >/sys/class/gpio/unexport
echo 2 >/sys/class/gpio/unexport 
echo 3 >/sys/class/gpio/unexport 

echo 11 >/sys/class/gpio/unexport
echo 18 >/sys/class/gpio/unexport 
echo 19 >/sys/class/gpio/unexport
echo 0 >/sys/class/gpio/unexport 