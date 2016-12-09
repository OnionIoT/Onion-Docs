---
title: Transferring Files
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 4
---

## Transferring Files to the Omega {#transferring-files}


The Omega is incredibly powerful in that it is a full Linux computer. This means that it has its own filesystem, allowing you to store files directly on the Omega. It also means that you can take your files from an external device and copy them to your Omega. This tutorial will show you how you to transfer files from Windows, Mac OS X, and Linux.

// TODO: add blurb about uploading files using the editor


### Using Windows

The Omega can use the SCP file protocol to transfer files wirelessly. SCP stands for Secure Copy, and is based SSH (Secure Shell).

In this tutorial we're going to use WinSCP to transfer our files.


> You'll need to have Apple's Bonjour Service in order to connect to the Omega's hostname. You can download Apple's Bonjour on [their website](https://support.apple.com/kb/DL999?viewlocal=en_US&local=en_US)

#### What is WinSCP?

WinSCP is an open source free SFTP client, FTP client, WebDAV client and SCP client for Windows. Its main function is file transfer between a local and a remote computer. Beyond this, WinSCP offers scripting and basic file manager functionality.

In short, it makes creating & updating files on your Omega a lot easier!

#### Getting Started

First, download [WinSCP from their site](https://winscp.net/eng/download.php).  

Once downloaded, install the application and then run it.

#### Configure the Connection

<!-- change it so the tutorial is about having the omega connected to a real wifi network -->
<!-- have a note about how it would be different if connecting to the omega's ap -->

Connecting to the Omega is super simple. First, make sure your Omega has internet connection. If this is not the case, follow the [Getting Started guide](#first-time-setup).

![WinSCP Image 1](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/onion-omega-winscp-1.png)

In the right hand pane, you'll need to set the details for your Onion Omega. Typically these are:

|Setting   | Value  |
|:---: | :---:|
| File Protocol | SCP |
| Hostname | omega-ABCD.local |
| Port Number | 22 |
| Username | root |
| Password | onioneer |

![WinSCP Image 2](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/onion-omega-winscp-2.png)

Once finished, press the "Save" button.

On the next window there is a tickbox option to save the password, that's up to you. Saving the password is less secure, but faster to access your Omega.

You can name the connection and you can also you can save a desktop shortcut if desired.

![WinSCP Image 3](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/onion-omega-winscp-3.png)

Now from the left menu you'll see the name you saved the new site as a few moments ago, eg "root@omega-2757.local", click on this, then "Login".

![WinSCP Image 4](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/onion-omega-winscp-4.png)

You will now try to connect to your Omega. On success you'll see this in the window:

![WinSCP Image 5](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/onion-omega-winscp-6.png)

If you connection fails, WinSCP will let you know that the host was not found. If this is the case, make sure that both you and your Omega have an internet connection, and that you have Apple's Bonjour Service installed. If you don't have Apple's Bonjour Service, you can connect to your Omega's access point, and connect to its IP `192.168.3.1` .

As this is your first time connecting via WinSCP you'll receive a warning similar to the one below. That's to be expected, click on "Yes"

![WinSCP Image 6](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/onion-omega-winscp-5.png)

You can now drag and drop between folders on your computer and folders on your Omega. Congratulations, you now have easy remote access to the files on your Omega!

![WinSCP Image 7](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/onion-omega-winscp-7.png)

<!-- explanation of transferring files back and forth -->


### Using Linux or Mac OS X

<!-- step by step instructions on using rsync -->

On Mac OS X or Linux, we can use the command-line utility `rsync` (remote sync) to transfer files to and from the Omega. It's included with Mac OS X and most Linux distributions by default (including the Omega's).

<!-- TODO: remove the installation part, maybe link to a page on rsync iunno -->
In case you don't have it, simply run the below commands to install it on your local machine:

```
sudo apt-get update
sudo apt-get install rsync
```

`rsync` uses the `ssh` protocol when connecting to remote servers. When working with an Omega, specify the username as `root` and provide the password when prompted (`onioneer` by default).

`rsync` can simply send files as-is over to the remote server, but if the files already exist then it takes a smarter approach to sending new data. It will look at the *differences* between the two sets of files, then applies the differences to the files to bring them up-to-date.


#### Push Directories and Files to the Omega

<!-- TODO: small blurb - make sure you're connected to the same wifi etc -->

##### Copying Whole Directories
First make sure you're connected to the same WiFi network/LAN as your Omega. Then to quickly copy an entire directory to your Omega, fill in this template with the paths of your folders, where `ABCD` is your Omega's factory name:

<!-- add <> to signify variables -->

```
rsync -a <LOCAL DIRECTORY> root@Omega-<ABCD>.local:~/<DIRECTORY TO PUSH TO>
```

Example and result:

```
rsync -a ~/my-cool-project root@Omega-ABCD.local:~/remote-directory

On Omega:
ls ~/remote-directory
my-cool-project
```

##### Copying the Contents of a directory
To copy only the *files* inside a directory, add a `/` to the end of `<LOCAL DIRECTORY>` like so:

```
rsync -a -v <LOCAL DIRECTORY>/ root@Omega-<ABCD>.local:~/<DIRECTORY TO PUSH TO>
```

Example and result:

```
## my-cool-project contains files called file1, file2, and file3
rsync -a ~/my-cool-project/ root@Omega-ABCD.local:~/remote-directory

On Omega:
ls ~/remote-directory
file1 file2 file3
```

##### Copying a Single File
To push a single file to the Omega:

```
rsync -a <LOCAL FILE> root@Omega-<ABCD>.local:~/<DIRECTORY TO PUSH TO>
```

Example and result:

```
rsync -a ~/my-awesome-file root@Omega-ABCD.local:~/remote-directory

On Omega:
ls ~/remote-directory
my-awesome-file
```

If you get a warning about connecting to an unknown host, type 'yes' (as this is your Omega).

#### Pull from Omega

Entire directory:

```
rsync -a root@Omega-<ABCD>.local:~/<DIRECTORY TO PULL FROM> <LOCAL DIRECTORY>
```

Files only:

```
rsync -a root@Omega-<ABCD>.local:~/<DIRECTORY TO PULL FROM>/ <LOCAL DIRECTORY>
```

#### Adding Your SSH Key

<!-- Add a link to the article on adding your SSH key to the Omega LATER -->

To skip the password prompt, you can add your SSH key to the Omega.

#### Going Further

This part will show you all of the in and outs of `rsync`.

Using a push command, the syntax for the command is explained below:

```
rsync -a [<OPTIONS>] <LOCAL DIRECTORY> <USERNAME>@<REMOTE HOST>:<DESTINATION DIRECTORY>
```

We'll go over each part of the command below.

* **`-a`** - archive mode. Equivalent to a combination of several operations, including but not limited to:
    * `-r` - recursively sync into directories
    * `-l` - preserve symlinks
    * `-t` - preserve modification times
    * and a few more useful flags (`-pgoD`). See the full reference for details: [`rsync` Reference][rsync reference]
    * The `-a` flag is a very convenient flag that you'll want to include in most of your typical calls.

* **`<OPTIONS>`** - some optional flags you can include are:
    * `--progress` - show progress during transfer
    * `-v` - verbose output: the terminal will report events and status
    * `-n` - dry run: see how exactly the files will be synced without actually transferring or overwriting anything.

* **`<LOCAL DIRECTORY>`** - The directory containing the files you want to push. There are two ways this can be done, shown below:

    * `~/my_directory` - copies the folder itself over to the destination, eg. `destination_directory/my_directory`
    * `~/my_directory/` - by adding a `/` at the end, this means the *contents* of `my_directory`. If `my_directory` had files `file1`, `file2`, `file3`, then the remote server would receive the files like so
        * `destination_directory/file1`
        * `destination_directory/file2`
        * `destination_directory/file3`

* **`<USERNAME>`** - the user on the remote system. For the Omega, this will always be `root`.

* **`<REMOTE HOST>`** - the URL or IP of the remote server.
    * This can be typically `Omega-ABCD.local` (`ABCD` being your Omega's factory name)
    * Or it can be the Omega's IP address, eg. `192.168.12.34`

* **`<DESTINATION DIRECTORY>`** - the directory on the remote server where your local files will be sent to, eg. `~/source/my_cool_project`

To see the full list of options and behaviours, see the [`rsync` Reference][rsync reference].

<!-- LATER: add console -->

<!-- link defintions -->

[rsync reference]: http://linuxcommand.org/man_pages/rsync1.html


### Upload Files using the editor
// try adding a {#title} to this guy so we can link directly to this section

// very small intro on the console, link to the console articles
// small intro on the editor, mention that it can be used to manage files on the Omega along with uploading single files using your browser

// walkthrough of uploading a file with pictures
//  1. opening the editor app (install if you haven't already done so - link to installing apps article)
//  2. hit the upload button
//  3. choose where you want to put it
