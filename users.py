import hashlib

def hash_password(p):
    return hashlib.sha256(p.encode()).hexdigest()

USERS = {
    "admin": hash_password("admin123"),
    "user1": hash_password("password1")
}
