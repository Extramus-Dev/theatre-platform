FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1

# Set app directory
WORKDIR /app
COPY theater_platform /app/theater_platform/
COPY web_server       /app/web_server/
COPY manage.py        /app/manage.py

# Install necessary packages
RUN apk update
RUN apk add --virtual build-deps gcc python3-dev musl-dev
RUN apk add --no-cache mariadb-dev

# Install python dependencies
RUN python -m pip install --upgrade pip
RUN python -m pip install Django djangorestframework django-extensions
RUN python -m pip install mysqlclient
RUN python -m pip install python-dotenv

# Uninstall no more necessary packages
RUN apk del build-deps