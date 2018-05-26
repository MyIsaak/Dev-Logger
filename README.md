# Introduction

DevLogger is the fastest command line tool for anyone that wants to update their daily log on Twitter and GitHub: In addition it takes screenshots and is super easy and simple to use from the terminal.

### How to use:

Usage: `python main.py [-h] [--append] [--offline] [--text] message`

If you need more detailed information just type `python main.py -h`

# Development

It is under early development and requires the following dependencies:

- gitpython
- twitter
- mss

Which can be installed using `sudo pip install gitpython twitter mss`

# Installation

In order to run the script you need to set up a settings.json file. It contains your password and username for Twitter and other sensitive information.

An example `settings.json` file:

```
{
	"username":"user",
	"password":"pass",
	"logpath":"log.md",
	"email": "isaak.eriksson@gmail.com",
	"repo": "url",
	"gallery", "screenshots",
	"reponame": "DevLogger",
	"gallery": "screenshots/"
}
```
