from fastapi import FastAPI
import uvicorn
from src.backend.faceted_search.db.engine import create_db_and_tables

from src.backend.faceted_search.api.api import api_router

app = FastAPI()


@app.get("/")
def home():
    return {"data": "hello world"}


# create the db and tables

create_db_and_tables()

app.include_router(router=api_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8081)
