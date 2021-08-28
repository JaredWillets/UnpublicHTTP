# UnpublicHTTP

**NOT FOR PRODUCTION USE, YET**

This is a program that is meant to be used between a public and private server in order to remove the need for port forwarding.

This program works by intercepting all traffic through the public server and adding it to a queue, which can be taken by the private server or multiple private servers and returns the desired output in a similar way to Flask. A fortunate
side efffect of this program is that it can be used to make a more scalable system for reading and responding to HTTP and later other types of requests.

This program does have some major security issues which I aim to repair shortly. If you notice anything in particular that should be encrypted or secured, please let me know through email or GitHub.

## **Instructions**

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
## **Encryption**
1. Ensure that you have the Python RSA module installed on both the public and private servers (```pip install rsa```)
2. Ensure that encryption.py file is in the same directory as both public-server.py on the public server and private-server.py on the private server. 
3. Use the key generator by running key_maker.py
4. It is preffered that you use a power of two as the number of bits in your encryption when generating the keys. It is also recommended to bring the number of bits as high as possible.
5. Add the public and private keys (PubKey,PrivKey) files to both of the directories of your servers.  
6. Only now should you change the variables in the code of public-server.py and private-server.py so that ```encrypt = True```
7. IT IS HIGHLY RECOMMENDED THAT YOU USE ENCRYPTION, ESPECIALLY WHEN PEOPLE'S DATA IS BEGIN SENT THROUGH HERE!

## **DISCLAIMER**

I am not responsible for data loss, theft, or any other consequences of using this code on a machine that is not owned by me. I do not recommend using this is a production environment. If you choose to do so, you do so at your own risk. With that being said, I would like to know if this causes problems so that I can create a better program to contribute to this great community.