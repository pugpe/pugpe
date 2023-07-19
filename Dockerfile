FROM python:2.7.18

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt
