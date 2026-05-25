import redis
import time

# Connect directly to our in-memory data store instance
# (Natively running on standard Redis port 6379)
try:
    cache = redis.Redis(host='localhost', port=6379, decode_responses=True)
    # Ping the service to confirm connectivity
    cache.ping()
except redis.ConnectionError:
    # Fallback option if local server instance is offline
    print("ℹ️ Local Redis instance offline. Simulating in-memory caching via local dictionary structures...")
    class MockRedis:
        def __init__(self): self.db = {}
        def get(self, k): return self.db.get(k)
        def setex(self, k, t, v): self.db[k] = v
    cache = MockRedis()

def fetch_heavy_user_profile(username):
    """Simulates a heavy database operation that reads from a slow disk or cloud storage."""
    # Step 1: Always check the fast in-memory cache layer first!
    cached_data = cache.get(f"user:{username}")
    
    if cached_data:
        print("⚡ [CACHE HIT] Data pulled instantly from RAM memory storage!")
        return cached_data, True

    # Step 2: Cache Miss - Fallback to the heavy, slow operation
    print("🐌 [CACHE MISS] Pulling records from main database storage disk...")
    time.sleep(2.0)  # Simulating heavy disk read latency
    fresh_profile_data = f"Profile Data for {username} - Verified Premium"
    
    # Step 3: Save the pulled data into the cache with an expiration of 15 seconds
    # This prevents old, stale data from sitting in your system memory forever
    cache.setex(f"user:{username}", 15, fresh_profile_data)
    return fresh_profile_data, False

if __name__ == "__main__":
    print("--- 🏎️ Simulating High-Speed Redis Caching Layer ---")
    USER = "vinit_99"
    
    # Run 1: Cold start (Cache is empty)
    start_time = time.time()
    data, was_cached = fetch_heavy_user_profile(USER)
    duration = time.time() - start_time
    print(f"⏱️ Run 1 Total Execution Time: {duration:.4f} seconds\n")
    
    # Run 2: Hot start (Data now exists inside the fast RAM memory cache)
    start_time = time.time()
    data, was_cached = fetch_heavy_user_profile(USER)
    duration = time.time() - start_time
    print(f"⏱️ Run 2 Total Execution Time: {duration:.4f} seconds")