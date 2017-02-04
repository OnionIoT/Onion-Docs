import registerClass
from sevenSegDisplay import sevenSegment
import time
# sec = 0.001

sevenDisplay = sevenSegment(11,18,19,0)
sevenDisplay.setup()

#time.sleep(sec)
# binValue = "{0:08b}".format(0b00000001)
# self.shiftReg.outputBits(binValue)

#sevenDisplay.showDigitOne(2)

while 1:
	sevenDisplay.showDigitThree(2)
	#time.sleep(sec)
	sevenDisplay.showDigitTwo(1)
	#time.sleep(sec)
