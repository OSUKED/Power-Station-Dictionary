FROM python:3.10

WORKDIR /code
RUN apt update && apt install nano
RUN pip install poetry

COPY poetry.lock pyproject.toml /code/
RUN poetry install

COPY ./powerdict /code/powerdict
RUN poetry run pip install -e .

COPY ./.env /code/.env
CMD ["poetry", "run", "uvicorn", "powerdict.api.main:app", "--host", "0.0.0.0", "--port", "8000"]