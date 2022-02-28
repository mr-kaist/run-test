from flask import Flask, request, make_response

import json

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def echo():
    resp = {
        "args": {},
        "headers": {},
        "body": None
    }

    for k, v in request.args.items():
        resp["args"][k] = v
    
    for k, v in request.headers.items():
        resp["headers"][k] = v

    resp["body"] = request.data.decode("utf-8")

    return make_response(resp)
    #약간의 수정


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True, threaded=True)