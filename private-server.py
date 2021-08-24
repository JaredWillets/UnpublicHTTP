import requests
import time
import routing
import json

publicServerAddress = '[insert your public server address here]'

while True:

    command = json.load(requests.post(publicServerAddress).text)
    output = routing.run(command)
    response = requests.post(publicServerAddress, data = output).text
    if response != 'ok':

        print('process not handled correctly')

    else:
        
        continue