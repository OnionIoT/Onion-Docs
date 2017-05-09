We'll cover how to do the following:

* Navigating through the filesystem
* Creating (and deleting) files and directories
* Creating and modifying text files

#### The Filesystem

<!-- // brief intro of the Omega's filesystem
//	* tell them that the stuff in `/` is largely common to all linux systems
//		* can point them to articles on linux/openwrt - if this is too much work rn, put it as a future TODO
//	* point out that we'll be working in `/root`, mention that this is a logical place for us to work since:
//		* this is the home directory of the `root` user, makes sense to keep our files in our home directory
//		* the contents of the `/root` directory will be preserved through fw updates -->

In Linux, everything is a file. So naturally, the file system is where a great deal happens. The filesystem of LEDE is organized like a tree. At the very bottom of a tree is the root, and so it is with our filesystem.

`/` is the universal symbol for the very bottom of the filesystem - the root directory. All the files that the OS has access to can be found under some directory under `/`.

This is not to be confused with the `root` **directory**. In LEDE, every user gets their own 'home' directory to store all their personal files. On the Omega, this is located at `/root/` by default. When we connect to Omegas' command line via `ssh`, we connect as the root and get placed inside the `/root/` folder. (Connecting via serial will place us in `/`.)

In Linux systems, `~` is an alias for the home directory, and can be used in scripts and programs. For example, calling a file in `~/myProject` is equivalent to calling `/root/myProject`.

On the Omega, all the contents in the `/root/` directory will be preserved through any firmware updates. So for our experiments, we'll try to store our files in there so they stay put!

>The home directory on other Linux systems may look like `/home/<username>`

<!-- TODO: list of commands -->
<!-- ### Commands We'll Cover -->

<!-- // create a table of the commands we'll be covering here, should have the command name and what the command allows us to accomplish -->

<!-- // NOTE: if this is far too time consuming, add it as a future TODO -->

### Navigating the Filesystem

<!-- // brief intro to the commands we're going to cover in this section, like: 'We'll learn how to change directories with the `cd` command, see what's in directories with `ls`' somethhing like that -->

Navigation usually consists of finding our location, looking for landmarks, and then setting a course for our destination. To that end, we'll look at the `pwd`, `ls`, and `cd` commands to let us do just that.

#### Locating Ourselves in the Filesystem

<!--
// pwd command
//	* tells us the full path of the Present Working directory
//	* useful to know where we are so we know where we can go

// include example(s)
-->


When we first drop into the command line, we don't get a lot of information about where we are. We only really know that we're in `root@omega-ABCD`. The `pwd` command will tell us exactly where we are relative to `/`

Immediately after logging in, `pwd` should return something like this:

``` shell
root@Omega-ABCD:~# pwd
/root
```

This tells us we're in the `/root/` folder, one level down from `/`. Notice that the prompt (all the things before `#`) already tells us where we are, the `~` is exactly our working directory `/root`.

#### What's in a Directory?

<!--
// ls command
//	* talk about the basic `ls`, how it lists the contents of the current directory
//	* talk about how it can be used to list the contents of other directories
//		* using relative paths
//		* using absolute paths
//	* command options:
//		* ls -1, shows one line per item in directory
//		* ls -l, gives it in a list format, (very) briefly cover the columns
-->

Now that we know where we are, we should take a look at our surroundings. To list out every file in a directory, the `ls` command is our go to.

For example, on one of Onion's office Omegas, this is what `ls` outputs:

``` shell
root@Omega-ABCD:~# ls
MAK01-dimmingLeds.py  checkAS6200Temp.sh
binify.sh             checkTemp.py
```

Awesome, now we know there's four files in the working directory.

But wait, there's more! Not only can `ls` list the working directory, if we give it a **path**, it can also peek into that path.

> A **path** is the full location of something in the filesystem, starting from the root.

Let's say we want to take a look into our `/` directory, we can append `/` as an argument like so:

``` shell
ls /
```

Which might return something like this:

``` shell
root@Omega-7CCB:~# ls /
bin           lib           rom           tmp
mnt           root          usr           dev
overlay       sbin          var           etc
proc          sys           www
```

The prompt tells us we're still in `~`, but those are folders in `/`.

<!-- TODO: add `ls -l` since it's hella useful -->

#### You can Get There from Here

<!-- TODO: This section is too long and needs to be summarized -->

<!-- // cd command
//	* allows us to change the current working directory
//		* using relative paths
//		* using absolute paths

// include example(s) -->

Of course we can't stay in the same working directory forever. We can move aroudn directories using the `cd` command. It stands for **change directory**.

The most frequent use of `cd` is in conjuction with a path as the argument, like so:

``` shell
cd /root
```

This command changes the present working directory to `/root`.

Earlier, we mentioned the idea of a 'path' in passing. A path (or 'absolute path') is like the full address to something in the file system. For example, if you have a directory called `kittens` in your `/root` folder, the path of that directory is `/root/kittens`. Similarly, for a file called `adorable.jpg` in `/root/kittens`, the path would be `/root/kittens/adorable.jpg`.

Typing out the full path everything can become tedious, so there are many shortcuts that `cd` can understand in the form of 'relative paths'. There are some path aliases that change where it leads depending on the context.

* To go to the `/root` on the Omega (or the home folder as a different user) `cd` with no arguments will take us there.
* The relative path for the 'directory above' is `..`, so `cd ..` will take us up one level no matter where we are.
* To get to any sub-directories in the working directory, we can `cd <name of directory>` instead of the absolute path.

All of the shortcuts above work with each other too!

Let's say we want to move two directories up:

``` shell
cd ../..
```

The first `..` expands to 'up one level', and in that directory, `..` again will of course take us back up once more.

We can also move to other directories contained in parent directories. If `..` had a directory called `puppies`, we could run:

If we want to `cd` up and sideways into the `kittens` directory, we can use the path `../kittens` - up one level, and into `kittens` below.



### Interacting with the Filesystem

<!-- // brief intro to the commands we're going to cover in this section, like: 'We'll learn how to change directories with the `cd` command, see what's in directories with `ls`' somethhing like that -->

Navigating is very useful, but doing things with files is what gets projects working! So to do that, we'll go over commands to create and delete directories, and creating and removing files.

We'll cover the `mkdir` and `touch` commands to create things, and the `rm` command to get rid of them.

#### Creating Directories

<!-- // mkdir command
// * allows us to create new directories
//		* using relative paths
//		* using absolute paths

// include example(s) -->


The `mkdir` command allows us to create empty directories. Run it like so:

```
mkdir <DIRECTORY>
```

You can use both relative and absolute paths. See the example below:

```
root@Omega-ABCD:~# mkdir hello               # relative path
root@Omega-ABCD:~# ls
hello
root@Omega-ABCD:~# mkdir /root/hello/world   # absolute path
root@Omega-ABCD:~# cd hello
root@Omega-ABCD:~/hello# ls
world
```

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
    * This will make the program continue if it runs into an error when trying to delete a file.

<!-- TODO: example -->
