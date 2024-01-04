from confluent_kafka import Producer
import json
import time
import random
import datetime

conf = {'bootstrap.servers': 'localhost:9092'}

p = Producer(conf)

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

for i in range(1, 1001):
    message = {
        "timestamp": int(time.time()),
        "userId": random.randint(1, 1000),
        "name": f"field{i}",
        "value": f"value{i}",
        "ccPath": f"{i}_controller"
    }
    p.produce("filters", json.dumps(message), callback=delivery_report)

p.flush()
