FROM python:3

WORKDIR /usr/src/app

RUN pip install kafka-python

COPY producer.py ./

CMD [ "python", "./producer.py" ]
