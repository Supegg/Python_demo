from flask import Flask
from flask_jsonrpc import JSONRPC

# Flask application
app = Flask(__name__)

# Flask-JSONRPC
jsonrpc = JSONRPC(app, '/api', enable_web_browsable_api=True)

@jsonrpc.method('App.hello')
def hello(s='world'):
    return f'Hello {s}, welcome to Flask JSON-RPC'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)


'''
https://github.com/cenobites/flask-jsonrpc
'''