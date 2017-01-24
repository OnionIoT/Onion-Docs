##**Shell Scripting**



A shell script in simply a script that excutes a series of commands written in the script at once from the terminal. This is equivalent to any programming language where you can execute a script from a console. Linux can come with two types of shells, C and Bourne Shell. Since we are using OpenWRT we are only concerned with the latter, which we invoke when we type _sh_ into the command line. At this point, we will write a simple script and explain what will happen at each step during execution. This script uses some general programming techniques. So if you are new to programming, we recommend reading [this](http://www.tutorialspoint.com/unix/unix-what-is-shell.htm) for an in depth explanation. 



<pre><code>

# Anything after the hash symbol is considered a comment.

# This script will create log of the time the script that was executed

# and the name of the person who executed it. The log will be stored in

# a file called log.txt, found in the "/" directory. The script will 

# also display the contents of the log.txt file on the terminal. 





#The line below tells Linux which shell to use for execution

#!/bin/bash 



# Create NAME variable with value name

NAME=name 



# Create DATE variable with value date

DATE=date 



#Prompt User to input their name

echo -n "Please Enter Your Name >"



#Store the value entered by the user into the variable username

read username



#Store the value of our username in NAME variable

NAME=$username

#The DATE stores the value returned by the date command. in form $(command)

DATE=$(date)

#Append the NAME and DATE values to the log.txt file

echo $NAME $DATE >> /log.txt 

#Display the contents of the log.txt file

cat /log.txt

</code></pre>



Copy the script to the "/" folder in your Omega and save it as LogGen.sh. Run the script by entering this script into terminal and see what happens. 

<pre><code>sh LogGen.sh

</code></pre>



Run it a few times entering different names and see what happens in the output. 

It should look something like this.



 

![Shell_Screen](http://i.imgur.com/9Q9mRWm.png)



Our last topic of the Linux Introduction Series, will introduce the concept of users, ownerships and permission in Linux Systems. 
