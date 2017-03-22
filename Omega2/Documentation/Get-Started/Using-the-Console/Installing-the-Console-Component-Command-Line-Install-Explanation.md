The `console-install-tool` utility automates the installation of the Console. If you would like to know what's going on behind the scenes, then this section is for you.

In the above section, we first used `uci` to set the `onion.console` configuration options and then we run the installation tool. When the `console-install-tool` is run, it will check `onion.console` configuration options to see which packages need to be installed. Based on which components are selected, it will then use `opkg` to install the specified components:

```
opkg update
opkg install console-base
```

> You can learn more about `opkg` in our [guide to opkg](#using-opkg).

After the installation is complete, the `rpcd` service needs to be restarted so the Console can have access to the system. The tool will restart the `rpcd` service with the following command:

```
/etc/init.d/rpcd restart
```
