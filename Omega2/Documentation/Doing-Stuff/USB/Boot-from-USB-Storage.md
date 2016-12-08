---
title: Booting from USB Storage
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 2
---

# Booting from USB Storage

// mention that, yes, flash storage on the Omega is limited, so it is possible to have the Omega boot from attached USB storage

// include an illustration of how the omega currently works (boots from on-board flash)
// include an illustration of how it works when booting from USB storage

// base this on the existing article:
//  notes on this: find the different between pivot-root and pivot-overlay and then discuss them with Lazar, we will likely only choose one to inlcude in the article

// remember to include the important caveats:
//  - updating the firmware might affect this (test this out and see what the outcome is)
//  - when the usb storage is removed, the omega will boot from the onboard flash and all of the filesystem changes made on the usb storage device will not be transferred (test this as well to find out exactly what happens)
