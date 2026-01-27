import re
def analyze_log(lines):
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s*-\s*(\d{1,3}(?:\.\d{1,3}){3})'
    for line in lines:
        try:
            match = re.search(pattern, line)
            if not match:
                raise ValueError("Invalid log format")
            timestamp, ip = match.groups()
            print(f"Timestamp: {timestamp} | IP: {ip}")
        except ValueError:
            continue
log_data = [
    "2025-01-01 10:30:00 - 192.168.0.10",
    "Invalid data line",
    "2025-01-02 11:00:00 - 10.0.0.5"
]
analyze_log(log_data)