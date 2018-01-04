## Cross-Compiling for the Omega {#cross-compiling}

Cross compilation just means compiling an executable meant for a platform that's different from the one on which the compilation is being performed. In this case, you will be using your computer, which likely runs on the x86 instruction set, to compile an executable for the Omega, which runs the MIPS instruction set.

The LEDE build system is at the core of our cross compilation efforts; it will build to toolchain which we will then use to cross compile our C or C++ code for the Omega.

> In the article on [using a C compiler on the Omega](#c-compiler-on-omega), it is mentioned that a limitation of compiling on the Omega is that the compiled programs are limited to using only the C standard libraries since only those header files are included on the Omega's filesystem as a space-saving measure.<br>
> The main advantage to cross compiling as opposed to compiling a program directly on your Omega is two-fold:<br>
> your program will be able to use libraries other than the implemented by other LEDE software packages, and,<br>
> the compilation will likely be much quicker on your computer in the cross compilation environment than on the Omega.

This article will explain how to setup the LEDE build system, explain what needs to be done in order to cross compile a program, and then go through an example of cross compilation.

### Setting Up the Build System

The build system can be used to build the cross compilation toolchain, create full firmware images, and create software packages that can be installed with `opkg`. This article focuses only on building the cross compilation toolchain.

> Note: Onion is not responsible for any damage or issues caused by using firmware or packages that do not originate from Onion.


To start, we will need to setup the LEDE build system on your computer, configure it for the Omega, and then build the toolchain. We've had success with this procedure on Ubuntu Linux, we strongly recommend following suit. Use a virtual machine if you don't have a native installation.

Our guide is loosely based on LEDE's own [build system installation instructions](https://lede-project.org/docs/guide-developer/install-buildsystem), check their instructions out if something is unclear.

#### System Setup

The LEDE build system requires quite a few packages, in your Linux environment, run the following command:

```
sudo apt-get install -y git wget subversion build-essential libncurses5-dev zlib1g-dev gawk flex quilt git-core unzip libssl-dev python-dev python-pip libxml-parser-perl
```

This may take some time!

#### Downloading the LEDE Build System

Use `git` to download the build system customized by Onion for the Omega2:

```
git clone https://github.com/OnionIoT/source.git
```

This will take some time but not nearly as much as the previous step!

<!-- #### Build System Feeds Setup

The feeds refer to the repositories of packages

If you intend to use the build system for creating your own firmware, you'll want to update the package feeds and include them

> If you want to install the O

Now we'll update the package feed repositories and in



src-git onion https://github.com/OnionIoT/OpenWRT-Packages.git;omega2 -->

#### Build System Setup

Ok, now we need to setup the build system so that it's configured for the Omega2 and Omega2+. 

> Since you're using the Onion-customized build system, this part will already be done and you can skip down to the Compilation step. We've left the instructions here in case you're using the original LEDE build system.

Go into the `source` directory and start the build system menu:

```
cd source
make menuconfig
```

![menuconfig](https://raw.githubusercontent.com/OnionIoT/Onion-Docs/master/Omega2/Documentation/Doing-Stuff/img/lede-menuconfig.png)

In the menu that appears, you will need to do the following:

* For `Target System`, select `MediaTek Ralink MIPS`
* For `Subtarget`, select `MT7688 based boards`
* For `Target Profile`, select `Multiple Devices`
* A new item will appear on the Main menu, `Target Devices`
* For `Target Devices`, select `Onion Omega2` and `Onion Omega2+`
* Exit and save your configuration

Now your LEDE build system is configured to create a toolchain, firmware, and packages that are compatible with the Omega2 and Omega2+!

#### Compilation

The only thing that's left is to compile the toolchain. The build system is based on makefiles, so a simple command will start the process:

```
make
```

If you have a bleeding edge processor that can handle a bunch of threads, you can use the following command:

```
make -j8
```

Where the `8` defines the number of compilation jobs to run simultaneously.

Depending on your system, the compilation will take quite some time and be very resource intensive, be patient! On server-grade systems, compilation will take about half an hour, on regular desktop or laptop systems **it may take hours**.


### Cross Compiling {#cross-compiling-procedure}

Now that the toolchain is built, we can use it to cross compile our own programs.

#### Concepts & Locations

Let's first cover a few important concepts and locations of the compiled build system.

The Toolchain:

* The toolchain is the cross compiler and standard library that we will use to compile code for the Omega
	* Note that the cross compiler is specific to the processor type!
* The toolchain can be found in the `staging_dir` directory with a name following the pattern: `staging_dir/toolchain-<CPU-ARCHITECTURE>_gcc-<GCC-VERSION>_<C-LIBRARY-NAME>/`
	* In our case it's: `staging_dir/toolchain-mipsel_24kc_gcc-5.4.0_musl/`
* All of our compilation tools can be found at: `staging_dir/toolchain-mipsel_24kc_gcc-5.4.0_musl/bin/`, this includes:
	* `mipsel-openwrt-linux-ar`
	* `mipsel-openwrt-linux-g++`
	* `mipsel-openwrt-linux-gcc`
	* `mipsel-openwrt-linux-gcc-nm`
	* `mipsel-openwrt-linux-gcc-ranlib`
	* `mipsel-openwrt-linux-gdb`
	* `mipsel-openwrt-linux-ld`
* The `staging_dir/toolchain-mipsel_24kc_gcc-5.4.0_musl/include/` directory holds all of the header files for the C standard library
* And the `staging_dir/toolchain-mipsel_24kc_gcc-5.4.0_musl/lib` directory holds the C standard library shared objects

The Target:

* The target holds everything the build system needs to
* The target can be found in the `staging_dir` directory with a name following the pattern: `staging_dir/target-<CPU-ARCHITECTURE>_<C-LIBRARY-NAME>/`
	* In our case it is: `staging_dir/target-mipsel_24kc_musl/`
* Header files of libraries added as packages can be found in the   `staging_dir/target-mipsel_24kc_musl/usr/include/` directory
	* **This is important** as our code will likely use header files from this location
* Shared objects for the libraries added as packages can be found in the `staging_dir/target-mipsel_24kc_musl/usr/lib/` directory
	* **This is important** since code that uses these libraries needs to be linked to these shared objects during compilation


#### The Cross Compilation Process

The process for cross compiling is straight-forward, we just need to ensure the following things when compiling:

1. We're using the cross compiler version of `gcc`/`g++`
1. We're using the cross compiler version of the linker
1. The compiler flags extend the *include search path* to include:
	* The toolchain header directory, `staging_dir/toolchain-mipsel_24kc_gcc-5.4.0_musl/include/`
	* The target header directory, `staging_dir/target-mipsel_24kc_musl/usr/include/`
1. The linker flags extend the *library search path* to include:
	* The toolchain library shared object directory, `staging_dir/toolchain-mipsel_24kc_gcc-5.4.0_musl/lib`
	* The target library shared object directory, `staging_dir/target-mipsel_24kc_musl/usr/lib/`

The additions to the *include search path* let the compiler know to also check in those directories when looking for header files that are `#include`-ed in your program. Similarly, the additions the the *library search path* let the compiler/linker know to also check in those directories when looking for shared object files.

The above requirements can be achieved in several different ways:

1. Directly using the cross compiler and libraries
1. Writing a Makefile that does all of the above
1. Writing a generic Makefile and a script to invoke the Makefile with all of the above configured

See [this cross-compilation guide](http://telecnatron.com/articles/Cross-Compiling-For-OpenWRT-On-Linux/#scamlSectionId-3) for ideas on how to accomplish the first two method. See our example below on how to implement the third method.

#### A Cross Compilation Example

This example will illustrate how a C project can be cross compiled for the Omega using a generic Makefile and a script to invoke the Makefile such that it outputs a cross-compiled binary executable. The code for the example is available in Onion's [`c-cross-compile-example` repo on GitHub](https://github.com/OnionIoT/c-cross-compile-example).

The C program uses the `libugpio` library to read and print the input value on a user-specified GPIO pin once a second for 20 seconds. As previously mentioned, this program cannot be compiled on the Omega since only the C standard library header files are included on the Omega's filesystem. We could copy over the header files to the Omega but cross compilation is the better and more scalable option.

<!-- TODO: put the github contents of the makefile in a backticks section -->

If you take a look at the [Makefile](https://github.com/OnionIoT/c-cross-compile-example/blob/master/makefile) in the repo, you'll notice that the compiler and all of the flags are variables. The significance of this will become clear when you take a look at the [`xCompile.sh` script](https://github.com/OnionIoT/c-cross-compile-example/blob/master/xCompile.sh). The script does the following:

1. Maps out the paths to the:
 	* Cross compiler toolchain
	* Library headers
	* Library shared objects
1. Generates the flags for extending the include and library search paths
1. Invoke the Makefile with the compiler, flags, and libraries to link overridden with the above

To accomplish this the user needs to run the script with arguments that define where the LEDE build system can be found and which libraries need to be linked:

```
sh -buildroot <path to buildroot> -lib <list of additional libraries to link in compile>
```

For this example program, assuming the LEDE build system can be found at `/root/source`, the command would be as follows:

```
sh xCompile.sh -buildroot ~/source/ -lib ugpio
```

This will result in a cross compiled executable, `gpioRead`.

Let's take a closer look at it:

```
root@b6b5a4128ee3:~/c-cross-compile-example# file gpioRead
gpioRead: ELF 32-bit LSB executable, MIPS, MIPS32 rel2 version 1, dynamically linked, interpreter /lib/ld-musl-mipsel-sf.so.1, not stripped
```

Success! We've cross compiled a program for the Omega! [Transfer the file to your Omega](#transferring-files), use `chmod +x gpioRead` to give it executable permissions, and run it with `./gpioRead`.
