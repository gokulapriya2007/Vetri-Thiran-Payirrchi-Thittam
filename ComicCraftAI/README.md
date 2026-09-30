# ComicCraft - AI Comic Story Creator

ComicCraft is a FastAPI-based Generative AI application that converts a user's story idea into a five-panel comic.

## Features

- Story prompt input
- Main character input
- Setting selection
- Story tone selection
- Art style selection
- Gemini AI story outline generation
- Gemini AI narration generation
- Character dialogue generation
- AI image generation
- Five-panel comic preview
- PDF export
- JSON API
- Image testing endpoint
- Health-check endpoint

---

# Project Structure

```text
ComicCraft/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routes.py
│   ├── config.py
│   ├── models.py
│   ├── gemini_flash.py
│   ├── gemini_pro.py
│   ├── image_generator.py
│   ├── layout_builder.py
│   └── exporters.py
│
├── templates/
│   ├── index.html
│   ├── comic_preview.html
│   ├── export_success.html
│   └── test_image.html
│
├── static/
│   ├── style.css
│   ├── panels/
│   └── exports/
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md