FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /app

# install python dependencies
RUN python -m pip install --upgrade pip

#dependencies listed
RUN python -m pip install Django
RUN python -m pip install djangorestframework
RUN python -m pip install django-extensions
RUN python -m pip install pymysql
RUN python -m pip install python-dotenv

# Copy application to container
COPY . /app/