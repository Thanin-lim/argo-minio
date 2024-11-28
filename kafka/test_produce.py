from kafka import KafkaProducer
import json
import logging

# Enable debugging
logging.basicConfig(level=logging.DEBUG)

# Kafka settings
bootstrap_servers = 'localhost:9092'  # Adjust if needed
topic = '1'  # Replace with your Kafka topic

# Create a Kafka producer instance
producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Produce a message to the Kafka topic
message = {"key": "value", "message": "Hello Kafka!"}
producer.send(topic, value=message)

# Ensure the message is sent before closing
producer.flush()

print("Message sent to Kafka topic:", topic)
