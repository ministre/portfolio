from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Anna Boranova"
)


class HomePage(BaseModel):
    subtitle: str
    text: str


home_page = {
    "subtitle": "Педагог дополнительного образования",
    "text": "Руководитель творческого объединения"
}


@app.get("/", response_model=HomePage)
def home():
    return home_page
