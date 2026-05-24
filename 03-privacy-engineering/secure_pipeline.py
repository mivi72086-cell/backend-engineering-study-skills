import hashlib
import os

def secure_hash_pipeline(raw_data: str, user_salt: bytes = None):
    # 1. If no salt is provided, generate a fresh, mathematically secure random 16-byte salt
    if user_salt is None:
        user_salt = os.urandom(16)
        
    # 2. Mix the salt with the raw text data
    # This prevents hackers from using pre-computed "Rainbow Tables" to guess common values
    salted_data = user_salt + raw_data.encode('utf-8')
    
    # 3. Apply the SHA-256 one-way cryptographic hash
    hash_object = hashlib.sha256(salted_data)
    hex_digest = hash_object.hexdigest()
    
    return hex_digest, user_salt

# --- Test the Secure Pipeline ---
print("\n--- Running Secure Cryptographic Hashing Pipeline ---")

user_email = "vinit@example.com"
print(f"📧 Raw Production Email: {user_email}")

# Hash the email for the first time
hashed_email_1, salt = secure_hash_pipeline(user_email)
print(f"🧂 Generated Random Salt: {salt.hex()}")
print(f"🛡️ One-Way Hash Stored in DB: {hashed_email_1}")

print("-" * 50)
print("🔍 VERIFICATION CHECK (User tries to log in again):")

# To verify, we re-hash the incoming input using the EXACT SAME salt we saved earlier
hashed_email_2, _ = secure_hash_pipeline(user_email, user_salt=salt)

if hashed_email_1 == hashed_email_2:
    print("✅ Match Confirmed! The identity is verified, but we never stored the raw email text.")
else:
    print("❌ Verification Failed.")