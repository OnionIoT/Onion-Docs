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
