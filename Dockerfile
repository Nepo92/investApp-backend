FROM python:3.13-rc-alpine

WORKDIR /root/backend/

COPY . .

RUN apk update \ 
    && apk add postgresql-dev \
    && apk add gcc \
    && apk add python3-dev \
    && apk add musl-dev \
    && apk add git

RUN pip install psycopg2-binary

CMD git pull