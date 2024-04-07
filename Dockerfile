FROM python:3.13-rc-alpine

WORKDIR /root/backend/

COPY . .

RUN apk add git

CMD git pull