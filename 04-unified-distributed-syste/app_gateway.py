from fastapi import FastAPI, Form
from confluent_kafka import Producer
import hashlib
import json
import os
import time

app = FastAPI()
producer = Producer({'bootstrap.servers': 'localhost:9092'})

@app.post("/api/register")
def register_user(username: str = Form(...), password: str = Form(...)):
    start_time = time.time()
    
    # 1. Cryptographic Privacy Engineering
    salt = os.urandom(16)
    hashed_password = hashlib.sha256(salt + password.encode('utf-8')).hexdigest()
    
    # 2. Fire-and-forget Event offload to Kafka Stream
    event_payload = {
        "event_type": "USER_REGISTRATION",
        "username": username,
        "secure_hash": hashed_password,
        "salt_hex": salt.hex(),
        "timestamp": time.time()
    }
    
    producer.produce(
        topic='user-lifecycle-events',
        key=username,
        value=json.dumps(event_payload)
    )
    producer.flush()
    
    return {
        "status": "Account created successfully",
        "username": username,
        "latency_seconds": round(time.time() - start_time, 4)
    }