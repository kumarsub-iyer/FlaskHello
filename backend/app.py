# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS so your React dev server can securely talk to this API
CORS(app) 

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({
        "message": "Hello from the Flask backend!",
        "status": "success"
    })

if __name__ == '__main__':
    app.run(port=5001, debug=True)