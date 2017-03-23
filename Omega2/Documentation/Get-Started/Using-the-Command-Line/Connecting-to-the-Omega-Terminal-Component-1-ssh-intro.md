SSH stands for **Secure Shell** . It's a network protocol that creates a secure channel for communication between two devices on the same network. It can be used to secure many different types of communication, but here we'll be using it to login to the Omega's command prompt.

<!-- //TODO: add stylized picture of the Omega2 and a laptop connected to a wifi network -->

#### The Good & Bad of SSH

When using SSH, the Omega and your computer communicate over the WiFi network to which they are both connected. This means that as long as the Omega is powered on and within range of your WiFi network, you can connect to it! No need to plug it directly into your computer.

The disadvantage of SSH is that if the network connection gets interrupted, the connection will also be severed.

For most use-cases with the Omega, SSH will work really well. This should be your go-to method for accessing the Omega's command-line.
