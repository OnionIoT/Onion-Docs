## Exploring The File System {#exploring-the-file-system}



All files in the Linux OS are organized into directories. For Windows users, this is akin to organizing files into "folders". An important point to note is that everything in Linux can be classified as a file or directory.



By the end of this section, the reader will be able to:



1)navigate directories



2)create/delete directories and files







### How To Navigate In Linux



Firstly, connect your Omega and open up the terminal.



#### `pwd` command



The first command we will learn is the pwd command, which stands for print working directory. Type `pwd` in the command line and hit enter.

You should see ...


![Pwd_Screen](http://i.imgur.com/oisFW07.png)

The command line has returned "/", this means that we are at the top of the directory. If your command line has returned anything else, for example "abc/def/ghi" it means that you are in that directory.

#### `ls` command

The ls command list the contents of the directories. This may include, files, other directories(known as sub-directories), and programs. This is extremely useful command when looking for things in a directory. So let's see what's in our homeGETPROPERNAMEFORTHIS directory. Type "ls" into the command line and hit enter. You should see the sceen below

![Ls_Screen](http://i.imgur.com/vmAsoz8.png)

As you can see, the command displayed the contents in our "home" folder.  You may or may not see the items in color depending on how you connect to the Omega. Since we are using Putty, we see them in color. Below is a short list of what the colors mean:

1) blue = directory

2) green = executable or recognized data file

3) sky blue = linked file

4) yellow with black background = device

5) pink = graphic image file

6) red = archive file

If your still interested in the color coding, it might be worth giving [this](http://askubuntu.com/questions/17299/what-do-the-different-colors-mean-in-the-terminal) a read. Additionally, you can use the `ls` command with the -l option for a more detailed list of the directory, we will use this in the Owners/Permissions [Section](https://github.com/OnionIoT/wiki/blob/master/Tutorials/LinuxBasics/Permissions_Part6.md).

#### `cd` command

 `cd` (change directory) is the main command we will use to navigate directories.

To change to a particular directory all we have to do is type `cd` into the terminal followed by the path,

 ```
 cd path
 ```

 Let's try change our directory to /usr/bin/ directory.



![CdPath_Screen](http://i.imgur.com/trJwXA3.png)



The `pwd` command is used to show we have succesfully changed directories.



The table below shows some of the different options you can use with the `cd` command that make life easier. Go ahead and play around with them until you are comfortable.



| `command` [option]   |      Descripton      |  

|----------|-------------|

| `cd`  |    Using `cd` by itself will take you to the root directory.       |

| `cd ..` |    This will take you up one one level to the parent directory.   |  

| `cd .`  | This will keep you in your curent directory.|    

| `cd -`  | This will change you to your previous directory, convenient when working in two directories simultaneously.|



### How To Create/Delete Files And Directories



#### `mkdir` command



The `mkdir` allows us to create directories. This simplest way to use it is to type `cd` followed by the name of the new directory into the terminal and hit enter. This will create the new directory in your present working directory.



```
mkdir newdirectoryname
```



Let's create a new directory called "NewDirectory".



Mkdir Screen:

![MkDir_Screen](http://i.imgur.com/p31a1Y4.png)



We have successfully created our a new directory called "NewDirectory" in our current working directory.



You can also create multiple directories inside your current directory by entering this into your terminal:



```
mkdir newdirectoryname1 newdirectoryname2 newdirectoryname3
```


Go ahead and try this on your own.Enter the ls command and you should be able to see all three newly created directories in your current directory.



We can also use `mkdir` to create a directory in a directory other than the one we are currently in. Simply type `mkdir` followed by the path/newdirectoryname. In our example, we will create a new directory named "NewDirectory" inside the /tmp/usr/ sub-directory, from our current working directory.



```
mkdir path/newdirectoryname
```





![MkDir_PathDir_Screen](http://i.imgur.com/TD1KOuy.png)



In the screenshot above, we use the cd, pwd and ls functions to show the contents of the /tmp/usr/ subdirectory before and after executing the `mkdir` command from the / directory. We successfully created the "NewDirectory" in the /tmp/usr sub directory.



You can also create multiple directories inside your another directory by entering this into your terminal:



```
mkdir path/newdirectoryname1 path/newdirectoryname2  path/newdirectoryname3
```


Go ahead and try this on your own.Enter the ls command and you should be able to see all three newly created directories in your current directory.



Now that we have created all these new directories, it seems fitting that we learn how to delete them.



#### `rmdir` command



The `rmdir` command allows us to delete a directory. It is used in an almost identical way to the `mkdir` command. For that reason, we will forgo most explanation and simply demonstrate an example of its usage in the screen shot below. Readers are encouraged to try on their own.



```
rmdir DirectoryName           
```


or



```
rmdir path/directoryname
```




![RmDir_Screen](http://i.imgur.com/QPo4AWQ.png)





Now that we have learned how to create and delete directories, we will learn how to do the same for files.



#### `touch` command



The `touch` command is the easiest way to create a new file in linux. It is used in a similar fashion as `mkdir` and `rmdir` commands, including creating multiple files at once.



```
touch newFileName
```


or



```
touch path/newFileName
```


Refer to the screenshot below for an example of its usage.





![Touch_Screen](http://i.imgur.com/dSfGlfz.png)



Using touch allows us to create a new file, but what if we want to create a new file and place content into it right away. For that, we will introduce the cat command.





#### `cat` command



`cat` is a powerful command that allows us to write as well as display contents to the file.



Firstly to create a file type this into your command line and hit enter(make sure newfile does not already exist in that folder otherwise you will overwrite the file):



```
cat  newfile
```


Now you will notice that you have not returned to the command line, instead the terminal is expecting more input. This is where you input the contents of the file. Once you are finished writing the contents of the file you can return to the command line using ctrl + d.



Similarly you can do the same for files that are in other directories by using the command:



```
cat  path/newfile
```


To display the contents of a file we can use the `cat` command as such:



```
cat filename
```


or



```
cat path/filename
```




In the example below we will create a file named HelloWorld.txt in a directory other than our current one, write Hello World! to the file and display its contents from the terminal.





![Cat_Screen](http://i.imgur.com/QI145Tn.png)



For users who would like to explore file editting in more detail, click [here](http://www.howtogeek.com/102468/a-beginners-guide-to-editing-text-files-with-vi/).



Finally we will learn how to delete files.



#### `rm` command



The `rm` command is used to delete files in the same way `rmdir` deletes directories.



`rm` filename



or



```
rm path/filename
```


As our example we will delete the `HelloWorld.txt` we created above.






![Rm_Screen](http://i.imgur.com/IABPbx4.png)



This concludes our introduction of Linux Filesystem. At this point, the reader should feel comfortable with navigating in Linux. In the following articles/sections we will look at some more advanced topics such as redirection and shell scripting.

In the [next section](#redirection), we'll be going over the bread and butter of the command line: redirecting inputs and outputs of commands.
