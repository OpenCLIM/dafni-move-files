FROM python:slim

RUN mkdir src

WORKDIR src

COPY script.py .

CMD [ "python", "script.py"]