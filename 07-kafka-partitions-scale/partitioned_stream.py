from confluent_kafka import Producer, Consumer
from confluent_kafka.admin import AdminClient, NewTopic
import json
import time

KAFKA_BROKER = 'localhost:9092'
TOPIC_NAME = 'high-scale-user-events'

# 1. THE ARCHITECT ACTION: Force-Create a Topic with 3 Parallel Partitions
def setup_partitioned_topic():
    admin_client = AdminClient({'bootstrap.servers': KAFKA_BROKER})
    
    # Define a new topic explicitly asking for 3 parallel partitions!
    new_topic = NewTopic(TOPIC_NAME, num_partitions=3, replication_factor=1)
    
    # Issue the command to the Docker cluster
    fs = admin_client.create_topics([new_topic])
    for topic, future in fs.items():
        try:
            future.result()
            print(f"🏗️  [INFRASTRUCTURE] Topic '{TOPIC_NAME}' successfully built with 3 parallel partitions!")
        except Exception as e:
            print(f"ℹ️  Topic notification: {e} (It likely already exists).")

# A quick tracking callback to print EXACTLY which partition Kafka chose
def delivery_report(err, msg):
    if err is not None:
        print(f"❌ Delivery failed: {err}")
    else:
        print(f"📡 [PRODUCER] Routed Key '{msg.key().decode('utf-8')}' -> Sent to PARTITION [{msg.partition()}] at Offset {msg.offset()}")

# 2. THE PRODUCER ACTION: Distributing Traffic Using Keys
def simulate_traffic_distribution():
    producer = Producer({'bootstrap.servers': KAFKA_BROKER})
    
    # A list of distinct usernames signing up at the exact same millisecond
    test_users = ["vinit_99", "amit_coder", "rohit_max", "sneha_dev", "rahul_ops", "pooja_tech"]
    
    print("\n⚡ Stream initiated! Distributing payloads across partitions using mathematical key routing...")
    for user in test_users:
        payload = {"username": user, "event": "ACCOUNT_CREATED", "timestamp": time.time()}
    
        # Crucial step: We pass 'key=user'. Kafka uses this text string to calculate the partition index!
        producer.produce(
            topic=TOPIC_NAME,
            key=user,
            value=json.dumps(payload),
            callback=delivery_report
        )
    
    producer.flush()

if __name__ == "__main__":
    setup_partitioned_topic()
    simulate_traffic_distribution()