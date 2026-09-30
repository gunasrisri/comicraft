import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_story(outline):
    prompt = f"""
You are a comic story writer.

Convert the following 5-panel comic outline into a complete comic-style story.

For every panel include:
- Narration
- Character dialogue

Keep the story engaging and easy to understand.

Comic outline:
{outline}
"""

    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=prompt
    )

    return response.text