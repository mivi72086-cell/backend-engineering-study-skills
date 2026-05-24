import base64

# 1. The raw sensitive data
secret_password = "vinit_secure_password_2026"
print(f"📄 Original Data: {secret_password}")

# 2. ENCODE: Convert text string to bytes, then encode to Base64
password_bytes = secret_password.encode('utf-8')
base64_encoded_bytes = base64.b64encode(password_bytes)
base64_string = base64_encoded_bytes.decode('utf-8')

print(f"🔒 Base64 Scrambled String: {base64_string}")

print("-" * 50)
print("😈 SIMULATING AN INTERCEPTOR / HACKER...")

# 3. DECODE: Anyone who finds this string can decode it instantly with zero permissions
decoded_bytes = base64.b64decode(base64_string)
unmasked_password = decoded_bytes.decode('utf-8')

print(f"🔓 Instantly Decoded Data: {unmasked_password}")