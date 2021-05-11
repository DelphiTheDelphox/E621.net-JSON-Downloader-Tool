# E621.net-JSON-Downloader-Tool
A tool designed to download metadata as JSON files from e621.net

Welcome to my E621.net json downloader tool.
The purpose of this is to aid in downloading the metadata of images downloaded from e621.net.
For use of directories with images, even in large quantities.
This software is designed to pick up where it left off. 
It saves its queue position every 100 entries by default.
On average you should add 1 second for each image added to the queue.

To use you must have 3 things, a directory with properly named images, a valid E621.net account, and an account with an active API Key.

How to format the image folder:
    Most E621 downloaders will supply images already in the correct format.
    The correct format is <ID Number>.<File Extension> ex. 560858.jpg.
    Images not in this format will not work.
    No other files should be in the folder.

Account and API Key:
    I'll assume that anyone still interested at this point probably has this set up already.
    However, if you do not, you must first go to your account screen, go to Manage API access, and then generate a new key.

This tool supplies you with the raw JSON data.
The data is useful for many things and I plan to add support for more human readable formats and strip out all the junk.



Warnings:
This tool operates relatively slowly, to comply with API rules.
Do not change the wait time value to be any lower, it is set to allow for 1 second gaps between requests

Do not impersonate a web browser User-Agent, as this is against the rules and will get you banned.
If you plan to use your own user agent, include your username in case the admins need to message you.

I am not responsible for any damage this may do to your machine.
Do not use in a nuclear power plant.

Apache License 2.0

delphithedelphox 2021
