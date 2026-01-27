import re
def validate_log_entry(log_line):
    pattern = r"^\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] (INFO|ERROR|WARN): .+$"
    if re.match(pattern, log_line):
        return "Valid Log Entry"
    else:
        return "Invalid Log Entry"
log = "[2025-11-05 14:33:21] ERROR: Disk full"
print(validate_log_entry(log))