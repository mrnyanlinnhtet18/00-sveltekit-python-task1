from flask import Flask, request, jsonify
from language_detector import detect_language
from flask_cors import CORS  

app = Flask(__name__)
CORS(app)

@app.route('/api/post', methods=['POST'])
async def language_detect_post():
    if request.content_type == 'application/json':
     req_data = request.get_json()
     languageInput = req_data['inputText']
     language = detect_language(languageInput)
     response = {
        "language":language
     }
     return jsonify(response)
    else:
        return 'Unsupported Media Type', 415

if __name__ == '__main__':
    app.run(debug=True)