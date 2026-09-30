import os
import json
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_outline(story_prompt):
    prompt = f"""
Create a structured 5-panel comic outline for this story:

{story_prompt}

Return ONLY valid JSON in this format:

[
  {{
    "panel": 1,
    "title": "Panel title",
    "scene": "Scene description",
    "image_prompt": "Detailed image generation prompt"
  }}
]

Create exactly 5 panels.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return json.loads(response.text)