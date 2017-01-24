## The Command Line Interface {#the-command-line-interface}





At this point we expect readers should have setup the Omega. If not the getting started guide can be found [here](https://wiki.onion.io/get-started).



#### What is the Command Line Interface?



The command line interface (CLI) is the user's access point into the operating system using a terminal. All user interaction is interpreted and executed by the OS through things called  commands. A user enters a command into a terminal to make something happen.



Additionally, commands come with  options that tell the command to do specific things related to that command. Users can select options by typing the command followed by the option into the terminal.

We will now explore some basic linux commands. Go ahead and connect your the Omega as in the getting started [guide](https://wiki.onion.io/get-started). You shoud see a screen like this:

![Opening_Screen](http://i.imgur.com/tRPQy5O.png)

#### Some Basic Commands


Let's go ahead try some basic commands:

```
login
```


This allows the user to login into the Linux as the root, which we will elaborate on further in this section/article.



Type login into the command line and press enter. You will be prompted to enter the username and password, which are "root" and "onioneer" respectively by default. Also note that the password will be hidden while you type. After that you should see a screen like this:






![Login_Screen](http://i.imgur.com/hxuce5c.png)



Congratulations! You have just executed your first command, you are now logged in as root.

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

busybox ifconfig --help

Let's see the next command:

<pre><code>date</code></pre>



The _date_ command will return the date and time.



Type _date_ on the terminal and press enter. You should see something like this.



Date Screen:




![Date_Screen](http://i.imgur.com/qSmPt1Q.png)



As you can see, the command returned the current date and time(may be incorrect, but can be fixed) on the terminal.



<pre><code>echo</code></pre>



For the programmers, this is analogous to a print function. For example, typing _echo_ "hello" will display "hello" in the command line. Go ahead and type "_echo_ hello" into the command line. You should see this.






![Echo_Screen](http://i.imgur.com/dtD91g3.png)



_echo_ can also be used to pass an input into another command but we'll elaborate on that more in the redirection/piping [article](https://wiki.onion.io/Tutorials/LinuxBasics/Redirection_Part4).





We will now explore the filesystem on the Omega.
