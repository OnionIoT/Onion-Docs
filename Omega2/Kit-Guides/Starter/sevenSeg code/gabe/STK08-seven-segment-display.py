import sys
from sevenSegDisplay import SevenSegDisplay


digitPins = [11, 18, 19, 0]
shiftRegPins = [1, 2, 3]

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
    
    sevenSeg = SevenSegDisplay(shiftRegPins, digitPins)
    sevenSeg.printHexNumber(inputHexString)
    
    while True:
        sevenSeg.refresh()

if __name__ == '__main__':
    __main__()