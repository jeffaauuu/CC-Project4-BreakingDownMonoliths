FROM python:3.8-alpine

COPY ./multiply/requirements.txt /multiply/requirements.txt

WORKDIR /multiply

RUN apk add --update \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && rm -rf /var/cache/apk/*

COPY ./multiply /multiply

EXPOSE 8002

CMD ["python", "multiply-helper.py"]
