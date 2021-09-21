FROM ubuntu

ADD /app/requirements.txt /app/requirements.txt

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update \ 
    && apt-get install -y --no-install-recommends python3 pip rawtherapee exiftool \
    && pip install -r /app/requirements.txt && rm /app/requirements.txt \
    && apt-get -y purge python3-pip \
    && apt-get -y autoremove && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/* 

ADD /app /app