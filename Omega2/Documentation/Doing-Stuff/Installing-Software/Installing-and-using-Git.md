---
title: Using Git
layout: guide.hbs
columns: two
devices: [ Omega2 ]
order: 2
---

# Installing and Using Git

// brief intro to Git and version control

Git is a popular [version control](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control) system that allows coders to track changes to their codebase, easily collaborate with others, and manage their project.

Git is the version control system used by [GitHub](https://github.com/), the super popular online web-based repository hosting service. The team at Onion uses GitHub exclusively for all of our version control needs. 

## Installing Git

// steps on using opkg to install Git
It's really easy to install Git on your Omega2/Omega2+ using OPKG. For a tutorial on how OPKG works, click [here](THE.LINK.TO.OPKG.ARTICLE)
1. First, make sure you have an internet connection

2. Run the command `opkg update`
	*After opkg updates, run `opkg install git git-http`

3. If git is successfully installed you'll see
```
Configuring git.
Configuring git-http.
```
If your installation fails, make sure you're connected to the internet and that you've updated opkg.
	* To check if you've got an internet connection run `ping www.google.com

4. To check if you have git already installed type `opkg list-installed | grep git`
	* The desired output is 
	```
	git - <version number>
	git-http - <version number>
	```

Congratulations you've successfuly installed Git on your Omega.


## Using Git

// brief steps using git on the omega to download projects from github
With Git installed on your Omega you can now clone repositories directly into your Omega just like you would on your computer. This is especially useful to try out some of the cool projects we have on our [GitHub](https://github.com/OnionIoT/)

// exalt the virtues of github and collaborative projects and how much onion loves this stuff
GitHub allows us as developers to collaborate with the community in various ways. If you've worked on something for the Omega that you would like to share with the community, you can submit a pull request. This allows us at Onion to see your work and potentially incorporate it into the official OnionIoT GitHub!