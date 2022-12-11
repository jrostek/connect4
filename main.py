"""API functions for running the game."""
from fastapi import FastAPI
from gameplay import play_game

app = FastAPI()


@app.get("/")
async def root():
    """Root of the app."""
    play_game()
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    """Who knows."""
    return {"message": f"Hello {name}"}
