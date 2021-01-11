FROM alpine

RUN apk add bash python3 py-pip rawtherapee exiftool
RUN pip install pyexiftool
RUN mkdir /app

ADD batch_convert.sh /app/batch_convert.sh
ADD convert.py /app/convert.py


#ENTRYPOINT [ "/app/convert.sh" ]