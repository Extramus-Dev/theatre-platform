FROM python:3.9
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
RUN python -m pip install pyparsing pydot

# install graphviz
# RUN apt-get -y update
# RUN apt-get install -y graphviz