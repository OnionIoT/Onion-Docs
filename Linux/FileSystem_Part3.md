##**Exploring The OpenWRT File System**



All files in the Linux OS are organized into directories. For Windows users, this is akin to organizing files into "folders". An important point to note is that everything in Linux can be classified as a file or directory. 



By the end of this section, the reader will be able to:



1)navigate directories



2)create/delete directories and files







###_**How To Navigate In Linux**_



Firstly, connect your Omega and open up the terminal. 



####_pwd_ command 



The first command we will learn is the pwd command, which stands for print working directory. Type _pwd_ in the command line and hit enter. 



You should see ... 



 


![Pwd_Screen](http://i.imgur.com/oisFW07.png)



The command line has returned "/", this means that we are at the top of the directory. If your command line has returned anything else, for example "abc/def/ghi" it means that you are in that directory. 







####_ls_ command 



The ls command list the contents of the directories. This may include, files, other directories(known as sub-directories), and programs. This is extremely useful command when looking for things in a directory. So let's see what's in our homeGETPROPERNAMEFORTHIS directory. Type "ls" into the command line and hit enter. You should see the sceen below 



 

![Ls_Screen](http://i.imgur.com/vmAsoz8.png)



As you can see, the command displayed the contents in our "home" folder.  You may or may not see the items in color depending on how you connect to the Omega. Since we are using Putty, we see them in color. Below is a short list of what the colors mean:



1) blue = directory 



2) green = executable or recognized data file



3) sky blue = linked file



4) yellow with black background = device



5) pink = graphic image file 



6) red = archive file



If your still interested in the color coding, it might be worth giving [this](http://askubuntu.com/questions/17299/what-do-the-different-colors-mean-in-the-terminal) a read. Additionally, you can use the _ls_ command with the -l option for a more detailed list of the directory, we will use this in the Owners/Permissions [Section](https://github.com/OnionIoT/wiki/blob/master/Tutorials/LinuxBasics/Permissions_Part6.md).





####_cd_ command 



 _cd_ (change directory) is the main command we will use to navigate directories. 



To change to a particular directory all we have to do is type _cd_ into the terminal followed by the path,



 <pre><code>cd &lt;path&gt;</code></pre>

 

 Let's try change our directory to &lt;/usr/bin/&gt; directory. 

 

 

![CdPath_Screen](http://i.imgur.com/trJwXA3.png)



The _pwd_ command is used to show we have succesfully changed directories. 



The table below shows some of the different options you can use with the _cd_ command that make life easier. Go ahead and play around with them until you are comfortable. 



| _command_ [option]   |      Descripton      |  

|----------|-------------|

| _cd_  |    Using _cd_ by itself will take you to the root directory.       | 

| cd .. |    This will take you up one one level to the parent directory.   |  

| cd .  | This will keep you in your curent directory.|    

| cd -  | This will change you to your previous directory, convenient when working in two directories simultaneously.|



###_**How To Create/Delete Files And Directories**_



####_mkdir_ command 



The _mkdir_ allows us to create directories. This simplest way to use it is to type _cd_ followed by the name of the new directory into the terminal and hit enter. This will create the new directory in your present working directory. 



<pre><code>mkdir newdirectoryname</code></pre>



Let's create a new directory called "NewDirectory".



 Mkdir Screen: 

![MkDir_Screen](http://i.imgur.com/p31a1Y4.png)



We have successfully created our a new directory called "NewDirectory" in our current working directory.



You can also create multiple directories inside your current directory by entering this into your terminal:



<pre><code>mkdir newdirectoryname1 newdirectoryname2 newdirectoryname3</code></pre>



Go ahead and try this on your own.Enter the ls command and you should be able to see all three newly created directories in your current directory.



We can also use _mkdir_ to create a directory in a directory other than the one we are currently in. Simply type _mkdir_ followed by the &lt;path/newdirectoryname&gt;. In our example, we will create a new directory named "NewDirectory" inside the &lt;/tmp/usr/&gt; sub-directory, from our current working directory. 



<pre><code>mkdir &lt;path/newdirectoryname&gt;</code></pre>



 

![MkDir_PathDir_Screen](http://i.imgur.com/TD1KOuy.png)



In the screenshot above, we use the cd, pwd and ls functions to show the contents of the /tmp/usr/ subdirectory before and after executing the _mkdir_ command from the / directory. We successfully created the "NewDirectory" in the /tmp/usr sub directory. 



You can also create multiple directories inside your another directory by entering this into your terminal:



<pre><code>mkdir &lt;path/newdirectoryname1&gt; &lt;path/newdirectoryname2&gt;  &lt;path/newdirectoryname3&gt; </code></pre>



Go ahead and try this on your own.Enter the ls command and you should be able to see all three newly created directories in your current directory.



Now that we have created all these new directories, it seems fitting that we learn how to delete them.



####_rmdir_ command 



The _rmdir_ command allows us to delete a directory. It is used in an almost identical way to the _mkdir_ command. For that reason, we will forgo most explanation and simply demonstrate an example of its usage in the screen shot below. Readers are encouraged to try on their own. 



<pre><code>rmdir DirectoryName</code></pre>           



or 



<pre><code>rmdir &lt;path/directoryname&gt;</code></pre> 



 

![RmDir_Screen](http://i.imgur.com/QPo4AWQ.png)





Now that we have learned how to create and delete directories, we will learn how to do the same for files. 



####_touch_ command



The _touch_ command is the easiest way to create a new file in linux. It is used in a similar fashion as _mkdir_ and _rmdir_ commands, including creating multiple files at once.



<pre><code>touch newFileName</code></pre>



or 



<pre><code>touch &lt;path/newFileName&gt;</code></pre>



Refer to the screenshot below for an example of its usage. 





![Touch_Screen](http://i.imgur.com/dSfGlfz.png)



Using touch allows us to create a new file, but what if we want to create a new file and place content into it right away. For that, we will introduce the cat command.





####_cat_ command



_cat_ is a powerful command that allows us to write as well as display contents to the file. 



Firstly to create a file type this into your command line and hit enter(make sure newfile does not already exist in that folder otherwise you will overwrite the file):



<pre><code>cat &gt; newfile</code></pre>



Now you will notice that you have not returned to the command line, instead the terminal is expecting more input. This is where you input the contents of the file. Once you are finished writing the contents of the file you can return to the command line using ctrl + d. 



Similarly you can do the same for files that are in other directories by using the command:



<pre><code>cat &gt; &lt;path/newfile&gt;</code></pre>



To display the contents of a file we can use the _cat_ command as such:



<pre><code>cat filename</pre></code>



or



<pre><code>cat &lt;path/filename&gt;</code></pre>





In the example below we will create a file named HelloWorld.txt in a directory other than our current one, write Hello World! to the file and display its contents from the terminal.



 

![Cat_Screen](http://i.imgur.com/QI145Tn.png)



For users who would like to explore file editting in more detail, click [here](http://www.howtogeek.com/102468/a-beginners-guide-to-editing-text-files-with-vi/). 



Finally we will learn how to delete files.



####_rm_ command



The _rm_ command is used to delete files in the same way _rmdir_ deletes directories. 



_rm_ filename



or 



<pre><code>rm &lt;path/filename&gt;</pre></code>



As our example we will delete the HelloWorld.txt we created above. 



 


![Rm_Screen](http://i.imgur.com/IABPbx4.png)



This concludes our introduction of Linux Filesystem. At this point, the reader should feel comfortable with navigating in Linux. In the following articles/sections we will look at some more advanced topics such as redirection and shell scripting. 
