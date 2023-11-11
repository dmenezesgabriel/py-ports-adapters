FROM python:3.9-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt --no-cache-dir --upgrade -r requirements.txt

COPY ./src /app/src
COPY ./migrations /app/migrations

CMD ["uvicorn", "src.adapter.driver.api.app:app","--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]
