SETUP Development Environment

Prerequests:
Java 7 runtime
Eclipse Kepler
Python 2.7

>>> Create a directory for development and add environment variable DEVEL_PATH to .profile set it to the develoment directory

>>> Clone this project (potato) and potato_env to your development directory

>>> Install lxml
sudo apt-get install libxml2-dev libxslt1-dev python-dev
sudo apt-get install python-lxml

>>> Download Google AppEngine SDK for Python
https://developers.google.com/appengine/downloads

>>> Unzip and copy the SDK to a folder

>>> Install PyDev for eclipse
http://pydev.org/updates/
NOTE: latest PyDev requires java runtime 7

>>> Install Google AppEngine Eclipse plugin
https://developers.google.com/eclipse/docs/getting_started

>>> Setup a python runtime for your eclipse workspace
Windows -> Preferences -> PyDev -> Interpreters -> Python Interpreter -> Quick Auto Config
Rename it to "potato_env" (double click on the name to rename)

Add String Substitution Variables:
Variable: DEVEL_PATH
Value   : <path-to-your-development-directory>

Add String Substitution Variables:
Variable: GOOGLE_APP_ENGINE
Value   : "${DEVEL_PATH}/potato_env/local/google_appengine"

>>> Import project
