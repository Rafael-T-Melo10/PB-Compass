FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install boto3

ENV AWS_ACCESS_KEY_ID=
ENV AWS_SECRET_ACCESS_KEY=
ENV AWS_SESSION_TOKEN=

CMD ["python", "etl.py"]
