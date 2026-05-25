import jwt
import time

# This secret key is kept hidden on the company's private server. 
# It is used to cryptographically sign our digital wristbands.
SERVER_SECRET_KEY = "super_secret_vinit_key_2026"
ALGORITHM = "HS256"

def issue_digital_wristband(username, role="user"):
    """Generates a secure, cryptographically signed JWT passport for a user."""
    current_time = time.time()
    
    # The payload contains the actual data claims
    payload = {
        "username": username,
        "role": role,
        "iat": current_time,          # Issued At time
        "exp": current_time + 10      # Expires in 10 seconds! (Strict security parameter)
    }
    
    # Sign the token using our secret key
    token = jwt.encode(payload, SERVER_SECRET_KEY, algorithm=ALGORITHM)
    return token
def verify_digital_wristband(token):
    """Decodes and validates the signature of the incoming passport token defensively."""
    try:
        # The library decodes the token and checks if the signature matches our secret key
        decoded_payload = jwt.decode(token, SERVER_SECRET_KEY, algorithms=[ALGORITHM])
        return {"status": "ACCESS_GRANTED", "data": decoded_payload}
    except jwt.ExpiredSignatureError:
        return {"status": "DENIED", "reason": "Token has expired! Access denied."}
    except jwt.InvalidSignatureError:
        return {"status": "DENIED", "reason": "Cryptographic signature mismatch! Tampering detected!"}
    except Exception as e:
        # 🛡️ CATCH-ALL SAFETY GUARDRAIL:
        # This catches bad Base64 layouts, structure corruption, or any chaotic payload manipulation.
        return {"status": "DENIED", "reason": f"Malformed token payload layout structure! Error: {str(e)}"}

# --- Let's Simulate an Authentication Cycle ---
if __name__ == "__main__":
    print("--- 🎟️ Simulating JWT Security System ---")
    
    # 1. User logs in, we give them a token
    vinit_token = issue_digital_wristband(username="vinit_99", role="premium_user")
    print(f"\n🔑 Issued Token for vinit_99:\n{vinit_token}")
    
    # 2. User tries to view a premium feature right away
    print("\n🔒 Scenario A: User accesses API instantly with the valid token:")
    result = verify_digital_wristband(vinit_token)
    print(f"Server Response: {result}")
    
    # 3. Hacker tries to forge a token by modifying data or signing it with a fake key
    print("\n🚨 Scenario B: A hacker tries to forge a fake token:")
    fake_token = vinit_token + "tampered_bytes"
    result = verify_digital_wristband(fake_token)
    print(f"Server Response: {result}")
    
    # 4. Testing expiration security parameters
    print("\n⏳ Scenario C: Waiting 11 seconds for the token to naturally expire...")
    time.sleep(11)
    result = verify_digital_wristband(vinit_token)
    print(f"Server Response: {result}")