from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='kafka-service:9092')

while True:
    time_ms = time.time_ns() // 1000000000
    message = time_ms.to_bytes((time_ms.bit_length() + 7) // 8, 'big')
    producer.send('input', message)
    time.sleep(5)
