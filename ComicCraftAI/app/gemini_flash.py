import json

from google import genai
from google.genai import types

from .config import (
    GEMINI_API_KEY,
    GEMINI_OUTLINE_MODEL,
    PANEL_COUNT,
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
# Extract JSON
# --------------------------------------------------

def extract_json(text: str):

    text = (text or "").strip()

    # Remove markdown code fences
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
# Generate comic outline
# --------------------------------------------------

def generate_outline(
    story_prompt,
    character_name,
    setting,
    tone,
    art_style
):

    prompt = f"""
You are an expert comic-book story planner.

Create a coherent {PANEL_COUNT}-panel comic outline.

Story idea:
{story_prompt}

Main character:
{character_name}

Setting:
{setting}

Story tone:
{tone}

Art style:
{art_style}

Return ONLY valid JSON.

Use exactly this structure:

{{
    "title": "short comic title",
    "panels": [
        {{
            "panel_number": 1,
            "title": "short panel title",
            "scene_description": "2-3 sentence visual description",
            "image_prompt": "detailed prompt for an AI image generator"
        }}
    ]
}}

Important rules:

1. Generate exactly {PANEL_COUNT} panels.
2. Keep the same main character throughout.
3. The story should have:
   - setup
   - development
   - turning point
   - climax
   - ending
4. Image prompts must include:
   - character
   - environment
   - action
   - composition
   - lighting
   - requested art style
5. Make the panels visually different.
6. Do not include markdown.
7. Do not include explanations outside JSON.
"""

    client = get_client()

    response = client.models.generate_content(
        model=GEMINI_OUTLINE_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.9,
            max_output_tokens=5000
        )
    )

    return extract_json(
        response.text
    )