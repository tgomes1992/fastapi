from fastapi import FastAPI
import os

import logging

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}




