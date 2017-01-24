## The Command Line Interface {#the-command-line-interface}

At this point we expect readers should have setup the Omega. If not, follow our [Getting Started Guide](#first-time-setup)

#### What is the Command Line Interface?

The command line interface (CLI) is the user's access point into the operating system using a terminal. All user interaction is interpreted and executed by the OS through things called  commands. A user enters a command into a terminal to make something happen.

Additionally, commands can accept options that tell the command to do specific things related to that command. Users can select options by typing the command followed by the option into the terminal.

We will now explore some basic Linux commands. Go ahead and login to your Omega, and you should see something like this:

![Opening_Screen](http://i.imgur.com/tRPQy5O.png)

#### Some Basic Commands

Let's go ahead try some basic commands:

```
login
```

This allows the user to login into the Linux as the root, which we will elaborate on further in this section/article.

Type login into the command line and press enter. You will be prompted to enter the username and password, which are "root" and "onioneer" respectively by default. Also note that the password will be hidden while you type. After that you should see a screen like this:

![Login_Screen](http://i.imgur.com/hxuce5c.png)

Congratulations! You have just executed your first command, you are now logged in as `root`.

**Information:**

If you are not used to work with the terminal, you might be happy to get some additional information what you can do within this "**Black-Box**".

To get more info about what commands you can use, just type:

```
busybox --help
```

and you will get a overview of what busy-box is and all commands available over it.

```
busybox --list
```

if you prefer a list of all this commands.

If you need more explanation about a certain command just use:

```
busybox ifconfig --help
```

Now let's try the `date` command:

```
date
```

This will return the date and time. Type `date` on the terminal and press Enter. You should see something like this.

![Date_Screen](http://i.imgur.com/qSmPt1Q.png)

As you can see, the command returned the current date and time(may be incorrect, but can be fixed) on the terminal.

```
echo
```

For the programmers out there, this is analogous to a print function. For example, typing `echo` "hello" will display "hello" in the command line. Go ahead and type `echo hello` into the command line. You should see this.

![Echo_Screen](http://i.imgur.com/dtD91g3.png)

`echo` can also be used to pass an input into another command but we'll elaborate on that more in the [Redirection Guide](#redirection).

We will now explore the [Filesystem on the Omega](#exploring-the-file-system).
