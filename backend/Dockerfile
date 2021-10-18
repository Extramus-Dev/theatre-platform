FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /app

RUN python -m pip install --upgrade pip

COPY requirements.txt /app/requirements.txt
RUN python -m pip install -r /app/requirements.txt

COPY . /app/