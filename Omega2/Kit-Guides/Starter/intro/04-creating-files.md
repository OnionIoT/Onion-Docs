## File Editing on the Omega

<!--
// this article is a description of how we're going to use `vi` to write the code we need for the experiments

// intro to article:
//	* the experiments we're going to do involve writing Python scripts
//	* here we'll learn how to write scripts using the command line
//	* we'll be using the Vi text editor
-->

In this Guide, there will be many experiments that make use of Python and Shell scripts. To get these scripts to run, we store the program code on the Omega as a file.

On the Omega, there's only one text editor - `Vim`. It's different from more familiar editors in how it works, so we'll cover the basics super quickly to get to making cool things faster!

### Creating or Opening a File

<!--
// `vi <filename>`
// if the file doesn't exist, will create it
// if the file already exists, will open it
-->

To work with a file, simply call `vim <filename>`. It will work if you do `vi <filename>` as well.

If the file already exists, it will be opened in Vim. If it doesn't, Vim will open an empty temporary file with the given name.

>The temporary file won't be permanent until you save it!

The file is open, but nothing happens when we type! So how do we edit and input text?


### Writing Text

<!-- // process: Have to hit `i` to be able to instert text, even before copy pasting -->

Hit `i` to get into 'insert mode', now we can start entering text!

The controls should now be quite familiar if you've used notepad before. The keys will insert characters, the arrow keys will nagivate, and `home/end/pgup/pgdn` will behave accordingly. 

Vim has multiple modes. Key presses behave differently in different modes. Entering characters and pasting with `ctrl-shift-v` will only work in **insert mode**.

The other mode is what Vim begins in - **normal mode**. In normal mode, all keystrokes are interpreted as commands. So all the text you want to paste will be interpreted as commands, causing lots of unpredicatble changes to the file.

If mistakes were made, what can we do?


### Undo and Redo

Undo is a normal mode function, hit `ESC` and press `u` to undo the last bit of changes made. 

To redo hit `ctrl-r` in normal mode.

`ESC` is the universal command in Vim that changes the current mode to normal mode. Pressing `u` in normal mode will undo the last changes made instead of inserting the `u` character.

But wait, there's more!


### Copy and Paste

Copying and pasting in vim can be done with the terminal shortcuts - `ctrl-shift-c` to copy, and `ctrl-shift-v` to paste. Note that paste only works in insert mode, and text will always be pasted where the cursor is! Note they may be different depending on the shortcuts your terminal supports.

Sometimes, Vim will automatically insert tabs in front of new lines, this will cause pasted code to turn into a [staircase](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Kit-Guides/img/vim-staircase-effect.png). To keep this from happening, enter `:set paste` in normal mode. To bring back auto indenting, enter `:set nopaste`.

Typing `:` calls up the 'command line' of Vim, where we can run Vim's less often used functions. Since `:` works just like a command prompt, we have to hit enter to send our command to it.

>The more commonly used commands in Vim are related to moving around and editing chunks of text - like `u` for undo.

Once the code is fixed up, it's time to save!


### Saving Changes

<!-- // process: `:w` to save changes -->

Hit `ESC` to enter normal mode, then `:w` and enter.

Just like `set paste`, we call up the vim command prompt here. The command we give it is `w` which stands for '**w**rite to file'. 

Now that we've saved, we'll have to exit Vim to test the script.


### Quitting and Saving changes

<!-- // process: `:wq` to save changes and exit vi -->

`ESC`, then enter `:wq`

The quitting process is very similar to saving - return to normal mode with `ESC`, type `:` to enter the `q` command to **q**uit Vim. Vim also has the ability to accept multiple commands and execute them in order. So we can save **and** quit by typing `:wq`.


### Quitting without Saving Changes

<!-- // process: `:q!` to quit without saving changes -->

`:q!` will force Vim to quit from normal mode.

Normally when trying to exit Vim with unsaved changes, Vim will deny the attempt as a safe measure. But quitting without saving is also useful to revert really big changes.



<!--
// NOTES FROM LAZAR:
// * the above outlines are brief but the article should be enough for an absolute beginner to get started with Vi
// * use this as a reference: https://docs.onion.io/omega2-docs/developing-using-the-command-line.html
// * include screenshots if you think it will help get the point across
-->

### More on Vim

<!--
// 'this is a brief intro to vi, it's actually a super powerful editor, learn more wiht this tutorial'
// TODO: find a really good Vi tutorial
-->

There's a lot more than meets the eye with Vim. It's a very powerful editor under the hood with thousands of third-party plugins and versions for all major operating systems. If you want to learn how to make the most out of it, [Open Vim](http://www.openVim.com/tutorial.html) has a fantastic tutorial that can get you started.


