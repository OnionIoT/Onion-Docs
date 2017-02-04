import registerClass
import onionGpio
import time


class sevenSegment:
		#Initializes the GPIO objects based on the pin numbers
		def __init__(self, digitOne, digitTwo, digitThree, digitFour):
			self.shiftReg = registerClass.shiftRegister(1,2,3)
			self.digitOne = onionGpio.OnionGpio(digitOne)
			self.digitTwo = onionGpio.OnionGpio(digitTwo)
			self.digitThree = onionGpio.OnionGpio(digitThree)
			self.digitFour = onionGpio.OnionGpio(digitFour)


			self.a = "01110111"
			self.b = "00111110"
			self.c = "10011100"
			self.d = "01111010"
			self.e = "10011110"
			self.f = "10001110"
			self.zero = "00111111"
			self.one = "00000110"
			self.two = "01011011"
			self.three = "01001111"
			self.four = "01100110"
			self.five = "01101101"
			self.six = "01111101"
			self.seven = "00000111"
			self.eight = "01111111"
			self.nine = "01101111"


		def getCharacter(self, character):
			if character == 0:
				return self.zero
			elif character == 1:
				return self.one
			elif character == 2:
				return self.two
			elif character == 3:
				return self.three
			elif character == 4:
				return self.four
			elif character == 5:
				return self.five
			elif character == 6:
				return self.six
			elif character == 7:
				return self.seven
			elif character == 8:
				return self.eight
			elif character == 9:
				return self.nine


		# def sendZero(self):
		# 	self.shiftReg.outputBits(self.zero)
		# def sendOne(self):
		# 	self.shiftReg.outputBits(self.one)
		# def sendTwo(self):
		# 	self.shiftReg.outputBits(self.two)
		# def sendThree(self):
		# 	self.shiftReg.outputBits(self.three)
		# def sendFour(self):
		# 	self.shiftReg.outputBits(self.four)
		# def sendFive(self):
		# 	self.shiftReg.outputBits(self.five)
		# def sendSix(self):
		# 	self.shiftReg.outputBits(self.six)
		# def sendSeven(self):
		# 	self.shiftReg.outputBits(self.seven)
		# def sendEight(self):
		# 	self.shiftReg.outputBits(self.eight)
		# def sendNine(self):
		# 	self.shiftReg.outputBits(self.nine)


		def showDigitOne(self, character):
			self.digitOne.setValue(0)
			self.shiftReg.outputBits(self.getCharacter(character))
			self.digitOne.setValue(1)

		def showDigitTwo(self, character):
			self.digitTwo.setValue(0)
			self.shiftReg.outputBits(self.getCharacter(character))
			self.digitTwo.setValue(1)

		def showDigitThree(self, character):
			self.digitThree.setValue(0)
			self.shiftReg.outputBits(self.getCharacter(character))
			self.digitThree.setValue(1)

		def showDigitFour(self, character):
			self.digitFour.setValue(0)
			self.shiftReg.outputBits(self.getCharacter(character))
			self.digitFour.setValue(1)



		# def showAll(self):
		# 	while 1:
		# 		self.digitOne.setValue(0)
		# 		time.sleep(0.0005)
		# 		self.digitOne.setValue(1)
		# 		self.digitTwo.setValue(0)
		# 		time.sleep(0.0005)
		# 		self.digitTwo.setValue(1)
		# 		self.digitThree.setValue(0)
		# 		time.sleep(0.0005)
		# 		self.digitThree.setValue(1)
		# 		self.digitFour.setValue(0)
		# 		time.sleep(0.0005)
		# 		self.digitFour.setValue(1)


		def setup(self):
			# time.sleep(0.01)
			self.shiftReg.setup();
			self.digitOne.setOutputDirection(1)
			self.digitTwo.setOutputDirection(1)
			self.digitThree.setOutputDirection(1)
			self.digitFour.setOutputDirection(1)


		def clear(self):
			self.shiftReg.clear();
			self.digitOne.setOutputDirection(1)
			self.digitTwo.setOutputDirection(1)
			self.digitThree.setOutputDirection(1)
			self.digitFour.setOutputDirection(1)