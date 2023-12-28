from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Salary(BaseModel):
    company: str
    liquid_salary: float
    date: datetime


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/salary")
def read_salary():
    salary = Salary(
        company="Ice Cream C&A", liquid_salary=2_000, date=datetime(2023, 12, 24)
    )
    return salary.model_dump()


@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}


if __name__ == "__main__":
    read_salary()
