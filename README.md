# UnpublicHTTP
This is a program that is meant to be used between a public and private server in order to remove the need for port forwarding.

This program works by intercepting all traffic through the public server and adding it to a queue, which can be taken by the private server or multiple private servers and returns the desired output in a similar way to Flask. A fortunate
side efffect of this program is that it can be used to make a more scalable system for reading and responding to HTTP and later other types of requests.

This program does have some major security issues which I aim to repair shortly. If you notice anything in particular that should be encrypted or secured, please let me know through email or GitHub.

### Instructions

1. Installation

    1.1 install Flask on your public server (```pip install flask```)
    1.2 Ensure that you have the json, requests, and time Python modules installed.

2. You start by adding public-server.py file on the public server, preferrably with an Apache and Flask configuration with this file renamed to __init__.py. (Not doing this can lead to problems because the server that comes with the file is just for debugging).

3. Add the routing.py and private-server.py files to the private server in the same directory.

4. Insert the values that it says to replace in the comments in the code for all of these files.

5. Add websites and paths to the routing.py to be returned to the user.

6. Run public-server.py and private-server.py, preferrably starting with publilc-server.py, though it should not matter to a great extent.

7. Try things out, experiment, and enjoy! Please, truly, absolutely, contact me at willetsjared@gmail.com or on GitHub if you need anything with this. I know that this is a work in progress and the code is not that great and I am open to criticism and suggestions. Seriously, I have thick skin.

8. Keep in mind that this is a project that was just started less than a week ago and needs large amounts of revision, more updates are coming soon to fix the issues. If you see something major that does not work in this, let me know.