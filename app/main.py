from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@app.post("/generate")
def generate(
    request: Request,
    story_prompt: str = Form(...)
):
    layout = [
        {
            "panel": 1,
            "title": "The Beginning",
            "scene": "Your story begins here.",
            "caption": story_prompt
        },
        {
            "panel": 2,
            "title": "The Adventure",
            "scene": "The character starts the adventure.",
            "caption": "An exciting journey begins..."
        },
        {
            "panel": 3,
            "title": "The Ending",
            "scene": "The story reaches its conclusion.",
            "caption": "And the adventure comes to an end."
        }
    ]

    return templates.TemplateResponse(
        request=request,
        name="comic_preview.html",
        context={"layout": layout}
    )


@app.get("/export-success")
def export_success(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="export_success.html",
        context={
            "pdf_path": "generated/comic.pdf"
        }
    )