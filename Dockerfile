FROM python:3.12-rc-alpine

WORKDIR /root/backend/

EXPOSE 80

RUN apk update \ 
    && apk add postgresql-dev \
    && apk add gcc \
    && apk add python3-dev \
    && apk add musl-dev \
    && apk add sudo \
    && apk add git

COPY . .

RUN pip install psycopg2-binary && pip install graphene && pip install python-dotenv

CMD git pull