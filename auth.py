import hashlib
from users import USERS
from detector import is_blocked, record_fail

def authenticate(username, password, ip):
    if is_blocked(ip):
        return "blocked"

    hashed = hashlib.sha256(password.encode()).hexdigest()
    if username in USERS and USERS[username] == hashed:
        return "success"
    else:
        attack = record_fail(ip)
        return "attack" if attack else "fail"
