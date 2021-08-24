import requests
import time
from flask import Flask, requets

queueRoute = '[ Insert the path that you would like for the queue ]' ## Replace this or the program will fail
queue = [] ## This will be used to store the requests that have not been tended to
queuePassword = 'password' ## Though this code will work, we recommend changing the password here

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def getPath(path):
    if path == f'{queueRoute}' and request.method == 'POST':
        if request.form['password'] == queuePassword:
            requested = queue[0]
            return requested
        else:
            return 'incorrect queue password'
    elif path == f'{queueRoute}' and not request.method=='GET':
        return 'inocrrect method'
    else:
        start = time.time()
        key = len(queue)
        queue.append({'path':path,'key':key})
        while time.time()-start <= 5:
            output = queue[key]['output']
            if output != '':
                return output
            else:
                continue
        return '<h1>Sorry...</h1><p>Our servers are busy right now. Please try again in a moment.</p>'
    

if __name__ == '__main__':
    app.run()