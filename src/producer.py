from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='kafka1:9092')

while True:
    producer.send('input', 'Hello, World!')
    time.sleep(5)
