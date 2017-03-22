The Console can be installed using the Omega's command line.

>For information on how to access the Omega's command line, follow this [guide to connecting to the Omega's Terminal](#connecting-to-the-omega-terminal)


>You'll need to be connected to the internet in order to install the Console. If you've followed the Setup Wizard, you will be all good to go.

With your terminal open, run the following commands:

```
uci set onion.console.setup=1
uci set onion.console.install=1
uci commit onion
console-install-tool
```

This will perform the entire Console installation sequence for you.
