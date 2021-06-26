import json

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/user/<id123>', methods=['POST'])
def user_register(id123):
    rtt = [0, 1, 4, 5, 6, 8, 9]
    id123 = id123.split('-')[-1]
    a3343 = [True if int(x) in rtt else False for x in id123]
    print(a3343)
    if False not in a3343:
        print(json.loads(request.data))
        d = jsonify({'status': 'ok'})
        d.headers.add("Access-Control-Allow-Origin", "*")
        return d
    else:
        d = jsonify({'status': 'fail'})
        d.headers.add("Access-Control-Allow-Origin", "*")
        return d


if __name__ == "__main__":
    app.run()
