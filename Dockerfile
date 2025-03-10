FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apt-get update && \
    apt-get install -y gettext

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/
