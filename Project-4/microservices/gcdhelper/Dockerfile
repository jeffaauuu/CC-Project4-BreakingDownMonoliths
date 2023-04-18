FROM python:3.8-alpine

COPY ./gcd/requirements.txt /gcd/requirements.txt

WORKDIR /gcd

RUN apk add --update \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && rm -rf /var/cache/apk/*

COPY ./gcd /gcd

EXPOSE 8004

CMD ["python", "gcd-helper.py"]
