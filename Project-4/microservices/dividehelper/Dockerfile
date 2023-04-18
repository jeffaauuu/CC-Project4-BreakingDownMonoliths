FROM python:3.8-alpine

COPY ./divide/requirements.txt /divide/requirements.txt

WORKDIR /divide

RUN apk add --update \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && rm -rf /var/cache/apk/*

COPY ./divide /divide

EXPOSE 8003

CMD ["python", "divide-helper.py"]
