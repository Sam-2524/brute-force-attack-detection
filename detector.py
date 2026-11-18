from datetime import datetime, timedelta
from collections import defaultdict

FAILED_LIMIT = 5
TIME_WINDOW = timedelta(minutes=2)
BLOCK_TIME = timedelta(minutes=10)

failed = defaultdict(list)
blocked = {}

def is_blocked(ip):
    if ip in blocked:
        if datetime.now() < blocked[ip]:
            return True
        else:
            del blocked[ip]
    return False

def record_fail(ip):
    now = datetime.now()
    failed[ip].append(now)

    failed[ip] = [t for t in failed[ip] if now - t <= TIME_WINDOW]

    if len(failed[ip]) >= FAILED_LIMIT:
        blocked[ip] = now + BLOCK_TIME
        failed[ip].clear()
        return True
    return False
