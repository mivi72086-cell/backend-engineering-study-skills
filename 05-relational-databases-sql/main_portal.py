from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse
import hashlib
import os
import sqlite3

# Import our helper functions from the script you just verified!
from database_setup import initialize_database, save_user_to_disk, fetch_user_from_disk

app = FastAPI()

# Make sure our table exists right when the server starts up
initialize_database()

# 1. CLEAN INTERACTIVE WEB INTERFACE
@app.get("/", response_class=HTMLResponse)
def serve_ui():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Secure Disk Auth Hub</title>
        <style>
            body { font-family: 'Segoe UI', sans-serif; background-color: #f0f4f8; padding: 40px; display: flex; gap: 20px; justify-content: center; }
            .box { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); width: 350px; }
            h3 { color: #2c3e50; margin-top: 0; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; }
            input { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #cbd5e1; border-radius: 5px; box-sizing: border-box; }
            button { width: 100%; padding: 10px; border: none; border-radius: 5px; color: white; font-weight: bold; cursor: pointer; margin-top: 5px; }
            .btn-reg { background-color: #2ecc71; }
            .btn-login { background-color: #3498db; }
        </style>
    </head>
    <body>
        <div class="box">
            <h3>📝 Create Account</h3>
            <form action="/auth/register" method="post">
                <input type="text" name="username" placeholder="Choose Username" required>
                <input type="password" name="password" placeholder="Choose Password" required>
                <button type="submit" class="btn-reg">Save to Database</button>
            </form>
        </div>

        <div class="box">
            <h3>🔐 Member Login</h3>
            <form action="/auth/login" method="post">
                <input type="text" name="username" placeholder="Username" required>
                <input type="password" name="password" placeholder="Password" required>
                <button type="submit" class="btn-login">Verify Credentials</button>
            </form>
        </div>
    </body>
    </html>
    """

# 2. THE REGISTER ROUTE (Writing to Disk)
@app.post("/auth/register")
def web_register(username: str = Form(...), password: str = Form(...)):
    # Run our privacy pipeline logic
    salt = os.urandom(16)
    hashed_password = hashlib.sha256(salt + password.encode('utf-8')).hexdigest()
    
    # Attempt to write the row into our SQLite table
    success = save_user_to_disk(username, hashed_password, salt.hex())
    
    if success:
        return {"status": "Success", "message": f"User '{username}' safely written to users.db file!"}
    else:
        raise HTTPException(status_code=400, detail="Username is already taken inside database file.")

# 3. THE LOGIN ROUTE (Reading from Disk & Verifying)
@app.post("/auth/login")
def web_login(username: str = Form(...), password: str = Form(...)):
    # Query the database file to find this user
    user_data = fetch_user_from_disk(username)
    
    if not user_data:
        raise HTTPException(status_code=401, detail="Access Denied: Username not found in users.db.")
        
    # Reconstruct the hash using the incoming login password and the SAVED salt from disk
    saved_hash = user_data["hash"]
    saved_salt_bytes = bytes.fromhex(user_data["salt"])
    
    computed_hash = hashlib.sha256(saved_salt_bytes + password.encode('utf-8')).hexdigest()
    
    # Compare hashes
    if computed_hash == saved_hash:
        return {"status": "Access Granted", "message": f"Welcome back, {username}! Verified via SQLite data columns."}
    else:
        raise HTTPException(status_code=401, detail="Access Denied: Password hash mismatch.")