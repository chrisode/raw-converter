FROM ubuntu

ADD /raw-converter/requirements.txt /raw-converter/requirements.txt

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update \ 
    && apt-get install -y --no-install-recommends python3 pip rawtherapee exiftool \
    && pip install -r /raw-converter/requirements.txt \
    && apt-get -y purge python3-pip \
    && apt-get -y autoremove && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/* 

ADD /raw-converter /raw-converter

## Backwards compability
RUN ln -s /raw-converter /app