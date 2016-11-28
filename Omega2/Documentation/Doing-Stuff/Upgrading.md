---
title: Updating the Omega
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 8
---

# Updating the Omega

In order to keep improving user experience for Omega, we will be releasing updated firmwares on a rolling basis. To capitalize on these improvements users should update their Omegas to the latest firmware release. To handle firmware transitions we have created a command-line utility 'oupgrade'.

## Using the Command line

To get the current firwmare installed on the device:
```
oupgrade -v
```

Upgrade to the latest repo version(instead of stable version):
```
oupgrade -l
```

Force the upgrade, regardless of version:
```
oupgrade -f
```

Compare installed firmware and available firmware versions:
```
oupgrade -c
```

## Notes On Upgrades

When an upgrade is performed, only the root and etc folders are preserved. So it is important to backup your work on the Omega prior to upgrading. 
