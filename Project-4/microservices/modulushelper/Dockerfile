FROM python:3.8-alpine

COPY ./modulus/requirements.txt /modulus/requirements.txt

WORKDIR /modulus

RUN apk add --update \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && rm -rf /var/cache/apk/*

COPY ./modulus /modulus

EXPOSE 8006

CMD ["python", "modulus-helper.py"]
