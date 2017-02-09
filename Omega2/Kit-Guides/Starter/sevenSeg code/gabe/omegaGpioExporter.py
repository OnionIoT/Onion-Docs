import os
from subprocess import call

gpioPath = "/sys/class/gpio"
gpioExportPath = os.path.join(gpioPath, "export")

class OmegaGpioExporter:
    def __init__(self):
        pass
        
    def exportPin(pin):
        call(["echo", pin, ">" + gpioExportPath])
        
    def exportDirection(pin, direction):
        call(["echo", direction, ">" + os.path.join(gpioPath, "gpio" + str(pin), "direction"])
        
    def writeValue(pin, value):
        call(["echo", value, ">" + os.path.join(gpioPath, "gpio" + str(pin), "value"])
 
    def pulse(pin, direction):
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