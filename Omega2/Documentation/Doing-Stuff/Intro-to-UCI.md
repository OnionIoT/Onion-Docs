## Intro to UCI {#intro-to-uci}

`uci` stands for Unified Configuration Interface, and it is a powerful tool for creating and managing configuration options in the Omega’s firmware. You can use `uci` to change options for subsystems such as the Omega’s WiFi AP, network connectivity, or even firewall without having to worry about:

* Making syntax errors in the configuration files which would break certain options
* Where the files are actually located

Just for reference, the configuration files live in `/etc/config` and are simple text files.

The syntax looks like this:

```
uci [OPTIONS] (COMMAND) [ARGUMENTS]
```

We will focus on the `(COMMAND)` and `[ARGUMENTS]` sections in this introduction. These are the commands we will focus on in this introduction.

* `show`
* `add`
* `set`
* `get`
* `commit`

All examples will be run on a dummy config file `/etc/config/foobar/`. If you want to follow along with the examples, create this file on your Omega:

```
touch /etc/config/foobar
```

### General Usage

`uci` generally works along this process:

1. **Stage** (temporarily store) changes to options using commands such as `uci add` or `uci set`
1. Commit the staged changes using `uci commit`

Don't forget to run `uci commit` after staging all of your changes, or the configuration will not be updated!

### `show`

Prints configuration files to the terminal.

UCI configuration details are divided into **subsystems**. Each subsystem has its own file in `/etc/config` and is split into **sections** that contain groups of **options**.

For example, let’s examine the `system` subsystem on the Omega. It contains some basic options such as the timezone, hostname (the Omega-ABCD that you see on the command line), and LED controls. the Run the following command:

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

#### Sections

When using `uci show`, sections are displayed in the following format:

```
[SUBSYSTEM].[SECTIONNAME]=[TYPE]
```

Sections can be named or unnamed. Unnamed sections replace the `SECTIONNAME` field with `@TYPE[INDEX]`, where `INDEX` is the index of where the unnamed section appears. There can be more than one unnamed section in a configuration file, and they can be the same time if you wish. 

For example, your `firewall` config can have multiple sections of the type `rule` as shown below:

```
firewall.@rule[0]=rule
firewall.@rule[0].name='Allow-ICMPv6-Input'
firewall.@rule[0].src='wan'
firewall.@rule[0].proto='icmp'
firewall.@rule[1]=rule
firewall.@rule[1].name='Allow-DHCPv6'
firewall.@rule[1].src='wan'
firewall.@rule[1].proto='udp'
...
(and so on)
```

The following lines are equivalent:

| uci | Raw (/etc/config/system) |
|-----------|-----|
| system.@system[0]=system | config system |
| system.ntp=timeserver | config timeserver 'ntp' |

Let's break down the `system.ntp=timeserver` section in more detail:

| Property | In `system.ntp=timeserver` |
|-----------|-----|
| SUBSYSTEM | system |
| SECTIONNAME | ntp |
| TYPE | timeserver |

#### Options

Otions are displayed like so:

```
[SUBSYSTEM].[SECTIONNAME].[OPTION]=[VALUE]
```

The following lines are equivalent:

| uci | Raw (/etc/config/system) |
|-----------|-----|
| system.ntp.enable_server='0' | option enable_server '0' |

Here are some examples of these fields in the raw configuration file above:

Let's break down the `system.ntp.enable_server='0'` option in more detail:

| Property | In system.ntp.enable_server='0' |
|-----------|-----|
| SUBSYSTEM | system |
| SECTIONNAME | ntp |
| OPTION | enable_server |
| VALUE | '0' |


To show the options in a configuration file, a section of a config file, or a specific option, run:

```
uci show [SUBSYSTEM].[SECTION].[OPTION]
```

You can also run just `uci show` to show all options in all of the configuration files.

### `add`

Adds an **unnamed** section to a subsystem.

```
uci add (SUBSYSTEM) (TYPE)
```

Example: 

```
root@Omega-F119:/# uci add foobar unnamedSection
cfg0258c2
root@Omega-F119:/# uci commit

root@Omega-F119:/# uci show foobar
foobar.@unnamedSection[0]=unnamedSection

root@Omega-F119:/# cat /etc/config/foobar 

config unnamedSection
```

### `set`

Adds or changes an existing option's value. Also can be used to add a named section.

To add an option:

```
uci set (SUBSYSTEM).(SECTIONNAME).(OPTION)=(VALUE)
```

To add a named section, run:

```
uci set (SUBSYSTEM).(NAME)=(TYPE)
```

**Note:** This command cannot add names to unnamed sections. Use `uci rename` instead.

Example:

```
root@Omega-F119:/# uci set foobar.sectionName='sectionType'
root@Omega-F119:/# uci set foobar.sectionName.someOption=someValue
root@Omega-F119:/# uci commit

root@Omega-F119:/# uci show foobar
foobar.@unnamedSection[0]=unnamedSection
foobar.sectionName=sectionType
foobar.sectionName.someOption='someValue'

root@Omega-F119:/# cat /etc/config/foobar 

config unnamedSection

config sectionType 'sectionName'
        option someOption 'someValue'
```

### `get`

Gets the value of an option.

```
uci set (SUBSYSTEM).(SECTIONNAME).(OPTION)=(VALUE)
```

Example:

```
root@Omega-F119:/# uci get foobar.sectionName.someOption
someValue
```

### Example - Changing the Omega's LED Pattern

Let's change the LED on the Omega from a solid amber to a blinking 'heartbeat' flash. Run the following:

```
uci set system.@led[0].trigger='heartbeat'
uci commit
```

Reboot your Omega, and once it has finished booting, the LED will be blinking in a 'thump-thump' pattern!

<!-- TODO: gif or video -->