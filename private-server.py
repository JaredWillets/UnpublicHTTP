import requests
import time
import routing
import json
import encryption

encrypt = False ## It is recommended to change this to true and add the keys according to the instructions in README.md
queuePassword = 'password' ## Recommended to be changed (must match the public server password)
publicServerAddress = '[insert your public server address here]' ## Must be changeed for the code to function properly
queuePath = "queue" ## It is recommended to change this (make sure to change it it in the public-server.py file)
returnPath = 'return' ## Same as the line above

while True:
    
    try:
        requestGiven = requests.post(publicServerAddress+queuePath, data={'password':'password'}).text
        if encrypt:
            requestGiven = encryption.decrypt(requestGiven)
        command = json.loads(requestGiven)
        output = routing.run(command['path'])
        response = requests.post(publicServerAddress+returnPath, data = {'output':output,'processingKey':command['processingKey']}).text
        if response != 'ok':
            print('Objective from the queue was not handled correctly')
        else:
            continue

    except Exception as e:        
        time.sleep(1)