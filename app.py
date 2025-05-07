from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from the backend!"})

if __name__ == '__main__':
    # Binding to the port Render expects (10000)
    app.run(host='0.0.0.0', port=10000)
