# PortBackwarding
This is a program that is meant to be used between a public and private server in order to remove the need for port forwarding.

This program works by intercepting all traffic through the public server and adding it to a queue, which can be taken by the private server or multiple private servers and returns the desired output in a similar way to Flask. A fotunate side efffect of this program is that it can be used to make a more scalable system for reading and responding to HTTP and later other types of requests.