# PortBackwarding
This is a program that is meant to be used between a public and private server in order to remove the need for port forwarding.

This program works by intercepting all traffic through the public server and adding it to a queue, which can be taken by the private server or multiple private servers and returns the desired output in a similar way to Flask. A fortunate
side efffect of this program is that it can be used to make a more scalable system for reading and responding to HTTP and later other types of requests.

This program does have some major security issues which I aim to repair shortly. If you notice anything in particular that should be encrypted or secured, please let me know through email or GitHub.

### Instructions

0. Installation
    0.1 install Flask on your public server (```pip install flask```)

1. You start by adding and running the public-server.py file on the server, preferrably with an Apache and Flask configuration with this file renamed to __init__.py. (Not doing this can lead to problems because the server that comes with the file is just for debugging)
