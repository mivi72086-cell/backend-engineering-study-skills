from confluent_kafka import Consumer, KafkaError
import json

# 1. Configuration rules for our background worker
config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'live-tracking-dashboard-group', # Unique Consumer Group ID
    'auto.offset.reset': 'earliest' # Start reading from the absolute beginning of the stream
}

consumer = Consumer(config)

# 2. Subscribe to the exact topic our producer wrote to
consumer.subscribe(['zomato-live-tracking'])

print("--- Real Kafka Consumer Initialized. Listening for live stream events... ---")

try:
    while True:
        # Poll Kafka for a new message every 1.0 second
        msg = consumer.poll(1.0)
        
        if msg is None:
            # No new events on the conveyor belt right now; loop back and keep waiting
            continue
            
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition reached
                continue
            else:
                print(f"❌ Consumer Error: {msg.error()}")
                break
                
        # 3. Successfully pulled a message out of the cluster!
        # Decode the raw bytes back into readable text layout
        event_data = json.loads(msg.value().decode('utf-8'))
        
        print(f"⚙️ [CONSUMER] Retrieved Event from Partition [{msg.partition()}] at Offset #{msg.offset()}")
        print(f"    📦 Payload: Order #{event_data['order_id']} | Status Change: {event_data['status']}")
        print("-" * 50)

except KeyboardInterrupt:
    # Cleanly exit if you press Ctrl + C
    print("\n🛑 Shutting down consumer worker gracefully...")
finally:
    # Close connection and commit finalized offsets to Kafka
    consumer.close()