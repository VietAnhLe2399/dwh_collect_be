FROM python:3.9.5-slim-buster

ENV PYTHONUNBUFFERED 1

COPY . /app
RUN apt-get update
RUN pip3 install -r /app/requirements.txt

COPY docker-run.sh /code/docker-run.sh
WORKDIR /app
RUN ["chmod", "+x", "./docker-run.sh"]

ENTRYPOINT ["sh", "./docker-run.sh"]