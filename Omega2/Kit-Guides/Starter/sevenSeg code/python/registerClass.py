import onionGpio
import time 
import os

class shiftRegister:
		#Initializes the GPIO objects based on the pin numbers
		def __init__(self, dataPin, serialClock, registerClock):
			self.ser = onionGpio.OnionGpio(dataPin)
			self.srclk = onionGpio.OnionGpio(serialClock)
			self.rclk = onionGpio.OnionGpio(registerClock)

		#Pulses the latchpin
		def latch(self):
			self.rclk.setValue(1)
			self.rclk.setValue(0)

		# Pulses the Serial Clock 8 times in and then latches to clear all the LEDs
		def clear(self):
			self.ser.setValue(0)
			for x in range(0, 8): #Clears out all the values currently in the register
				# self.srclk.setValue(1)
				# self.srclk.setValue(0)
				os.popen("gpioctl dirout-high 2").read()
				os.popen("gpioctl dirout-low 2").read()
			self.latch()

		#Sets the GPIOs to output with an initial value of zero
		def setup(self):
			self.ser.setOutputDirection(0)
			# self.srclk.setOutputDirection(0)
			os.popen("gpioctl dirout-low 2").read()
			self.rclk.setOutputDirection(0) 
			self.clear()

		#Sets the serial pin to the correct value and then pulses the serial clock to shift it in
		def inputBit(self, inputValue):
			self.ser.setValue(inputValue)
			# self.srclk.setValue(1)
			# self.srclk.setValue(0)
			os.popen("gpioctl dirout-high 2").read()
			os.popen("gpioctl dirout-low 2").read()
			# self.ser.setOutputDirection(inputValue)
			# self.srclk.setOutputDirection(1)
			# self.srclk.setOutputDirection(0)

		#Splits the input values into individual values and inputs them. The pulses the latch pin to show the output.
		def outputBits(self, inputValues):
			inputValues = str(inputValues)
			mylist = list(inputValues)
			for x in mylist:
				x = int(x)
				self.inputBit(x)
			self.latch()
