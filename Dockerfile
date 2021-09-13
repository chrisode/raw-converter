FROM ubuntu

ADD requirements.txt /app/requirements.txt

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update \ 
    && apt-get install -y --no-install-recommends python3 pip rawtherapee exiftool \
    && rm -rf /var/lib/apt/lists/* \
    && pip install -r /app/requirements.txt && rm /app/requirements.txt

ADD . /app