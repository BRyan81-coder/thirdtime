from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    filename = data.get('filename', 'unknown')
    content = data.get('content', '')

    # Mock summary based on file type or content length
    summary = {
        "filename": filename,
        "content_length": len(content),
        "summary": f"Received file '{filename}' with {len(content)} characters of content."
    }

    return jsonify(summary)

if __name__ == '__main__':
    app.run(debug=True)
