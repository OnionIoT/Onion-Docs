from onionGpio import OnionGpio
from OmegaExpansion import relayExp

SWITCH_PIN = 0
RELAY_ID = 7

def main():
    switch = OnionGpio(SWITCH_PIN)
    
    relayStatus = relayExp.checkInit(RELAY_ID)

    if (relayStatus is False):
        print ("Relay checked,
        relayExp.driverInit(RELAY_ID)







