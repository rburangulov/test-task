from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='kafka1:9092')

while True:
    producer.send('input', 'Hello, World!')
