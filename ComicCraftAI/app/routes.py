from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
import random, urllib.parse, os

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent
template_dir = "app/templates" if os.path.exists("app/templates") else str(BASE_DIR / "templates")
if not os.path.exists(template_dir):
    template_dir = "templates"
templates = Jinja2Templates(directory=template_dir)

def get_dummy_images(story, character, style, num=5):
    imgs = []
    for i in range(num):
        prompt = f"{character} {story} panel {i+1} {style} comic book"
        encoded = urllib.parse.quote(prompt)
        url = f"https://image.pollinations.ai/prompt/{encoded}?seed={random.randint(1,999999)}"
        imgs.append(url)
    return imgs

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/generate", response_class=HTMLResponse)
async def generate(request: Request):
    form = await request.form()
    story_prompt = form.get("story_prompt") or form.get("story") or "adventure story"
    main_character = form.get("main_character") or form.get("character") or "hero"
    art_style = form.get("art_style") or "comic"
    
    images = get_dummy_images(story_prompt, main_character, art_style)
    
    return templates.TemplateResponse("comic_preview.html", {
        "request": request,
        "images": images,
        "story": story_prompt,
        "character": main_character
    })