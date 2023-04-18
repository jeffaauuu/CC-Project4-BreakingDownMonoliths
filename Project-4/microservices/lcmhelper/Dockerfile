FROM python:3.8-alpine

COPY ./lcm/requirements.txt /lcm/requirements.txt

WORKDIR /lcm

RUN apk add --update \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && rm -rf /var/cache/apk/*

COPY ./lcm /lcm

EXPOSE 8005

CMD ["python", "lcm-helper.py"]
