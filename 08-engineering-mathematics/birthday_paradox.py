import random

def simulate_birthday_collision(room_size):
    """Simulates a room of people and checks if any two share a birthday (1-365)."""
    birthdays = []
    
    for _ in range(room_size):
        # Assign a random day of the year
        day = random.randint(1, 365)
        
        # If the day is already in our list, we found a collision match!
        if day in birthdays:
            return True
        birthdays.append(day)
        
    return False # No matches found in this room

if __name__ == "__main__":
    print("--- 🔬 Running Birthday Paradox Probability Matrix ---")
    
    # We will test rooms of different sizes, running 10,000 simulations per room size
    RUNS = 10000
    test_sizes = [5, 10, 23, 40, 57]
    
    print(f"Running {RUNS:,} sample rooms for each size to calculate the exact mathematical odds...\n")
    
    for size in test_sizes:
        collisions_detected = 0
        
        for _ in range(RUNS):
            if simulate_birthday_collision(size):
                collisions_detected += 1
                
        # Calculate the empirical probability percentage
        probability = (collisions_detected / RUNS) * 100
        print(f"👥 Room Size: {size} people | 💥 Shared Birthdays Detected: {collisions_detected}/{RUNS} times | 📊 Odds: {probability:.2f}%")