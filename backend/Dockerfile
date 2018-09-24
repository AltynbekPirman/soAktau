FROM python:3.6
MAINTAINER Altynbek
ENV PYTHONUNBUFFERED=1
RUN mkdir /src
WORKDIR /src
ADD requirements.txt /src/
RUN pip install -r requirements.txt
ADD init.sh uwsgi.ini /src/ /src/
RUN chmod +x /src/init.sh
