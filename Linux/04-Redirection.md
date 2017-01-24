## Redirection {#redirection}

When you run a command on the command line, you may see some text output or sometimes even be prompted for input. However, you can directly pass the output of one command as input to a file or another command, and the output of that command to another, and so on. This technique is known as **redirection**, and you can use this to create dynamic commands!

### Input/Output Redirection

We have already seen an example of this in the previous tutorial when we used the `cat` command to create a new file. When we executed the command:

```
cat > filename
```

we were prompted by the terminal to enter some text. This text was then passed from `cat` as input into the file's contents. This is known as **output redirection.**

#### `echo` command

We can also use the `echo` command in a similar manner. Follow the example below.

![RedirOut_Screen](http://i.imgur.com/EWQ0SvZ.png)


In this case, the `>` sign means to overwrite any contents of the file or create the file if it does not exist.

However, we can also redirect a command's output so it adds to the end (bottom) of the file rather than overwriting it. Instead of a single `>`, use two like so: `>>`

For example, let's say we wanted to append the date and time to the file we created in the previous example. We can use a command like this below:

![RedirApend_Screen](http://i.imgur.com/uiJEIn5.png)

#### `sort` command

Now let's try passing files as input to commands so that they can operate on the contents. This is known as **input redirection.**

For example, let's use the `sort` command. This command sorts the content of a file in alphabetical order by default.

```
sort < filename
```

In the next example we'll create a new file with randomly assorted letters called `alpha.txt`. Run the following command:

```
sort < alpha.txt
```

This will display the letters of the file in alphabetical order.

![RedirIn_Screen](http://i.imgur.com/TIkn320.png)

#### Example

Now let's try both types of redirection in a practical example. In the next screen we will use output of the `sort` step as input into a new file containing the ordered alphabet. Run the following command:

```
sort < alpha.txt > ordered.txt
```

![RedirInOut_Screen](http://i.imgur.com/gi6NDdA.png)

As you can see the ordered.txt file stores the contents of `alpha.txt` in alphabetical order.

Now we will move onto Piping.

### Piping

To create really dynamic commands, we can pass the output of one command into the input of another.  This is known as **piping**.

The pipe symbol is `|`; it's not a lowercase "L" nor a numeral 1! If you're confused on where to find it, it's usually `Shift+\` on US keyboards and may look like a broken line.

To show you the power of piping, let's create a file called `names.txt` which will have a different name on each line. Then execute the following command:

```
cat names.txt | grep a | grep j
```

Here's what's going down:

* `cat` outputs the contents of `names.txt`.
* The output of `cat` is passed as input to a `grep` command, which searches for and outputs only the lines containing the character `a`.
* The output of the above step is passed to another `grep` command. This time, `grep` searches for and outputs only the lines containing the charactter `j`.

The end result will display all lines with both "a" and "j" in a line . Check it out in the screenshot below:

![Pipe_Screen](http://i.imgur.com/wZbo9Hk.png)

We recommend getting comfortable with using pipes as they are essential in accomplishing more complicated tasks!

Next up, we'll show you how to be lazy. Writing a command over and over again can get tedious, but [shell scripting](#shell-scripting) lets you write once and run over and over again.
