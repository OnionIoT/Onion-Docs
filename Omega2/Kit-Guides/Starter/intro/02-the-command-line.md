## The Command Line

// intro:
// * describe how the Omega's OS is linux, but a minimalistic version, the way we interface with the Omega is through the command line interface (looking for a super compact version of our linux intro series, but to servo as an intro to this article, https://docs.onion.io/omega2-docs/linux-for-omega-beginners.html )

### The Command Line Interface

// * a brief description of what the command line interface is and how we can use it to change any part of the Omega's OS.
// * for the purposes of the kit we'll be just doing the following:
//		- navigating through the filesystem
//		- creating (and potentially deleting) files and directories
//		- creating and modifying text files

// can use https://docs.onion.io/omega2-docs/the-command-line-interface.html as a reference, but  don't talk about the login, date, and echo commands like the article


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

#### (NEED A DECENT TITLE FOR THE TOUCH COMMAND)

// touch command
//	* if the file doesn't exist, it creates an empty file
//	* if the file exists, it changes the last modified date.
//		- have an example of this and use `ls -l` to show the before and after

// include example(s)

#### Deleting Files and Directories

// rm command
// 	* show how to delete a file
//		- talk about the `rm -f` option to not get asked if you're sure you want to perform the delete
// 	* show how to delete a directory, `rm -rf`
//		- briefly explain why we need the recursive `-r` flag
//		- mention `rmdir` as an alternative

// include example(s)
