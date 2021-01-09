FROM alpine

RUN apk add bash rawtherapee
RUN mkdir /app

ADD lib /app/lib
ADD convert.sh /app/convert.sh

ENTRYPOINT [ "/app/convert.sh" ]