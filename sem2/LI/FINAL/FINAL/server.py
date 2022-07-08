from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Rota de teste que recebe dados em JSON e envia de volta
@app.route("/test", methods=['POST'])
def test():
    received = request.json
    return jsonify(received)

# Segunda rota de teste que soma dois números
@app.route("/sum", methods=['POST'])
def sum():
    received = request.json
    return jsonify({'result': received['a'] + received['b']})

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=8080, debug=True)