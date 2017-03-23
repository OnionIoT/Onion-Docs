## Installing Software {#starter-kit-intro-installing-software}

<!-- // DONE: intro:
//	* we'll need to install some additional software on the Omega to make sure that all of the code we write for our experiments will work
//	* to do that, we'll use `opkg`, the Omega's package Manager -->

We'll need to install some additional software on the Omega so that all of the code we write for our experiments can run. To do this, we'll use the `opkg` utility.

### What is OPKG?

<!-- // DONE: brief description of `opkg`
//	* explain the concept of linux package managers and software packages
//	* the omega's package manager is `opkg`, -->

Not everything available for the Omega is installed right away. Some people may never need certain utilities, so we configured the Omega to ship only with common packages you will likely use. We then made additional software available online that you can use to further tailor your Omega to suit your needs. This is done using the **package manager** on the Omega, `opkg`.

A package manager, well, manages software packages. It lets you run short, consistent commands to find, download, and install all kinds of software from the Internet. It also keeps track of what versions of programs that you have installed and can be used to update software directly from the command line.

There are package managers for other Linux systems such as `apt-get` and `yum`.

### Installing the Required Packages

<!-- // TODO: outline the commands we'll need to run to install the required software:
//	opkg update
//	opkg install <packages>
// -> you'll have to look through the experiments to see which packages we need, sync up with Lazar when you're done

// show the expected output -->

To install the packages we need for our experiments, run the following commands on the Omega:

```
opkg update
opkg install python-light pyOnionGpio pyOnionI2C
```

You should see something like the following:

```
root@Omega-ABCD:/# opkg update
Downloading http://repo.onion.io/omega2/packages/core/Packages.gz
Updated list of available packages in /var/opkg-lists/omega2_core
Downloading http://repo.onion.io/omega2/packages/core/Packages.sig
Signature check passed.
Downloading http://repo.onion.io/omega2/packages/base/Packages.gz
Updated list of available packages in /var/opkg-lists/omega2_base
Downloading http://repo.onion.io/omega2/packages/base/Packages.sig
Signature check passed.
...
(downloading more package lists)
...
root@Omega-ABCD:/# opkg install python-light pyOnionGpio pyOnionI2C
Installing python-light (2.7.13-4) to root...
Downloading http://repo.onion.io/omega2/packages/packages/python-light_2.7.13-4_mipsel_24kc.ipk
Installing python-base (2.7.13-4) to root...
Downloading http://repo.onion.io/omega2/packages/packages/python-base_2.7.13-4_mipsel_24kc.ipk
Installing libffi (3.2.1-2) to root...
Downloading http://repo.onion.io/omega2/packages/packages/libffi_3.2.1-2_mipsel_24kc.ipk
...
(downloading and installing more packages)
...
Configuring python-base.
Configuring pyOmegaExpansion.
Configuring pyOnionI2C.
Configuring libffi.
Configuring libbz2.
Configuring python-light.
Configuring pyOnionGpio.
```

If you see something like this, you're good to go!

### Doing More with OPKG

<!-- // DONE: opkg can do a lot more, link them to the opkg article in our Docs (https://docs.onion.io/omega2-docs/using-opkg.html) -->

`opkg` can do a lot more! For full details, take a look at our [`opkg` Guide](https://docs.onion.io/omega2-docs/using-opkg.html).
