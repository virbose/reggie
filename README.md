# reggie

Simple user registration site with single third party API integration.

## Setup

First, you will need to install 'docker' and 'docker-compose'. For installation
instructions refer to the Docker [docs](https://docs.docker.com/compose/install/)

Second, create a `.env` file in the same directory as the `docker-compose.yml` file and fill it with the data found in

Once these are installed, setup the containers with `docker-compose build` then start them with `docker-compose up` or `docker-compose up -d` to run in detached mode.

- Personally I recommend running `docker-compose up postgres rabbit flower` in one tab and `docker-compose up frontreg django celery` in a second tab -- this will prevent output saturation if you are wanting to see requests

While the `django` container is being initialized, it will run migrations, Python tests and then run the server. It's no CI/CD but running the tests prevents the server from booting if there are any issues.

## Usage

Once the containers have been set up and started, you should have access to the following:

- The frontend is found at [localhost:3000](http://localhost:3000/); use this to submit a new registration and view existing ones.

- The Django container can be found at [localhost:8000](http://localhost:8000/api/) - use this for the `django-rest-framework` own API navigator.

- There's also a handy celery flower tool available at [localhost:8888](http://localhost:8888/). Keep an eye on this to see how the tasks are doing.

## Caveats

- There is a very clear problem with the containers -- they are all running in development mode.
  - The immediate next step would be to look at deploying these somewhere in production mode, as well as using a bundle of the frontend as opposed to the development server.
- There are some unit tests, checking the integrity of the models and the DRF views

  - There can always be more, also `coverage` doesn't particularly like upping the coverage of its' files even if tests have been written;

- The front-end is not tested although I would have liked to have done that
  - This is a future **TODO** but since the focus was to be on the back-end, I decided to forego the frontend tests
- Error reporting is somewhat limited on the frontend:
  - It says whether an email is invalid or if it exists, but defaults to 'there was an issue' otherwise; this can be improved
