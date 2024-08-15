#!/usr/bin/env python3
import sys
import signal

total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_statistics():
    """Prints the current statistics."""
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")

def signal_handler(sig, frame):
    """Handles keyboard interruption (CTRL + C)."""
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    parts = line.split()
    if len(parts) < 7:
        continue
    try:
        ip_address = parts[0]
        date = parts[3] + " " + parts[4]
        method = parts[5][1:]
        resource = parts[6]
        protocol = parts[7][:-1]
        status_code = int(parts[8])
        file_size = int(parts[9])
        
        total_size += file_size
        if status_code in status_counts:
            status_counts[status_code] += 1
        line_count += 1
        
        if line_count % 10 == 0:
            print_statistics()
    except (IndexError, ValueError):
        continue

print_statistics()
