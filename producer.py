import time 
import json 
import random 
from datetime import datetime
from data_generator import generate_transaction
from kafka import KafkaProducer

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda m: json.dumps(m).encode('utf-8')
)   

def write_json(new_data, filename='/home/efe/.config/Neo4j Desktop/Application/relate-data/dbmss/dbms-9aae218f-9345-4270-934c-fb4bf54debcc/import/data.json'):
    with open(filename, 'a') as file:
        # If file is not empty, add a comma before appending new data
        if file.tell() != 0:
            file.write('\n')
        json.dump(new_data, file, indent=4)

if __name__ == '__main__':
    while True:
        dummy_message = generate_transaction()
        producer.send('my-topic', dummy_message)
        write_json(dummy_message)
        print(dummy_message)
        time_to_sleep = random.randint(1, 11)
        time.sleep(time_to_sleep)
