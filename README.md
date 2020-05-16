# reggie

Simple user registration site with single third party API integration.

## Setup

First, you will need to install 'docker' and 'docker-compose'.

Once these are installed, setup the containers with `docker-compose build` then start them with `docker-compose up` or `docker-compose up -d` to run in detached mode.

On first boot-up, you will need to open a new terminal **while** the containers are running and apply migrations by running `docker-compose run django python manage.py migrate`.
