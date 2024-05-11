FROM python:3.10-slim-bullseye

WORKDIR /usr/src/fastapiapp1

RUN apt-get update -y && apt-get upgrade -y
COPY . .
RUN python -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "./run.sh" ]

