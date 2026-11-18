import time
from detector import record_fail

LOG_FILE = "login.log"

with open(LOG_FILE, "r") as f:
    f.seek(0,2)
    print("🔍 Real-time IDS running...")

    while True:
        line = f.readline()
        if line:
            if "FAIL" in line:
                ip = line.split()[3]
                record_fail(ip)
                print(f"[ALERT] Failed login from {ip}")
        time.sleep(1)
