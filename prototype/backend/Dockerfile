FROM python:3.10.4-alpine3.15

RUN apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers \
		shadow \
		python3-dev \
		openssl-dev \
		libffi-dev


ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /backend
COPY ./requirements.txt /backend/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#CMD ["uwsgi", "app.ini"]
