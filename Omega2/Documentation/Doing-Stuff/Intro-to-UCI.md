## Intro to UCI {#intro-to-uci}

`uci` stands for Unified Configuration Interface, and it is a powerful tool for creating and managing configuration options in the Omega’s firmware. You can use `uci` to change options for subsystems such as the Omega’s WiFi AP, network connectivity, or even firewall without having to worry about:

* Making syntax errors in the configuration files which would break certain options
* Where the files are actually located

Just for reference, the configuration files live in `/etc/config` and are simple text files.

The syntax looks like this:

```
uci [OPTIONS] (COMMAND) [ARGUMENTS]
```

We will focus on the `(COMMAND)` and `[ARGUMENTS]` sections in this introduction. Some of the most used commands are:

* `show`
* `add`
* `get`
* `set`
* `commit`

### `show` - Examine Configuration Files

Let’s use one of the subsystems on the Omega, `system`, as an example. Run the following command:

```
uci show system
```

You’ll get something like:

```
system.@system[0]=system
system.@system[0].timezone='GMT0'
system.@system[0].ttylogin='0'
system.@system[0].log_size='64'
system.@system[0].urandom_seed='0'
system.@system[0].cronloglevel='8'
system.@system[0].hostname='Omega-F119'
system.ntp=timeserver
system.ntp.enabled='1'
system.ntp.enable_server='0'
system.ntp.server='0.lede.pool.ntp.org' '1.lede.pool.ntp.org' '2.lede.pool.ntp.org' '3.lede.pool.ntp.org'
system.@led[0]=led
system.@led[0].name='On'
system.@led[0].default='0'
system.@led[0].trigger='default-on'
system.@led[0].sysfs='omega2p:amber:system'
```


Let’s compare this to the raw file. Run:

```
cat /etc/config/system
```

And you’ll get something like this:

```
config system
        option timezone 'GMT0'
        option ttylogin '0'
        option log_size '64'
        option urandom_seed '0'
        option cronloglevel '8'
        option hostname 'Omega-F119'

config timeserver 'ntp'
        option enabled '1'
        option enable_server '0'
        list server '0.lede.pool.ntp.org'
        list server '1.lede.pool.ntp.org'
        list server '2.lede.pool.ntp.org'
        list server '3.lede.pool.ntp.org'

config led
        option name 'On'
        option default '0'
        option trigger 'default-on'
        option sysfs 'omega2p:amber:system'

```

The above file may seem organized enough. However, if you were to edit it and make a typo or mistake, you could cause bugs or crashes in any programs that depend on it, especially at boot time!

These configuration details are divided into **subsystems**. Each subsystem has its own file in `/etc/config` and is split into **sections** that contain groups of **options**.

#### Sections

When working with `uci`, sections are displayed in the following syntax:

```
[SUBSYSTEM].[SECTIONNAME]=[TYPE]
```

Sections can be named or unnamed. Unnamed sections take on the syntax `@SECTIONTYPE=SECTIONTYPE`.

and options are displayed like so:

```
[subsystem].[section].[option]=[value]
```

Here are some examples of these fields in the raw configuration file above:

* `subsystem` - `system` from the `system` file in `/etc/config`
    * Not to be confused with the `system` in `config system`; this is named for convenience.
* `section` - the `ntp` in `config timeserver 'ntp'`
* `type` - the `timeserver` in `config timeserver 'ntp'`
* `option` - the `trigger` in `option trigger 'default-on'`
* `value` - the `Omega-F119` in `option hostname 'Omega-F119'`

To show the options in a configuration file, a section of a config file, or a specific option, run:

```
uci show [SUBSYSTEM].[SECTION].[OPTION]
```

You can also run just `uci show` to show all options in all of the configuration files.

### `add` - Add Section to Config File

To add a section to a subsystem, run:

```
uci add (SECTION) (SUBSYTEM)
```

### `set` - Add or Change Option

To add or change an existing option, run:

```
uci set (SUBSYSTEM) (SECTION).[OPTION]
```

#### Example - Changing the Omega's LED Trigger

