from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_news():
    return 'Hi Mom! This is fastAPI'

