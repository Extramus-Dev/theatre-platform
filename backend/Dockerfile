# Set parent image for our own
FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1

# Set app directory
WORKDIR /app
COPY .  /app/

# Install necessary apps
RUN apk update
RUN apk add --virtual build-deps gcc python3-dev musl-dev
RUN apk add --no-cache mariadb-dev

# Install python dependencies
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

# Uninstall no more necessary packages
RUN apk del build-deps
