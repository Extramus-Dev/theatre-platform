# Base image for newly image. Alpine version is lightweigther.
FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1

# Set app directory
WORKDIR /app
COPY . /app/

# install python dependencies
RUN python -m pip install --upgrade pip
# dependencies
RUN python -m pip install Django djangorestframework django-extensions
RUN python -m pip install pymysql
RUN python -m pip install python-dotenv