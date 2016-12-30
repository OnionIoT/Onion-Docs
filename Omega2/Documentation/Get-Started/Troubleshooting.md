
## Troubleshooting {#first-time-troubleshooting}

### My Omega won't fit into the Dock!

Sometimes the Omega's pins aren't at a perfect 90˚ angle. Don't be afraid to press on them a little to get them to the correct angle, they're tougher than you think!

If they need to be bent inwards a little, try putting the pins up against a flat surface at 45˚ and pushing a little.

<!-- TODO: IMAGE OF THIS ACTION -->

If the pins need to be bent outward, put the pins up against a flat surface near the edge at 45˚ the other way and pushing a little.

<!-- TODO: IMAGE OF THIS ACTION -->

### My Omega won't connect to my WiFi Network

Make sure your password has been typed in correctly, remember, WiFi passwords are case sensitive.

### My Omega still won't connect to my WiFi Network and I've made sure my WiFi password is correct

It's possible that the your WiFi network and the Omega's AP network are *colliding*.
This happens if your WiFi network uses the same *IP address network prefix* as the Omega's AP, `192.168.3.0/24`. Follow our guide for [fixing IP address collisions](#fix-ip-addr-collisions).


### My Omega doesn't reboot after installing the update, it just turns off

Some Omega2+ models may not reboot automatically with the factory firmware. If your Omega's LED turns off and remains off for 15 seconds or more at the end of the firmware update, you will need to manually reboot it.

To manually reboot your Omega, briefly disconnect the power and reconnect it. This can also be accomplished by toggling the power switch on the Expansion, Mini, or Power Dock. Your Omega will then boot and complete the update. It will be ready for use when the LED stops flashing and remains solid.
