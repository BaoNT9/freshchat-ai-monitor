"""
Simple CORS Proxy for Freshchat AI Monitor
Run this locally to bypass CORS issues
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

AGENT_API = 'https://endpoint-99e957ab-e868-4cb9-a88f-c8f6ac525f1a.agentbase-runtime.aiplatform.vngcloud.vn/invocations'

@app.route('/', methods=['POST'])
def proxy():
    try:
        data = request.json
        response = requests.post(AGENT_API, json=data, timeout=30)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    print("Proxy running at http://localhost:5000")
    app.run(port=5000, host='0.0.0.0')