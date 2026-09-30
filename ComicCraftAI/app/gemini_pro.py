from .image_generator import generate_image
from .image_generator import generate_images
import json

from google import genai
from google.genai import types

from .config import (
    GEMINI_API_KEY,
    GEMINI_STORY_MODEL,
    require_gemini
)


# --------------------------------------------------
# Gemini client
# --------------------------------------------------

def get_client():

    require_gemini()

    return genai.Client(
        api_key=GEMINI_API_KEY
    )


# --------------------------------------------------
# JSON parser
# --------------------------------------------------

def extract_json(text: str):

    text = (text or "").strip()

    if text.startswith("```"):

        parts = text.split("\n", 1)

        if len(parts) == 2:
            text = parts[1]

        if "```" in text:
            text = text.rsplit(
                "```",
                1
            )[0]

    return json.loads(text)


# --------------------------------------------------
# Generate story
# --------------------------------------------------

def generate_story(
    outline,
    character_name,
    tone
):

    prompt = f"""
You are an expert comic-book writer.

Expand the following comic outline into
complete narration and dialogue.

Main character:
{character_name}

Tone:
{tone}

Comic outline:
{json.dumps(
    outline,
    ensure_ascii=False,
    indent=2
)}

Return ONLY valid JSON.

Use this structure:

{{
    "panels": [
        {{
            "panel_number": 1,
            "caption": "short caption",
            "narration": "1-3 concise sentences",
            "dialogue": "short character dialogue"
        }}
    ]
}}

Rules:

1. Do not create extra panels.
2. Preserve the events in the outline.
3. Keep the character consistent.
4. Dialogue should be short and natural.
5. Narration should be easy to read.
6. Make the story flow naturally from panel to panel.
7. Do not use markdown.
"""

    client = get_client()

    response = client.models.generate_content(
        model=GEMINI_STORY_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.8,
            max_output_tokens=5000
        )
    )

    return extract_json(
        response.text
    )