api-fiddler
===========

This application is capable of generating random JSON data to help accelerate the development of front-end Web Apps and Mobile Apps.

Project Description
===================

Usually the development of front-end Web Apps and Mobile Apps will begin after the backend that serves data is ready. However, through this application, developers can get proxy data to build the User Interface and then link to their backend service once it is ready.

Features
========

Current features include weather and stocks. It is setup to generate random strings and integers using a random-generator. It also has a parser to generate JSON data.
More features can be added on demand. Suggestions are welcome! 

Prerequesites
=============

Python 3
PyYAML - pyyaml.org

How to Run
==========

Clone the repository on your LOCAL machine (not the ECE2524 VM)
For Windows users running PuttY, download github for Windows and clone the repository and use python3
Install PyYAML - Instructions given below
Go into the cloned directory, and run ./server.py
Launch your browser and go to http://localhost:8080/weather or http://localhost:8080/stocks
Modify the outline.yaml file to add more request functionalities (only integer and string are currently supported)

Support
=======

To Install PyYAML
=================

Download the zip file of latest version from PyYAML (pyyaml.org). Windows users use the installer.
Unzip it and run the command: python3 setup.py install
