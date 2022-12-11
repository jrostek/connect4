"""API functions for running the game."""
from fastapi import FastAPI
from src.gameplay import play_game
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

with open(Path("templates", "index.html")) as f:
    site = f.read()

app = FastAPI()
app.mount("/static", StaticFiles(directory=Path("static")), name="static")
app.mount("/templates", StaticFiles(directory=Path("templates")), name="templates")
# templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root():
    """Root of the app."""
    # play_game()
    replace = site.replace(r"nothing here yet...", "it has worked (somewhat)")
    return HTMLResponse(replace)
