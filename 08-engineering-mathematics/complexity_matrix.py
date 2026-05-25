import time

# 🟢 O(1) - Instant lookup
def test_constant(data_dict, target_key):
    start = time.perf_counter()
    _ = data_dict.get(target_key)
    return (time.perf_counter() - start) * 1000  # Convert to milliseconds

# 🟡 O(N) - Single Loop Scan
def test_linear(data_list, target_value):
    start = time.perf_counter()
    for item in data_list:
        if item == target_value:
            break
    return (time.perf_counter() - start) * 1000

# 🔴 O(N^2) - Nested Loop Scan (The Performance Killer)
def test_quadratic(data_list):
    start = time.perf_counter()
    total_duplicate_checks = 0
    
    # Loop 1: Grab an item
    for item_a in data_list:
        # Loop 2: Compare it against every single other item!
        for item_b in data_list:
            if item_a == item_b:
                total_duplicate_checks += 1
                
    duration_ms = (time.perf_counter() - start) * 1000
    return duration_ms, total_duplicate_checks

if __name__ == "__main__":
    print("--- 🔬 Running Big-O Performance Matrix ---")
    
    # Let's create a moderate dataset size of 5,000 items
    SIZE = 5000
    test_list = list(range(SIZE))
    test_dict = {i: i for i in test_list}
    
    print(f"Dataset Size: {SIZE} items")
    print("-" * 40)
    
    # 1. Measure O(1)
    time_o1 = test_constant(test_dict, SIZE - 1)
    print(f"🟢 O(1) Constant Lookup:  {time_o1:.6f} ms")
    
    # 2. Measure O(N)
    time_on = test_linear(test_list, SIZE - 1)
    print(f"🟡 O(N) Linear Scan:     {time_on:.6f} ms")
    
    print("\n⏳ Now running the O(N^2) Nested Loop simulation...")
    print("⚠️ Notice how the computer pauses because the math forces it to take 25 MILLION steps!")
    
    # 3. Measure O(N^2) using a much smaller chunk (only 2,000 items) so your computer doesn't crash
    reduced_list = list(range(2000))
    time_on2, checks = test_quadratic(reduced_list)
    
    print("-" * 40)
    print(f"🔴 O(N^2) Quadratic Scan (on just 2,000 items!): {time_on2:.2f} ms")
    print(f"📊 Total cross-comparison computations made: {checks:,} steps")