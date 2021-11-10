# Set parent image for our own
FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1

# Set app directory
WORKDIR /app
COPY .  /app/

# Install python dependencies
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
