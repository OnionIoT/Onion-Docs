from registerClass import shiftRegister
import signal

shiftRegister = shiftRegister(1,2,3) #Data pin is GPIO 1, serial clock pin is GPIO 2, Latch pin is GPIO 3

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

signal.signal(signal.SIGINT, signal_handler)


shiftRegister.setup()
value = 192
interrupted = False
while 1:

	for x in range(0, 12):
		binValue = "{0:08b}".format(value) # Transforms the value into a binary number (192 = 11000000)
		shiftRegister.outputBits(binValue) # Sends the 8 bit value to be output by the shift register
		if x < 6:
			value >>= 1 #Shifts the value right by one (11000000 -> 01100000)
		else:
			value <<= 1 #Shifts the value left by one (01100000 -> 11000000)
	if interrupted:
		shiftRegister.clear()
		break
