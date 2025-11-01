from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_text(subject, topic, difficulty):
    prompt = f"""
    You are an AI teacher. Generate a {difficulty}-level explanation and one practice question
    on the topic "{topic}" under the subject {subject}.
    End with a short summary in bullet points.
    """
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content.strip()
