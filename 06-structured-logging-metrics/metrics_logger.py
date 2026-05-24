import json
import time
from datetime import datetime

LOG_FILE = "system_performance.json"

def log_system_event(level: str, endpoint: str, latency_ms: float, status_code: int, message: str):
    """Formats system execution metrics into a structured JSON log entry."""
    
    # 1. Capture the exact timestamp in international ISO format
    current_time = datetime.utcnow().isoformat() + "Z"
    
    # 2. Construct the structured data packet
    log_packet = {
        "timestamp": current_time,
        "log_level": level.upper(),
        "api_endpoint": endpoint,
        "execution_latency_ms": round(latency_ms, 2),
        "http_status": status_code,
        "message": message
    }
    
    # 3. Append the JSON log packet permanently to our metrics file
    with open(LOG_FILE, "a") as file:
        # json.dumps converts a python dictionary into a clean string line
        file.write(json.dumps(log_packet) + "\n")
        
    print(f"📊 [METRIC LOGGED] {level.upper()} | {endpoint} | Latency: {round(latency_ms, 2)}ms")

# --- Simulation to test our Flight Recorder ---
if __name__ == "__main__":
    print("--- 🛫 Initializing System Performance Simulation ---")
    
    # Simulation 1: A super fast database read
    start_time = time.time()
    time.sleep(0.05) # Simulating a 50ms operation
    duration_ms = (time.time() - start_time) * 1000 # Convert seconds to milliseconds
    log_system_event("INFO", "/api/login", duration_ms, 200, "User authorization cleared successfully.")
    
    # Simulation 2: A lagging network timeout event
    start_time = time.time()
    time.sleep(1.2) # Simulating a slow 1.2-second delay
    duration_ms = (time.time() - start_time) * 1000
    log_system_event("WARNING", "/api/fetch-profile", duration_ms, 408, "Database connection timeout threshold approached.")