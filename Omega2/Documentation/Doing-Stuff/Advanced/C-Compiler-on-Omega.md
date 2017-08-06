## Compiling C on the Omega {#c-compiler-on-omega}

Since the Omega is a Linux computer, it supports C and C++ programs. By default, `gcc`, the C compiler, and `g++`, the C++ compiler are not installed. This article will explain the limitations of compiling C & C++ programs on the Omega, how to install and then use the compilers.


### Limitations

There are two main limitations when compiling C & C++ programs with the Omega: the processing speed and availability of the headers of libraries.

#### Processing Speed

The Omega's processor is optimized for low power consumption and low heat generation, which means that it's definitely not as powerful as the average modern laptop. This means that compiling large programs will take some time, you'll have to be patient.

#### Library Header Availability

When the Omega's OS is built, the header files for libraries that are not regularly part of the C standard library are not included as a space saving measure. If you take a look at `/usr/lib`, where the library shared object are kept and compare it to `/usr/include`, where the library header files are kept, you'll see the discrepancy: some library objects do not have corresponding header files!

This includes libraries such as:

* libugpio
* [libonioni2c](#i2c-c-library)
* [libonionpwmexp](#pwm-expansion-c-library)
* [libonionoledexp](#oled-expansion-c-library)
* [libonionrelayexp](#relay-expansion-c-library)
* libuci
* libubus
* libjson-c
* libiwinfo

>To use a library in your program, you need to include the header file in your code so that the compiler knows the declaration of the functions that you are using from that library. Then, when the compiler is linking the binary file of your program, it needs to be informed of the location of the library shared object, `.so` file so the program knows where to look during runtime for the compiled definitions of the library functions used in the program.
>If the headers are not present, the compiler **will not** successfully compile the program, even if the library object is present.


#### A Solution

It is possible to overcome to two above-mentioned limitations by using the **LEDE build system on your computer to cross-compile** your program for the Omega.

See the article on [Cross Compilation](#cross-compiling) for more details and instructions.



### Installing the Compiler

The `gcc` compiler takes up quite a bit of space, so the first order of business is to configure the Omega to [boot from external storage](#boot-from-external-storage).

The packages we need are not included in the Onion package repositories, so we'll need to update the repositories that the `opkg` utility checks. Open up `/etc/opkg/distfeeds.conf` and uncomment the following lines:

```
src/gz reboot_base http://downloads.lede-project.org/snapshots/packages/mipsel_24kc/base
```

and

```
src/gz reboot_packages http://downloads.lede-project.org/snapshots/packages/mipsel_24kc/packages
```

>For more info on the package repos the Omega uses, take a look at our [article on using `opkg`](#using-opkg-switch-to-lede-repos)

Once that's done, we can proceed to install `gcc` and the `make` utility:

```
opkg update
opkg install gcc
opkg install make
```

#### Installing a Debugger

If you will be running C & C++ programs, you'll most likely want to debug a program at one point or another. Install the `gdb` to help in that endeavour:

```
opkg update
opkg install gdb
```

There are many resources available online that provide guides on using GDB to debug programs. These two guides offer a good overview on using GDB and are a good place to start:

* [Debugging Under Unix: gdb Tutorial](https://www.cs.cmu.edu/~gilpin/tutorial/)
* [How to Debug using GDB](http://cs.baylor.edu/~donahoo/tools/gdb/tutorial.html)




### Compiling a C Program

Now that you have the compiler installed, let's use it to compile a C program! Create a file on your Omega called `helloworld.c` and populate it with some C code:

```
#include <stdio.h>

int main()
{
	printf("Hello World!\n");
	printf("We're running a C program on the Omega2!\n");
	return 0;
}
```

To compile the program, run the following command:

```
gcc helloworld.c -o helloworld
```

This will produce `helloworld`, an executable binary file that is the compiled version of your C code! Let's run it:

```
root@Omega-665D:~# ./helloworld
Hello World!
We're running a C program on the Omega2!
```

Awesome! You've just compiled your very first C program on the Omega!

#### A Example Program

Take a look at our [`c-example` repo on GitHub](https://github.com/OnionIoT/c-example/) to find a C program and Makefile that can be compiled on your Omega. Connect to your Omega, [install `git`](#installing-and-using-git), clone the `c-example` repo, and run `make` to compile your very own C program.

The output of the compilation will be an executable binary called `gpioRead`. The program will read and print the input value on a user-specified GPIO pin once a second for 20 seconds. Run it with `./gpioRead`!


### Compiling a C++ Program

The `gcc` package we installed with `opkg` also includes `g++`, a C++ compiler, so we can compile C++ programs as well!

The process is very similar to compiling a C program, just a few key differences. Let's create a `helloworld.cpp` file on the Omega and populate it with the following code:

```
#include <iostream>
using namespace std;

int main() {
   cout << "Hello World!" << endl;
   cout << "Now we're running a C++ program on the Omega2" << endl;
   return 0;
}
```

Compile it with the following command:

```
g++ helloworld.cpp -o helloworld2
```

This produces an executable binary file, `helloworld2` that is the compiled version of your C++ code!

Let's run the binary:

```
root@Omega-665D:~# ./helloworld2
Hello World!
Now we're running a C++ program on the Omega2
```



### Going Further

The `gcc` and `g++` compilers are really powerful and configurable. When used in conjunction with the `make` utility we installed, you will be able to create and compile a variety of C & C++ projects with little repetitive work.

There are many resources available online on these topics, we recommend starting with the following to get an overview:

* [Compiling C and C++ Programs](http://pages.cs.wisc.edu/~beechung/ref/gcc-intro.html)
* [GCC and Make: Compiling, Linking and Building C/C++ Applications](https://www3.ntu.edu.sg/home/ehchua/programming/cpp/gcc_make.html)
