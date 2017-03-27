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

def __main__():
    # if script was called with no arguments
    if len(sys.argv) == 1:
        print "Please input a hex string, eg. 0x12ab"
        return -1

    # if script was called with too many arguments
    elif len(sys.argv) > 2:
        print "Too many arguments. Please input only one hex number."
        return -1

    # read the hex string from the argument
    inputHexString = sys.argv[1]
    inputLen = len(inputHexString)
    while True:
        for i in range(inputLen):
        	sevenDisplay.showDigit(i,inputHexString[i])
