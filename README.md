# NPR Podcasts Downloader

LICENSE: [CC By SA](https://creativecommons.org/licenses/by-sa/4.0/legalcode) [in Plain Text](
https://creativecommons.org/licenses/by-sa/4.0/legalcode.txt)

## Why

* Named after snakes who swim on top of the water.
* Running out the door w/the latest news and swimming laps w/an mp3 player.
* [Sponsor me on github](https://github.com/sponsors/alexreich).

## Features

A basic python script that downloads the latest podcasts from NPR feeds. Can be added to the chron on Linux or Task Scheduler on Windows to download the news at a set time without user intervention. This script was designed for a radio station so the news can be downloaded automatically through the Windows Task Scheduler and then imported into the playlist all without user intervention, so listeners can be informed of the news 10 minutes after the hour - every hour.
## Dependencies
The script requires python and the following python libraries: requests, bs4, and lxml. In order to install the dependencies, open a terminal in the directory where the NPR News Downloader is installed and run the following commands
```pip install requests```
```pip install bs4```
```pip install lxml```

## Executing the Script
After installing the required dependencies required to run the script, simply run ```python nprnewsdownload.py```. A batch script for Windows and shell script for Linux have been provided for your convenience. These scripts can also be used to help add the program to the chron or Windows Task Scheduler, so the News Can be downloaded with at a set time without user intervention. This is perfect for radio stations.
