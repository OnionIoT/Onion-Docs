##**Redirection**



Using the the redirection tools we are able to create dynamic commands. 



####**Input/Output Redirection**

We can use redirection to send the output of one command to files.



We have already seen an example of this in the previous tutorial, when we used the _cat_ command to create a new file. 



When we executed the command:



```cat > filename```



After the file was created,  we were prompted by the terminal to enter something by the cat command.The output of cat was redirected as input into the file's contents. This is known as output redirection. 



We can also use the echo command in a similar manner.

Follow the example below. 



 

![RedirOut_Screen](http://i.imgur.com/EWQ0SvZ.png)



We can redirect the output commands so it does not overwrite the contents of the file but rather appends to it. For that we use the pattern &gt;&gt;.



Say we wanted to append the date and time to this file we created in the previous example we could use a command like this. 



 

![RedirApend_Screen](http://i.imgur.com/uiJEIn5.png)



####_sort_ command



Now lets try some input redirection, which allows us to pass files as input to commands. For that we will introduce a new command, _sort_, which sorts the content of a file in alphabetical order by default. 



```sort < filename```



In the next example we will create a new file with randomly assorted letters, called alpha. We will use the command:



```sort < alpha.txt```



This will display the letters of the file in alphabetical order.



 

![RedirIn_Screen](http://i.imgur.com/TIkn320.png)



Now let's put both types of redirection in a practical example. In the next screen we will use output of the past screen as input into a new file containing the ordered alphabet. To do this we use the command.



```sort < alpha.txt > ordered.txt```



 

![RedirInOut_Screen](http://i.imgur.com/gi6NDdA.png)



As you can see the ordered.txt file stores the contents of alpha.txt in alphabetical order. 





Now we will move onto Piping. 



####**Piping**



As we learn more commands Pipes will allow us to create dynamic commands by passing the output of one command into the input of another command. Use of a pipe is indicated through the symbol |  



To demonstrate the power of piping we will create a files called "names.txt" which will have a different name on each line. We will then execute the following command. 



```cat names.txt | grep a```



The output of cat is passed as input to the input of the _grep_ command which searches the output for all lines containing the character "a" and then do the same for all lines with "j". The end result will display all lines with "a" and "j" in a line . We have demonstrated this in the screenshot below. 





 

![Pipe_Screen](http://i.imgur.com/wZbo9Hk.png)



We recommend that you get comfortable with using pipes as they are essential in accomplishing more complicated tasks. The next topic we will introduce is shell scripting. 
