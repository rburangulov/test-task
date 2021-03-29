from kafka import KafkaConsumer

consumer = KafkaConsumer('input', bootstrap_servers='kafka-service:9092')

for message in consumer:
        print (message.value)
