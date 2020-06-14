FROM phusion/baseimage

RUN apt-get update && apt-get -y install ufraw && apt-get clean
RUN mkdir /app

ADD convert.sh /app/convert.sh
