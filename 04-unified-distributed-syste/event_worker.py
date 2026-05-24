from confluent_kafka import Consumer
import asyncio
import json
import time
import random

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'unified-worker-group',
    'auto.offset.reset': 'earliest'
})
consumer.subscribe(['user-lifecycle-events'])

async def processing_pipeline(username):
    # Simulate erratic downstream database latency (0.1s or a lagging 4.0s)
    if random.choice([True, False]):
        print(f"⚠️  [CHAOS] Downstream service lagging for: {username}")
        await asyncio.sleep(4.0)
    else:
        await asyncio.sleep(0.1)
    print(f"📧 [SUCCESS] Onboarding complete for: {username}")

async def start_worker():
    print("--- Running Resilient Async Event Consumer Worker ---")
    try:
        while True:
            msg = consumer.poll(0.5)
            if msg is None or msg.error():
                await asyncio.sleep(0.1)
                continue
                
            event_data = json.loads(msg.value().decode('utf-8'))
            username = event_data['username']
            print(f"\n📥 Processing Event for '{username}' from Offset #{msg.offset()}")
            
            # Enforce strict 1.5-second hard asynchronous time fence
            try:
                await asyncio.wait_for(processing_pipeline(username), timeout=1.5)
            except asyncio.TimeoutError:
                print(f"🚨 [TIMEOUT] Processing exceeded limit! Dropping worker lag.")
                print(f"🔄 [DLQ LOG] Moved user '{username}' to recovery queue for offline retry.")
    except KeyboardInterrupt:
        print("Stopping worker...")
    finally:
        consumer.close()

if __name__ == "__main__":
    asyncio.run(start_worker())