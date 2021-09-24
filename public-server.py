import requests
import time
from flask import Flask, request
import encryption

queueRoute = '[ Insert the path that you would like for the queue ]' ## Replace this or the program will fail
queue = [] ## This will be used to store the requests that have not been processed
queuePassword = 'password' ## Though this code will work, we recommend changing the password here
returnRoute = '[ Insert the path that you would like for information to be returned to ]' ## Replace this or the program will not work
processing = [] ## This will store the data until the server sends the information back to the user
encrypt = False ## It is recommended that you create a key and change this according to the instructions found in README.md

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods = ['POST','GET'])
@app.route('/<path:path>', methods = ['POST','GET'])
def getPath(path):
    if path == f'{queueRoute}' and request.method == 'POST':
        if request.form['password'] == queuePassword:
            try:
                requested = queue[0]
                queue.pop(0)
            except:
                requested = ''
            if not encrypt:return requested
            else: return encryption.encrypt(requested)
        else:
            return 'incorrect queue password'
    elif (path == f'{queueRoute}' or path == f'{returnRoute}') and not request.method=='POST':
        return 'inocrrect method'
    elif path == f'{returnRoute}' and request.method == 'POST':
        output = request.form['output']
        key = int(request.form['processingKey'])
        processing[key]['output'] = output
        return 'ok'
    else:
        start = time.time()
        key = len(processing)
        form_data = {'args':request.args,'form':request.form,'files':request.files,'json':request.json}
        queue.append({
            'path':path,
            'processingKey':key,
            'data':encryption.encrypt(str(form_data))
        })
        processing.append({'path':path,'output':''})
        while time.time()-start <= 5:
            output = encryption.decrypt(processing[key]['output'])
            if output != '':
                processing[key] = int()
                return output
            else:
                continue
        return '<h1>Sorry...</h1><p>Our servers are busy right now. Please try again in a moment.</p>'
    
if __name__ == '__main__':
    app.run()
