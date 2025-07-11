import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from typing import Union
from fastapi import FastAPI
from script.web_extract import scrape_news

app = FastAPI()

@app.get('/')
def get_news():
    data = scrape_news()
    return data

