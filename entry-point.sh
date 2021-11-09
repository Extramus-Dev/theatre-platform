#!/bin/bash

export DB_HOST=theater-platform-db
export DB_PORT=3306
export API_HOST=theater-platform-django-api-server
export API_PORT=8000
export UI_HOST=theater-platform-web-ui
export UI_PORT=8080

export DB_NAME=theater-platform
export DB_USER='theater_admin'
export DB_USER_PW='theater_platform2021'
export DB_ROOT_PW=root

export VUE_APP_TITLE = Theater Marketplace

docker-compose build
docker-compose up
