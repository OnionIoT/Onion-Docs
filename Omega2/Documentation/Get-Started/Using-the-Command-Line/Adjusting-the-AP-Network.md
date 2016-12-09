## Adjusting the AP Network Through the Command-Line {adjusting-ap-network-through-command-line}


The Omega's AP Network settings, such as the SSID, the password and more, can be modified through the command-line by using the `uci` command. The following command will show you the wireless configuration settings, and each of the option names:

```
uci show wireless
```

To change the AP Network settings we will change any of these three options:

```
wireless.@wifi-iface[0].ssid='Omega-2757'
wireless.@wifi-iface[0].key='12345678'
wireless.@wifi-iface[0].encryption='psk2'
```

By editing the values in this section you can modify your Omega's AP network settings.

| Option | What it changes |
| --- | --- |
| SSID | The Omega's AP network name |
| Encryption | The Encryption type of the AP network  |
| Key | The password of the AP network |

The syntax for editing one of these options is as follows:

```
uci set wireless.@wifi-iface[0].<OPTION NAME>=<VALUE>
```

Here's what editing the SSID of my Omega's AP network would look like:

```
uci set wireless.@wifi-iface[0].ssid=MyCoolOmega
```

Now that we've modified the setting, we need to save the changes using the following command:

```
uci commit wireless
```

We'll need to restart the wireless adapter in order to apply the saved changes:

```
/etc/init.d/wireless restart
```

<!-- Which method should be alternative, if any -->
### Alternative Method: Editing the Configuration File to Adjust the AP Network
You can also adjust the AP network through the command-line by directly editing the wireless configuration file located in `/etc/config/`. To view the contents of this file enter the following command:

```
cat /etc/config/wireless
```

and you'll see something similar to the following as output:

```
config wifi-device 'ra0'
        option type 'ralink'
        option mode '9'
        option channel 'auto'
        option txpower '100'
        option ht '20'
        option country 'US'
        option disabled '0'

config wifi-iface
        option device 'ra0'
        option network 'wlan'
        option mode 'ap'
        option encryption 'psk2'
        option key '12345678'
        option ssid 'Omega-2757'
        option ApCliAuthMode 'WPA2PSK'
        option ApCliEncrypType 'AES'
        option ApAuthMode 'WPA2PSK'
        option ApCliEnable '1'
        option ApCliSsid 'OnionWiFi'
        option ApCliPassWord 'ultrasecretsecurepassword'

config wifi-config
        option ssid 'OnionWiFi'
        option encryption 'WPA2PSK'
        option key 'ultrasecretsecurepassword'
```


The block of code that handles the AP Network settings is located in this section:

```
config wifi-iface
        option device 'ra0'
        option network 'wlan'
        option mode 'ap'
        option encryption 'psk2'
        option key '12345678'
        option ssid 'Omega-2757'
```

The file can be edited using the `vi` command:

```
vi /etc/config/wireless
```

Once you're happy with your changes, save and exit the file, and run the following command to restart the wireless adapter and apply the changes:

```
/etc/init.d/wireless restart
```
