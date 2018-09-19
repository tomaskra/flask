FROM alpine:latest

MAINTAINER Tomas Kracka "tomaskracka@gmail.com"

RUN apk upgrade && \
    apk add python python-dev py-pip && \
    pip install virtualenv

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY main.py /app

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]
