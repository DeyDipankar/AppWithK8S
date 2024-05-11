FROM python:3.10-slim-bullseye

WORKDIR /usr/src/app

RUN apt-get update && apt-get upgrade
COPY . .
RUN python -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "run.sh" ]

