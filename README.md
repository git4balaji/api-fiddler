api-fiddler
===========

This application is capable of generating random JSON data to help accelerate the development of front-end Web Apps and Mobile Apps.

Project Description
===================

Usually the development of front-end Web Apps and Mobile Apps will begin after the backend that serves data is ready. However, through this application, developers can get proxy data to build the User Interface and then link to their backend service once it is ready.

UNIX Philosophy
===============

Interface Pattern
-----------------

This project follows the MVC interface pattern. The Model is kept seperated in randomgen.py. There is no view generated except raw JSON string. The Controller handles the requests and interacts with the parser.

Rule of Silence
---------------

The bash shell acts as a log for the requests that are recieved and the response to those requests. Nothing else is thrown out throught the shell. The web browser simple recieves the data from the request if the request is valid. Otherwise, it gives a 404 Not Found Error.

Rule of Representation
----------------------

Some parts of the program need to refactored to avoid repition, especially in server.py file. In addition, functionality can be added to read from multiple YAML files rather than the fixed outline.yaml file. Also, Controller can be designed better to handle requests.

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
Launch your browser and go to http://localhost:8080 for further instructions
You can stop the server anytime by pressing Ctrl C

Support
=======

To Install PyYAML
=================

Download the zip file of latest version from PyYAML (pyyaml.org). Windows users use the installer.
Unzip it and run the command: python3 setup.py install
