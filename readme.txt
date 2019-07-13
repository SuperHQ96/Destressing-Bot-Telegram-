1) Destressing Bot:
Within the 'Destressing Bot' folder, there are four python files as well as one excel file.

Destressingbot.py - This is the main body of the program and the other python files are imported to be used here.
Funnyscraper.py - This is the code to web scrape for either pictures or videos from 9gag.com
Gamescraper.py - This is the code to web scrape for a mini-game from html5games.com
Musicscraper.py - This is the code to web scrape for music from SoundCloud

helplines.xlsx - This is the list of helpline numbers which the program reads from using the xlrd module

2) Heroku Scripts:

Destressing-bot folder - Contains the files as described in section (1) above. *Take note that the only difference is that the main program reads the 
helpline numbers from the excel file for the Destressing Bot folder while the helpline numbers are hardcoded into the main program for the heroku program.

Procfile - Informs Heroku which programming language the program is using and which file contains the main program.

Requirements.txt - Informs Heroku which modules needs to be pip installed in order for the main program to run.