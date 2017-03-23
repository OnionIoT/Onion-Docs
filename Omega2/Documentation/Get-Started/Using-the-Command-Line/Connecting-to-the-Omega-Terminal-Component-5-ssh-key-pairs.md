Over the course of a few months, the number of times you type in the password to connect will add up to a whole bunch of time that could have been spent having fun. Don't worry, there's another way to authenticate your SSH connection: **SSH Key Pairs**.

By using SSH Key Pairs, **the Omega and your computer will do a secure handshake so you won't need to type in that pesky password all the time**. Not only that, using a key pair will make your Omega even more since passwords can be discovered but secure key pair authentication cannot be broken.

#### What are Key Pairs?

Good question! Authentication using a Key Pairs is based on having two randomly generated binary keys, where one is **public** and one is **private**.

* The private key is like a handwritten signature, used to prove your identity, so **make sure to keep it secret and keep it safe!**
* The public key's only purpose is to verify your identity, and is meant to be shared with other devices.

An SSH connection to your Omega that's secured by with a key pair will look something like this:

- Your computer will ask to login to the Omega, and the Omega will respond with 'Ok, but first prove your identity'
- Your computer will then generate a hash using your private key and send it to the Omega
- The Omega will use the stored public key to try to decode the identity hash, if the Public Key matches the Private Key, the decode will be successful, and the Omega will allow the connection to proceed.

#### Adding your Public Key

The method will be different depending on what Operating System you're using on the computer used to connect. We've included guides for the following:

* [Mac OS X](#ssh-add-public-key-mac)
* [Linux](#ssh-add-public-key-linux)
* [Windows](#ssh-add-public-key-windows)

#### How to Add your Public Key to the Omega on a MAC {#ssh-add-public-key-mac}


**Step 1: Locating Existing Key Pair**

Let's first check to see if your computer already has a key pair. Open the Terminal App on your Mac and run:

```

ls ~/.ssh/id_rsa.pub

```

If this file exists, skip ahead to Step 3.

<!-- // TODO: add screenshot of terminal showing file exists -->

**Step 2: Generating a Key Pair**

No worries if you don't have a key yet, follow this [quick guide](https://help.github.com/articles/generating-an-ssh-key/#platform-mac) to generate a key pair.

**Step 3: Copy Key Pair**

Copy the contents of the public key file to the clipboard:

```
cat ~/.ssh/id_rsa.pub
```

**Step 4: Create an Authorized Keys File**

Connect to your Omega's command prompt and create a new file:

```
vi /etc/dropbear/authorized_keys
```

And paste your public key into it.

**And you're done!**

From now on, you'll be able to securely connect to your Omega without having to type out a password every time.


#### How to Add your Public Key to the Omega on a Linux machine {#ssh-add-public-key-linux}

**Step 1: Locating Existing Key Pair**

Let's first check to see if your computer already has a key pair. Open the Terminal App on your Mac and run:

```
ls ~/.ssh/id_rsa.pub
```

If this file exists, skip ahead to Step 3.

<!-- // TODO: add screenshot of terminal showing file exists -->

**Step 2: Generating a Key Pair**

No worries if you don't have a key yet, follow this [quick guide](https://help.github.com/articles/generating-an-ssh-key/#platform-linux) to generate a key pair.

**Step 3: Copy Key Pair**

Copy the contents of the public key file to the clipboard:

```
cat ~/.ssh/id_rsa.pub
```

**Step 4: Create an Authorized Keys File**

Connect to your Omega's command prompt and create a new file:

```
vi /etc/dropbear/authorized_keys
```

And paste your public key into it.

**And you're done!**

From now on, you'll be able to securely connect to your Omega without having to type out a password every time!

#### How to Add your Public Key to the Omega on a Windows machine {#ssh-add-public-key-windows}

**Step 1: Locating Existing Key Pair**

Let's first check to see if your computer already has a key pair. Open the Windows Explorer and enter the following as the address:

```
%HOMEDRIVE%%HOMEPATH%\.ssh\id_rsa.pub
```

If this file exists, skip ahead to Step 3.

**Step 2: Generating a Key Pair**

No worries if you don't have a key yet, follow this [quick guide](https://help.github.com/articles/generating-an-ssh-key/#platform-windows) to generate a key pair.

**Step 3: Copy Key Pair**

Open the public key file with a text editor (Notepad works fine) and copy the contents to the clipboard


**Step 4: Create an Authorized Keys File**

Connect to your Omega's command prompt and create a new file:

```
vi /etc/dropbear/authorized_keys
```

And paste your public key into it.

**And you're done!**

From now on, you'll be able to securely connect to your Omega without having to type out a password every time.
