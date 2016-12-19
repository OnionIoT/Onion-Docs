The One Wire protocol is a bus-based protocol that uses, as the name implied, one wire for data transmission. It's similar to I2C (link to lcd screen article) but it has a longer range and a lower data rate. It follows a master-slave architecture with each bus allowing for one master, the Omega in this case, and many slave devices. Every device type has it's own unique single-byte (eight bit) identifier, and each device has it's own unique 64-bit serial number that includes the device type byte as the Least Significant Byte.
// throw in an example of a single-byte in hex
// bonus points: throw in an image showing 64 bits (separated into bytes), and highlighting the lsb (can make this easily in excel)

// make sure to mention that it can be referred to as 1W, 1-Wire, etc.