import os
from pathlib import Path

from dotenv import load_dotenv


# --------------------------------------------------
# Base directory
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent


# --------------------------------------------------
# Load .env
# --------------------------------------------------

load_dotenv(BASE_DIR / ".env")


# --------------------------------------------------
# Gemini configuration
# --------------------------------------------------

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY",
    ""
).strip()


GEMINI_OUTLINE_MODEL = os.getenv(
    "GEMINI_OUTLINE_MODEL",
    "gemini-3.8-flash"
)


GEMINI_STORY_MODEL = os.getenv(
    "GEMINI_STORY_MODEL",
    "gemini-3.8-flash"
)


GEMINI_IMAGE_MODEL = os.getenv(
    "GEMINI_IMAGE_MODEL",
    "gemini-3.1-flash-image"
)


# --------------------------------------------------
# Image provider
# --------------------------------------------------

IMAGE_PROVIDER = os.getenv(
    "IMAGE_PROVIDER",
    "gemini"
).lower()


# --------------------------------------------------
# Hugging Face
# --------------------------------------------------

HF_TOKEN = os.getenv(
    "HF_TOKEN",
    ""
).strip()


HF_IMAGE_MODEL = os.getenv(
    "HF_IMAGE_MODEL",
    "stabilityai/stable-diffusion-xl-base-1.0"
)


# --------------------------------------------------
# Comic settings
# --------------------------------------------------

PANEL_COUNT = int(
    os.getenv(
        "PANEL_COUNT",
        "5"
    )
)


IMAGE_WIDTH = int(
    os.getenv(
        "IMAGE_WIDTH",
        "1024"
    )
)


IMAGE_HEIGHT = int(
    os.getenv(
        "IMAGE_HEIGHT",
        "1024"
    )
)


# --------------------------------------------------
# Directories
# --------------------------------------------------

STATIC_DIR = BASE_DIR / "static"

PANELS_DIR = STATIC_DIR / "panels"

EXPORTS_DIR = STATIC_DIR / "exports"

TEMPLATES_DIR = BASE_DIR / "templates"


# Make sure folders exist
PANELS_DIR.mkdir(
    parents=True,
    exist_ok=True
)

EXPORTS_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# --------------------------------------------------
# API key validation
# --------------------------------------------------

def require_gemini():

    if not GEMINI_API_KEY:

        raise RuntimeError(
            "GEMINI_API_KEY is missing. "
            "Open the .env file and add your Gemini API key."
        )