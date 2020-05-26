FROM python:3.7

COPY . /app
WORKDIR /app

ENV FLASK_ENV=development \
    FLASK_APP=partner

RUN pip install .

CMD ["flask", "run", "--host=0.0.0.0"]