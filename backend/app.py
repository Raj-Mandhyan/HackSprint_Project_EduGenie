from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.generate_text import generate_text
from utils.generate_image import generate_image
from utils.generate_audio import generate_audio

app = Flask(__name__)
CORS(app)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    subject = data.get('subject')
    topic = data.get('topic')
    difficulty = data.get('difficulty')
    output_type = data.get('output_type')

    text_output = generate_text(subject, topic, difficulty)
    response = {"text": text_output}

    if "image" in output_type:
        response["image_url"] = generate_image(topic)
    if "audio" in output_type:
        response["audio_file"] = generate_audio(text_output)

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
