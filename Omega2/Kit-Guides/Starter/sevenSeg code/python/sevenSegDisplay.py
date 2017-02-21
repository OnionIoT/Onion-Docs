import registerClass
import onionGpio
import time

class sevenSegment:
    digitMap = {
    "0": "00111111",
    "1": "00000110",
    "2": "01011011",
    "3": "01001111",
    "4": "01100110",
    "5": "01101101",
    "6": "01111101",
    "7": "00000111",
    "8": "01111111",
    "9": "01101111",
    "a": "01110111",
    "b": "01111100",
    "c": "10011100",
    "d": "01111010",
    "e": "10011110",
    "f": "10001110",
    "off": "00000000",
    "-": "01000000"
    }

	#Initializes the GPIO objects based on the pin numbers
	def __init__(self, dPin):
		self.shiftReg = registerClass.shiftRegister(1,2,3)
        for i in range (0,4):
    		self.digitPin[i] = onionGpio.OnionGpio(dPin[i])
    		self.digitPin[i].setOutputDirection(1)


	def showDigit(self, d, character):
		self.digitPin[d].setValue(0)
		self.shiftReg.outputBits(self.digitMap[character])
		self.digit[d].setValue(1)


	def clear(self):
		self.shiftReg.clear();
        for i in range (0,4):
    		self.digitPin[i] = onionGpio.OnionGpio(dPin[i])
