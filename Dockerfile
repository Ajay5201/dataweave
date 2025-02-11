FROM python:3.7
WORKDIR /usr/src/nudges
COPY ./app ./app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
