from fastapi import FastAPI

app = FastAPI()


@app.post("/short_url")
def generate_short_url():
    return ...


@app.get("/{slug}")
def redirect_to_short_url(slug: str):
    return ...
