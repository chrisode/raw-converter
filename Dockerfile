FROM alpine

RUN apk add bash python3 py-pip rawtherapee exiftool

RUN mkdir /app
ADD requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt && rm /app/requirements.txt

ADD batch_convert.sh /app/batch_convert.sh
ADD convert.py /app/convert.py

ENTRYPOINT [ "/app/batch_convert.sh" ]