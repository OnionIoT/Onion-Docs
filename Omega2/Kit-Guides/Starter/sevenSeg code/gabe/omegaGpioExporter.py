from os import path
from subprocess import call

gpioPath = "/sys/class/gpio"
gpioExportPath = path.join(gpioPath, "export")

class OmegaGpioExporter:
    def __init__(self):
        pass
        
    def exportPin(self, pin):
        filepath = path.join(gpioExportPath, "gpio" + str(pin))
        
        if not path.isdir(filepath):
            with open(gpioExportPath, "w") as export:
                export.write(str(pin) + "\n")
        
    def exportDirection(self, pin, direction):
        filepath = path.join(gpioPath, "gpio" + str(pin), "direction")
        
        if path.exists(filepath):
            with open(filepath, "w") as directionFile:
                directionFile.write(direction + "\n")
        
    def writeValue(self, pin, value):
        filepath = path.join(gpioPath, "gpio" + str(pin), "value")
        
        if path.exists(filepath):
            with open(filepath, "w") as valueFile:
                valueFile.write(str(value) + "\n")
 
    def pulse(self, pin, direction):
        if direction == 0:
            self.writeValue(pin, 1)
            self.writeValue(pin, 0)
            self.writeValue(pin, 1)
            return
        
        if direction == 1:
            self.writeValue(pin, 0)
            self.writeValue(pin, 1)
            self.writeValue(pin, 0)
            return