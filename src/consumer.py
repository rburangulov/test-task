from kafka import KafkaConsumer
from kafka import KafkaProducer
from datetime import datetime

consumer = KafkaConsumer('input', bootstrap_servers='kafka-service:9092')
producer = KafkaProducer(bootstrap_servers='kafka-service:9092')

for message in consumer:
    message_date_int = int.from_bytes(message.value, 'big')
    message_date = datetime.fromtimestamp(message_date_int).isoformat()
    message_date_bytes = bytes(message_date, encoding='utf-8')
    producer.send('output', message_date_bytes)
