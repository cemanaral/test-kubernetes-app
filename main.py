import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! v11'

@app.route('/health')
def health():
    return 'App is healthy.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
