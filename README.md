# Partner sales points
Usage for the register, find and search partners based on GEOJson with MongoDB.

### Requirements
- python3.8
- docker
- mongodb

## Structure
Has three modules:
- database: access to database and queries for run.
- partners: views and services with business rules there.
- tests: all unit tests off app inside there.

## Run

This app required a localhost instance of mongodb running, for it you can use the docker compose that exists there.
And for run by docker compose run this:
```shell script
docker-compose up
```

And for run, as a flask app:
```shell script
export FLASK_ENV=development && \
export FLASK_APP=partners && \
pip install . && \
flask run
```

## Tests
_All tests found here run with *testcontainer-python*. 
Why? because I cant found a good option of embedded mongo for unittests and testcontainers are a so good framework_

For run tests you need install packages that required to run that:
```shell script
pip install '.[tests]'
pytest
```

## Build a docker image
for build, run this command:
```shell script
docker build -t partner-sales-points .
```

for run that:
```shell script
docker run -p 5000:5000 partner-sales-points
```