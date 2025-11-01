from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_image(topic):
    prompt = f"Educational diagram explaining {topic}."
    result = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="512x512"
    )
    return result.data[0].url
