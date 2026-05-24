from confluent_kafka import Producer
import json
import time

# 1. Point our connection to the exact port we exposed in our docker-compose file
config = {
    'bootstrap.servers': 'localhost:9092'
}

producer = Producer(config)

# A callback function that triggers as soon as Kafka safely writes the message to its disk
def delivery_report(err, msg):
    if err is not None:
        print(f"❌ Delivery failed: {err}")
    else:
        print(f"🚀 Event safely written to Kafka! Topic: {msg.topic()} | Partition: [{msg.partition()}]")

print("--- Starting Production-Grade Kafka Producer ---")

# 2. Stream 5 live tracking notifications to a custom Kafka topic
for i in range(1, 6):
    payload = {
        "order_id": 6000 + i,
        "status": "Food Packing",
        "timestamp": time.time()
    }
    
    # Convert JSON payload into strings/bytes before sending over the wire
    producer.produce(
        topic='zomato-live-tracking', 
        key=str(payload["order_id"]), 
        value=json.dumps(payload), 
        callback=delivery_report
    )
    
    # Flush forces the producer to send the message immediately out of internal memory buffer
    producer.flush()
    time.sleep(1)

print("🏁 Stream sequence dispatched successfully.")