from typing import List

from pydantic import BaseModel, Field


class PromptRequest(BaseModel):

    story_prompt: str = Field(
        min_length=3,
        max_length=2000
    )

    character_name: str = Field(
        default="Alex",
        max_length=100
    )

    setting: str = Field(
        default="enchanted forest",
        max_length=200
    )

    tone: str = Field(
        default="light-hearted",
        max_length=100
    )

    art_style: str = Field(
        default="comic book",
        max_length=100
    )


class Panel(BaseModel):

    panel_number: int

    title: str

    scene_description: str

    image_prompt: str

    caption: str = ""

    narration: str = ""

    dialogue: str = ""

    image_url: str = ""


class ComicResponse(BaseModel):

    title: str

    panels: List[Panel]

    pdf_url: str = ""