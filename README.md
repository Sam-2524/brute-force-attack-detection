# Brute Force Attack Detection and Prevention System

A Python-based cybersecurity project that detects repeated failed login attempts and temporarily blocks suspicious IP addresses to help prevent brute-force attacks.

## Project Overview

Brute-force attacks involve repeatedly attempting different passwords to gain unauthorized access to an account.

This project implements a basic detection and prevention mechanism that monitors failed authentication attempts, identifies suspicious activity, and temporarily blocks IP addresses that exceed a defined threshold.

## Key Features

- **Failed Login Monitoring:** Tracks unsuccessful authentication attempts.
- **Brute-Force Detection:** Detects 5 failed attempts within a 2-minute time window.
- **IP Blocking:** Temporarily blocks suspicious IP addresses for 10 minutes.
- **Authentication Checking:** Validates usernames and password hashes.
- **Real-Time Log Monitoring:** Monitors login logs and generates alerts for failed login activity.

## Technologies Used

- Python
- Git and GitHub
- Linux / Kali Linux (security testing environment)

## Project Structure

```text
brute-force-attack-detection/
│
├── auth.py
├── detector.py
├── monitor.py
├── users.py
├── login.py
├── gyi.py
└── README.md
```

## Detection Logic

| Parameter | Configuration |
|---|---|
| Failed login threshold | 5 attempts |
| Detection time window | 2 minutes |
| IP block duration | 10 minutes |

When an IP address reaches the failed-login threshold within the configured time window, the system temporarily blocks further authentication attempts from that IP.

## How It Works

1. A user attempts to log in.
2. The authentication module checks whether the IP address is blocked.
3. Invalid login attempts are recorded.
4. The detection module checks the number of failures within the time window.
5. If the threshold is reached, the IP address is temporarily blocked.
6. The monitoring module generates alerts from failed-login log entries.

## Security Note

This project is an educational prototype, not a production-ready authentication system. The current implementation uses in-memory tracking and demonstration credentials. Strong password hashing, persistent storage, and additional security controls are recommended before real-world deployment.

## Learning Outcomes

- Understanding brute-force attack techniques.
- Implementing failed-login detection using Python.
- Learning basic IP-based blocking mechanisms.
- Understanding authentication security and log monitoring.

## Author

**Sampurn Alok**

Cybersecurity Enthusiast | Aspiring Cybersecurity Analyst

GitHub: [Sam-2524](https://github.com/Sam-2524)
