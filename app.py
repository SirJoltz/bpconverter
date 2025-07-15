from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows frontend to call backend from a different domain

@app.route("/")
def index():
    return send_file("index.html")

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    xml_code = data.get('xmlCode', '')

    # TODO: Replace this with your actual transformation logic
    pad_code = f"// Mock PAD code\n// Received {len(xml_code)} characters of XML"

    return jsonify({'padCode': pad_code})

if __name__ == '__main__':
    app.run(debug=True)