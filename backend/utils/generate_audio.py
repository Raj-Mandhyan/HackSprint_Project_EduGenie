from gtts import gTTS
import os, uuid

def generate_audio(text):
    os.makedirs("backend/static", exist_ok=True)
    filename = f"audio_{uuid.uuid4().hex}.mp3"
    path = os.path.join("backend/static", filename)
    gTTS(text).save(path)
    return filename
