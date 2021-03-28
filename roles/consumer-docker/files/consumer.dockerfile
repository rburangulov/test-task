FROM python:3

WORKDIR /usr/src/app

RUN pip install kafka-python

COPY consumer.py ./

CMD [ "python", "./consumer.py" ]
