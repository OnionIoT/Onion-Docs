## Ownership and Permissions {#ownership-and-permissions}

In all linux systems there is a hierarchy of users, with the root, also known as super user, sitting at the top. Each of the users have an ownership over their _own_ files and have the right to read, write and execute them as they please. Users do not have the same permissions to other users files. The exception to this is the super user or root. On the Omega, we will not concern ourselves with the user system since we are always logged in as root. 

To further explain the concept, let's revisit the last [tutorial](https://github.com/OnionIoT/wiki/blob/master/Tutorials/LinuxBasics/ShellScript_Part5.md) on scripting. 

In our last tutorial we executed the shell script by using the :

```
sh LogGen.sh
```

Now that command worked by let's say we wanted to drop the sh and run the command:

```
./LogGen
```

We will receive this message from the command line

```
/bin/ash: ./LogGen.sh: Permission denied
```

So lets go ahead and look at the permission on the shell script. To do that run the ls command with the -l option. This will give us a detailed description of the files/subdirectories in our current directory.

```
ls -l
```

You should see something like this...

![LsPerm_Screen](http://i.imgur.com/toiOOTm.png)

For now all we are concerned with is the column containing the stuff that looks like this drwxr-xr-x . If you are interested in a more detailed description of what all the descriptions mean refer to this [article](https://www.linux.com/learn/tutorials/309527-understanding-linux-file-permissions). 

So lets take a look at our permission for the LogGen.sh file. Yours should look like this.

```
-rw-r--r--
```

The first "-" indicates that it is a file, if it were a directory we could make we would find a "d" in its place. The next three characters indicate whether the super user has read,write,executable permission. Similarly the next 6 characters are similar indicators for the user and the usergroup, with "rwx" indicating full permission and "---" indicating no permission. 

####_chmod_ command

Since we are the root user we can give ourselves full permission to the file. So let's go ahead and change the permissions. To do this we will need to employ the  _chmod_ command. At this point, quickly read this [article](http://linuxcommand.org/lts0070.php) describing how to use the command.

To give ourselves full permission enter this command:

```
chmod 777 LogGen.sh
```

To check if the permission has changed enter:

```
ls -l
```

You should see something like this below.

![LsPermChanged_Screen](http://i.imgur.com/DvQMeeP.png)

We have sucessfully given ourselves full permission.

So let's try to to run the LogGen.sh file without sh. 

```
./LogGen
```

![PermGranted_Screen](http://i.imgur.com/7ud9EHX.png)
