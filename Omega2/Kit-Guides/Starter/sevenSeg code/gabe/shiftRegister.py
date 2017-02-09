# shift register class
# writes directly to the Omega's filesystem for fast access
import os
import omegaGpioExporter


class ShiftRegister:
		# initializes the GPIO objects based on the pin numbers
		def __init__(self, dataPin, clockPin, registerPin):
			self.dataPin = dataPin
			self.clockPin = clockPin
			self.latchPin = registerPin
            
            self.driver = omegaGpioExporter.OmegaGpioExporter()
            # setup shift register pins
            self.setup()
        	
        # pulses the latchpin, writing values to outputs
		def latch(self):
			self.driver.pulse(self.latchPin, 1)
            
        def clock(self):
            self.driver.pulse(self.clockPin, 1)

		# Pulses the Serial Clock 8 times in and then latches to clear all the LEDs
		def clear(self):
            self.driver.exportValue(self.dataPin, 0)
			for x in range(8): #Clears out all the values currently in the register
				self.drive.pulse(self.clockPin, 1)

			self.latch()

		# sets the GPIOs to output with an initial value of zero
		def setup(self):
            # build an array of all the pins to export
            shiftRegisterPins = [self.dataPin, self.clockPin, self.registerPin]
            
            # export the shift register pins into the filesystem
            for pin in shiftRegisterPins:
                self.driver.exportPin(pin)
                self.driver.exportDirection(pin, "out"):

			self.clear()

		#Sets the serial pin to the correct value and then pulses the serial clock to shift it in
		def shiftOne(self, value):
			self.driver.writeValue(self.dataPin, value)
			self.driver.clock()
        
		#Splits the input values into individual values and inputs them. The pulses the latch pin to show the output.
		def writeBytestring(self, byte):
            # convert string as a list of values (MSB first)
			values = map(int, list(byte))
            
            # load them into the shift register
			for value in values:
				self.shiftOne(value)
			
            # write to outputs
            self.latch()
