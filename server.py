# server.py
import os
import time
import json

from flask import Flask, request, session
from flask_cors import CORS
from datetime import timedelta

def create_app():
    app = Flask(__name__)
    app.secret_key = 'any random string'
    return app

app = create_app()
CORS(app)

@app.before_request
def before_request():
    # session.permanent = True
    # app.permanent_session_lifetime = timedelta(minutes=30)
    print(app.name)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/function0", methods=['GET', 'POST'])
def function0():
    result_dict = {'msg': '...'}
    try:
        if request.method == 'POST':
            if 'files' in request.files:
                received_files = request.files['files']
            if 'val' in request.form:   # ImmutableMultiDict([('val', 'blahblah')])
                received_val = request.form['val']
            
        else:
            result_dict.update({'msg': 'Request must be POST.'})
        #
        return json.dumps(result_dict, ensure_ascii=False).encode('utf8')
    except Exception as ex:
        print(str(ex))
        result_dict.update({'msg': ''})
        return json.dumps(result_dict, ensure_ascii=False).encode('utf8')
  

if __name__ == '__main__':
    app.run()
