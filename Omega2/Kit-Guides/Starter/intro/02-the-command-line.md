<!-- // NOTE: when describing the commands, we can lift from our existing article: https://docs.onion.io/omega2-docs/exploring-the-file-system.html
//	let's just make this more concise! -->
## The Command Line

<!-- // intro:
// * describe how the Omega's OS is linux, but a minimalistic version, the way we interface with the Omega is through the command line interface (looking for a super compact version of our linux intro series, but to servo as an intro to this article, https://docs.onion.io/omega2-docs/linux-for-omega-beginners.html ) -->

The Omega's operating system (OS) is based on Linux, a popular open-source OS that powers servers and computers all over the world. The version on the Omega is a minimalistic and lightweight distribution called LEDE, which stands for **Linux Embedded Development Environment**. It supports many programming languages and and can run all kinds of complex projects while still being small enough to fit in the Omega's memory.

### The Command Line Interface

<!-- // * a brief description of what the command line interface is and how we can use it to change any part of the Omega's OS.
// * for the purposes of the kit we'll be just doing the following:
//		- navigating through the filesystem
//		- creating (and potentially deleting) files and directories
//		- creating and modifying text files -->

// can use https://docs.onion.io/omega2-docs/the-command-line-interface.html as a reference, but  don't talk about the login, date, and echo commands like the article

We interact and operate the Omega by usng the **command line interface** (CLI). The CLI is the user’s access point into the operating system using a text-based terminal program. All user interaction is interpreted and executed by the OS through instructions, or **commands**. A user enters a command into a terminal to make something happen.

The CLI can look something like the picture below. In this terminal program on Windows, the green box is where the commands you type will be displayed on the screen.

![command line interface](http://i.imgur.com/hxuce5c.png)

For the purposes of this kit, we'll get to do the following:

* Navigating through the filesystem
* Creating (and potentially deleting) files and directories
* Creating and modifying text files

#### The Filesystem

// brief intro of the Omega's filesystem
//	* tell them that the stuff in `/` is largely common to all linux systems
//		* can point them to articles on linux/openwrt - if this is too much work rn, put it as a future TODO
//	* point out that we'll be working in `/root`, mention that this is a logical place for us to work since:
//		* this is the home directory of the `root` user, makes sense to keep our files in our home directory
//		* the contents of the `/root` directory will be preserved through fw updates



### Commands We'll Cover

// create a table of the commands we'll be covering here, should have the command name and what the command allows us to accomplish

// NOTE: if this is far too time consuming, add it as a future TODO

### Navigating the Filesystem

// brief intro to the commands we're going to cover in this section, like: 'We'll learn how to change directories with the `cd` command, see what's in directories with `ls`' somethhing like that

#### Finding the Current Directory (Maybe there's a better way to say this?)

// pwd command
//	* tells us the full path of the Present Working directory
//	* useful to know where we are so we know where we can go

// include example(s)

#### Seeing the Contents of a Directory (Maybe there's a better way to say this?)

// ls command
//	* talk about the basic `ls`, how it lists the contents of the current directory
//	* talk about how it can be used to list the contents of other directories
//		* using relative paths
//		* using absolute paths
//	* command options:
//		* ls -1, shows one line per item in directory
//		* ls -l, gives it in a list format, (very) briefly cover the columns

// include example(s)

#### Changing Directories (Maybe there's a better way to say this?)

// cd command
//	* allows us to change the current working directory
//		* using relative paths
//		* using absolute paths

// include example(s)


### Interacting with the Filesystem

// brief intro to the commands we're going to cover in this section, like: 'We'll learn how to change directories with the `cd` command, see what's in directories with `ls`' somethhing like that

#### Creating Directories

// mkdir command
// * allows us to create new directories
//		* using relative paths
//		* using absolute paths

// include example(s)

#### Creating Files

<!-- // DONE: touch command
//	* if the file doesn't exist, it creates an empty file
//	* if the file exists, it changes the last modified date.
//		- have an example of this and use `ls -l` to show the before and after

// include example(s) -->

The `touch` command can be used to create files. The syntax looks like this:

```
touch <FILENAME>
```

* If the file doesn't exist yet, it creates an empty file.
* If the file already exists, it updates the time it was last modified to when you ran the command.

You can check the file's last modified time using `ls -l` like in the example below:

``` sh
root@Omega-ABCD:~# touch hello.txt
root@Omega-ABCD:~# ls -l
-rw-r--r--    1 root     root             0 Mar 23 23:38 hello.txt    # we've created our file
root@Omega-ABCD:~# cat hello.txt
root@Omega-ABCD:~#                    # nothing happens, the file is empty
...
(wait a minute or two)
...
root@Omega-ABCD:~# touch hello.txt    # update the time it was last modified
root@Omega-ABCD:~# ls -l
-rw-r--r--    1 root     root             0 Mar 23 23:41 hello.txt    # the modified time updated!
```


#### Deleting Files and Directories

<!-- // DONE: rm command
// 	* show how to delete a file
//		- talk about the `rm -f` option to not get asked if you're sure you want to perform the delete
// 	* show how to delete a directory, `rm -rf`
//		- briefly explain why we need the recursive `-r` flag

// include example(s) -->

Delete a file using the `rm` command like so:

```
rm <FILENAME>
```

To delete a directory and all of the files inside it, run:

```
rm -rf <DIRECTORY>
```

These two options are explained below:

* `-r` - **recursive** mode
    * This means to go into a directory and delete all of the files inside.
    * If it finds more directories, it enters them and deletes their contents as well.
    * This is required when deleting directories, otherwise it will return an error.
* `-f` - **force**
    * When deleting files inside a directory, you'll be asked for confirmation to delete each file. 
    * Use this option to skip this and delete the files right away.
    
