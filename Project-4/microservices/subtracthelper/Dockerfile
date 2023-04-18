FROM python:3.8-alpine

COPY ./subtract/requirements.txt /subtract/requirements.txt

WORKDIR /subtract

RUN apk add --update \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && rm -rf /var/cache/apk/*

COPY ./subtract /subtract

EXPOSE 8001

CMD ["python", "subtract-helper.py"]
