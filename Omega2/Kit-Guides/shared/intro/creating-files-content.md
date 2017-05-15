### Creating or Opening a File

<!--
// `vi <filename>`
// if the file doesn't exist, will create it
// if the file already exists, will open it
-->

To work with a file, simply call `vim <filename>`. It will work if you do `vi <filename>` as well.

If the file already exists, it will open it in vim. If it doesn't, it will open an empty temporary file with the given name.

>The temporary file won't be permanent until you save it!

If you type things immediately when vim starts, nothing will come out. So how do we get text in?


### Writing Text

<!-- // process: Have to hit `i` to be able to instert text, even before copy pasting -->

Hit `i` to get into 'insert mode', now we can start entering text!

The controls of insert mode should be quite familiar if you've used notepad before. The keys will insert characters, the arrow keys provide nagivation, and `home/end/pgup/pgdn` will behave accordingly.

Vim is based on different modes. Entering characters and pasting with `ctrl-shift-v` will only work in **insert mode**.

Vim begins in **normal mode**, where all keystrokes are interpreted as commands. So all the text you want to paste will be interpreted as commands, causing lots of unpredicatble changes to the file.

If mistakes were made, what can we do?


### Undo and Redo

Undo is a normal mode function, hit `ESC` and press `u` to undo the last bit of changes made. To redo hit `ctrl-r` in normal mode.

The reason we hit `ESC` first is to return to normal mode. So instead of inserting `u`, vim will undo the last changes we made.

Once the code is fixed, it's time to save.


### Saving Changes

<!-- // process: `:w` to save changes -->

Hit `ESC` to enter normal mode, then `:w` and enter.

Entering `:` calls the 'command line' of vim, where we can run vim's less often used functions. The command we give it is `w` which stands for '**w**rite to file'. Since `:` works like a command like, we have to `enter` to send our command to it.

>The more commonly used commands in vim are related to navigating, copy/pasting, and editing chunks of text - like `u` for undo.

Now that we've saved, we'll have to exit vim to test the script.

### Quitting and Saving changes

<!-- // process: `:wq` to save changes and exit vi -->

`ESC`, then `:wq` enter.

The quitting process is very similar to saving - return to normal mode with `ESC`, type `:` to enter the `q` command to **q**uit vim.

Vim also has the ability to accept multiple commands and execute them in order. So we can save **and** quit by typing `:wq`.


### Quitting without Saving Changes

<!-- // process: `:q!` to quit without saving changes -->

```
:q!
```

Forcing vim to quit can be done by adding `!` to the end of the `:q` command.

Normally when trying to exit vim with unsaved changes, vim will deny the attempt as a safe measure. But quitting without saving is also useful to revert really big changes.



<!--
// NOTES FROM LAZAR:
// * the above outlines are brief but the article should be enough for an absolute beginner to get started with Vi
// * use this as a reference: https://docs.onion.io/omega2-docs/developing-using-the-command-line.html
// * include screenshots if you think it will help get the point across
-->

### More on Vi

<!--
// TODO: find a really good Vi tutorial
-->
There's a lot more than meets the eye with vim. It's actually a very powerful editor under the hood and can be installed in all major operating systems. If you want to learn how to make the most out of it, [Open Vim](http://www.openvim.com/tutorial.html) has a fantastic tutorial that can get you started.
