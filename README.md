# DevLogger

> A simpler faster way to log your development process that tweets and pushes commits with screenshots

![example screenshot](https://github.com/MyIsaak/DevLogger/blob/master/2018-01-01.png?raw=true)

## Introduction

DevLogger is a command line tool for anyone that wants to update their daily log on Twitter and GitHub: In addition it takes screenshots and is super easy and simple to use from the terminal.

## How to use:

Usage: `python main.py [-h] [--append] [--offline] [--text] message`

If you need more detailed information just enter tha following in the terminal: `python main.py -h`

## Development

It is under early development and requires the following dependencies:

- gitpython
- twitter
- mss

Which can be installed using `sudo pip install gitpython twitter mss`

## Installation

In order to run the script you need to set up a settings.json file. It contains your password and username for Twitter and other sensitive information.

An example `settings.json` file:

```
{
	"username":"user", // Your Twitter username
	"password":"pass", // Your Twitter password
	"logpath":"log.md",// The devlog file location relative to base repo dir
	"email": "isaak.eriksson@gmail.com", // Your GitHub email
	"repo": "url", // Your Github repo url
	"gallery", "screenshots/", // Folder to store screenshots
	"reponame": "DevLogger", // Name of GitHub repo
}
```
