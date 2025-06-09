from flask import Flask, request, jsonify

app = Flask(__name__)

# GET request handler
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message='Hello from Flask backend!')

# POST request handler
@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify(received=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
