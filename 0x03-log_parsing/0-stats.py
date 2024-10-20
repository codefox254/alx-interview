#!/usr/bin/python3
"""
Log parsing module
"""

import sys
import re


def output(log: dict) -> None:
    """
    Helper function to display stats:
    - Total file size
    - Frequency of each status code
    """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code]:
            print("{}: {}".format(code, log["code_frequency"][code]))


if __name__ == "__main__":
    # Regex to match log lines with IP, date, request, status code, and file size
    regex = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" '
        r'(.{3}) (\d+)'
    )

    line_count = 0
    log = {
        "file_size": 0,
        "code_frequency": {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
    }

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.fullmatch(line)
            if match:
                line_count += 1
                code = match.group(1)
                file_size = int(match.group(2))

                # Increment total file size
                log["file_size"] += file_size

                # Increment status code frequency
                if code.isdecimal() and code in log["code_frequency"]:
                    log["code_frequency"][code] += 1

                # Output log stats every 10 lines
                if line_count % 10 == 0:
                    output(log)
    finally:
        output(log)
