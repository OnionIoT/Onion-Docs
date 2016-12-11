
## Fix Network IP Address Collisions {#fix-ip-addr-collisions}

If you've been unsuccessful in connecting your Omega to your home WiFi network and you've made sure that the password is 100% correct, you might have an *IP address collision* between your WiFi network and the Omega's AP network.


### What is an IP Address Collision?

// ip address collision - if both the wifi network and the Omega's AP have the same `192.168.3.0/24` subnet/ip address network prefix, the Omega won't know what to send where
// TODO: insert a link to a page describing ip address prefixes and subnets

#### Identifying your WiFi Network's IP Address Prefix

// need to reconnect your computer to your wifi network and then find your IP address, if it's  `192.168.3.X`, then you have a collision
// link to articles showing how to find a computer's ip address in windows, os x, and linux

### Fixing the Collision

// two ways to fix the collision:
// 1: change the Omega's AP network prefix (easier)
// 2: change your router's network prefix (mention this but say we're not gonna cover this)

// show steps on connecting to the command line, using uci to change the ip address to 192.168.<WHATEVER>.1, restarting the network service, and trying to connect to your wifi network again
