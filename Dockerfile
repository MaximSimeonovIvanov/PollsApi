FROM python:3.8

ENV PYTHONBUFFERED 1

RUN mkdir /application

WORKDIR /application

COPY ./application /application

RUN pip install -r requirements.txt