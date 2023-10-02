# pull official base image
FROM python:3.11.2-slim-buster

# set working directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# add Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock /app/

# install system dependencies
RUN apt-get update \
    && apt-get -y install gcc postgresql netcat \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# install dependencies
RUN pip install --upgrade pip \
    && pip install --upgrade setuptools \
    && pip install pipenv \
    && pipenv sync --dev --system

# copy rest of the app
COPY . .

# make entrypoint.sh executable
RUN chmod +x /app/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
