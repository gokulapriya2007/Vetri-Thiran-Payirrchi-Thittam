from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routes import router


BASE_DIR = Path(__file__).resolve().parent.parent

# Create required folders
(BASE_DIR / "static" / "panels").mkdir(
    parents=True,
    exist_ok=True
)

(BASE_DIR / "static" / "exports").mkdir(
    parents=True,
    exist_ok=True
)


app = FastAPI(
    title="ComicCraft - AI Comic Story Creator",
    description="Generate AI-powered five-panel comics using Gemini.",
    version="1.0.0"
)


# Static files
app.mount(
    "/static",
    StaticFiles(
        directory=str(BASE_DIR / "static")
    ),
    name="static"
)

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

# Root folder-a kandupidikka
BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI()

# Idhu thaan mukkiyam - static path-a sariya kudukanum
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

# Unga vera routes ellam idhukku keela irukkanum


app.include_router(router)


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": "ComicCraft"
    }