FROM python:3.11 as python-base

WORKDIR /code

COPY pyproject.toml /code/pyproject.toml

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]