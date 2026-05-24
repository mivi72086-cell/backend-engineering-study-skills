import time
import random

class CircuitBreaker:
    def __init__(self, failure_threshold=3, cooldown_period=5):
        self.failure_threshold = failure_threshold # Max failures allowed before tripping
        self.cooldown_period = cooldown_period     # Seconds to stay open before testing
        self.state = "CLOSED"                      # Initial state
        self.failure_count = 0
        self.last_state_change = time.time()

    def call_recommendation_api(self):
        current_time = time.time()

        # 🚨 CHECK 1: If circuit is OPEN, check if the cooldown has expired
        if self.state == "OPEN":
            if current_time - self.last_state_change > self.cooldown_period:
                print("\n🔄 [BREAKER] Cooldown expired. Switching to HALF-OPEN to test the service...")
                self.state = "HALF-OPEN"
                self.last_state_change = current_time
            else:
                # Instantly fail-fast without hitting the broken service
                print("🚫 [BREAKER] Circuit is OPEN! Blocking call to protect system. Serving empty fallback layout.")
                return {"recommendations": []} # Graceful Fallback

        # ⚙️ SIMULATE THE SERVICE: Let's mimic an unstable recommendation server
        # (For requests 3 to 7, it will completely crash)
        is_service_broken = True if 3 <= request_counter <= 7 else False

        if is_service_broken:
            print("💥 [EXTERNAL API] Recommendation Server threw a 500 Server Error!")
            self.failure_count += 1
            
            if self.state == "HALF-OPEN" or self.failure_count >= self.failure_threshold:
                if self.state != "OPEN":
                    print("🚨 [BREAKER] Failure threshold reached! TRIPPING CIRCUIT TO OPEN!")
                    self.state = "OPEN"
                    self.last_state_change = current_time
            return {"recommendations": []} # Graceful Fallback
            
        else:
            # Service is healthy
            print("🟢 [EXTERNAL API] Recommendation Server returned data successfully!")
            self.failure_count = 0
            if self.state == "HALF-OPEN":
                print("🔒 [BREAKER] Service recovered! Closing circuit back to normal.")
                self.state = "CLOSED"
            return {"recommendations": ["Item A", "Item B"]}

# --- SIMULATE LIVE USER TRAFFIC ---
breaker = CircuitBreaker()
request_counter = 1

print("--- Starting Chaos Engineering Circuit Breaker Simulation ---")

for i in range(1, 12):
    print(f"\n👉 User Request #{request_counter} visiting Product Page...")
    response = breaker.call_recommendation_api()
    
    request_counter += 1
    time.sleep(1) # Wait 1 second between user visits