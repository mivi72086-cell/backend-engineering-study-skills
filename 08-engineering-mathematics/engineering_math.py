import time

# 📊 1. BIG-O NOTATION SIMULATION
def constant_time_lookup(data_dict, key):
    """O(1) Complexity: Instant lookup regardless of size."""
    start = time.perf_counter()
    result = data_dict.get(key)
    duration = time.perf_counter() - start
    return duration

def linear_time_search(data_list, target):
    """O(N) Complexity: Must scan everything step-by-step."""
    start = time.perf_counter()
    for item in data_list:
        if item == target:
            break
    duration = time.perf_counter() - start
    return duration


# 🔐 2. CRYPTOGRAPHIC MODULO OPERATION
def simulate_crypto_hash(input_number):
    """A tiny simulation of a mathematical one-way scramble using prime numbers and modulo."""
    LARGE_PRIME_A = 48611
    LARGE_PRIME_B = 51071
    LARGE_MODULUS = 100003
    
    # Mathematical mixing step
    scrambled_step = (input_number * LARGE_PRIME_A) + LARGE_PRIME_B
    final_hash_digest = scrambled_step % LARGE_MODULUS
    return final_hash_digest


if __name__ == "__main__":
    print("--- 📐 Running Career Mathematics Sandbox ---")
    
    # Setup two datasets: One small, one massive
    small_list = list(range(100))
    large_list = list(range(1000000)) # 1 Million items!
    
    small_dict = {i: i for i in small_list}
    large_dict = {i: i for i in large_list}
    
    # Test O(1) vs O(N) at scale
    print("\n🔬 Testing Big-O Scale Mechanics:")
    print(f"⏱️ O(1) Dictionary Lookup (Small Size): {constant_time_lookup(small_dict, 99):.8f}s")
    print(f"⏱️ O(1) Dictionary Lookup (1 Million Items): {constant_time_lookup(large_dict, 999999):.8f}s")
    print("📈 Notice how the O(1) lookup time stays nearly identical even when data multiplied by 10,000x!")
    
    print(f"\n⏱️ O(N) Linear Scan (Small Size): {linear_time_search(small_list, 99):.8f}s")
    print(f"⏱️ O(N) Linear Scan (1 Million Items): {linear_time_search(large_list, 999999):.8f}s")
    print("🚨 Look how much longer the Linear Scan took when data grew! That scales terribly in production.")
    
    # Test Crypto Math
    print("\n🔬 Testing One-Way Modulo Math:")
    test_val = 12345
    hash_digest = simulate_crypto_hash(test_val)
    print(f"Raw Input Number: {test_val}  --> Scrambled Hash Output: {hash_digest}")