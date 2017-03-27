from shiftRegister import ShiftRegister
import omegaGpioExporter
import string

class SevenSegDisplay:
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
    
    def __init__(self, shiftRegPins, digitPins):
        # requires shiftRegister pins in the following order:
        # [dataPin, clockPin, latchPin]
        self.shiftReg = ShiftRegister(shiftRegPins[0], shiftRegPins[1], shiftRegPins[2])
        self.digitPins = digitPins
        self.gpioDriver = omegaGpioExporter.OmegaGpioExporter()
        
        self.digitOn = 0
        self.digitOff = 1
        
        self.digits = ["off", "off", "off", "off"]
        
        # digitPins are in L-R order
        for i in range(4):
            self.gpioDriver.exportPin(self.digitPins[i])
            self.gpioDriver.exportDirection(self.digitPins[i], "out")
            
        self.clear()
        
    def allDash(self):
        self.setDigits("----")
    
    def clear(self):
        self.digits = ["off", "off", "off", "off"]
        self.refresh()        
    
    def setDigit(self, character, digit):
        if (digit < 1) or (digit > 4):
            print "Digit out of range."
            return -1
            
        self.digits[digit-1] = character
        
    def setDigits(self, string):
        if len(string) > 4:
            print "String too long, cannot print!"
            return -1
        
        characters = list(string)
        for i in range(4):
            self.setDigit(characters[i], i+1)
        
        self.refresh()
    
    def printHexNumber(self, hexString):
        hexList = list(hexString)
        
        if (hexList[0] is not "0") or (hexList[1] is not "x"):
            print "Please input a 4-digit hex string beginning with '0x', such as 0x12ab."
            return -1
        
        hexNum = list(hexString.split("x")[1])
        numDigits = len(hexNum)
        
        if numDigits > 4:
            print "Hex number is too long!"
            return -1
        
        elif numDigits == 0:
            print "You forgot the number part of the hex string!"
            return -1
            
        # hex numbers shorter than 4 digits will be printed on the right side
        blankDigits = 4 - numDigits
        
        for i in range(blankDigits):
            self.setDigit("off", i+1)
        
        for i in range(numDigits):
            character = hexNum[i]
            
            if character.isalpha:
                character = character.lower()
                
            if character not in SevenSegDisplay.digitMap:
                print "Invalid number!"
                return -1
            
            self.setDigit(character, i + blankDigits)
        
    
    def refresh(self):
        for i in range(4):
            # write out the current digit to the shift register
            self.shiftReg.writeBytestring(SevenSegDisplay.digitMap.get(self.digits[i], "-"))
            # turn off the previous digit            
            self.gpioDriver.writeValue(self.digitPins[i], self.digitOff)               
            # turn on the current digit
            self.gpioDriver.writeValue(self.digitPins[i+1], self.digitOn)
            
            