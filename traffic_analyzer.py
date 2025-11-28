from collections import Counter
import time
import sys

def cut_string(s, cut_char):
    return s.split(cut_char)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Please provide a file name. Example: python script.py access.log")
        sys.exit(1)
    # Constants
    ONE_DAY = 86400

    # Variables
    file_lines = []
    count_lines = int()
    count_unique_lines = int()
    top_ip_addresses = dict()
    unique_ips_in_last_day = int()

    file = open(sys.argv[1], "r")
    timestamp = int(time.time())
    limit = timestamp - ONE_DAY

    # Read lines from the file
    for line in file:
        file_lines.append(line.strip())

    # Analyze lines
    counter = Counter(file_lines)

    count_lines = len(file_lines)
    count_unique_lines = len(set(file_lines))    
    top_ip_addresses = [
        (line.split()[1], count)
        for line, count in sorted(counter.items(), key=lambda x: x[1], reverse=True)[:3]
    ]
    unique_ips_in_last_day = sum(
        1
        for ts, count in counter.items()
        if int(ts.split()[0]) >= limit
    )

    # Print results
    if (len(sys.argv) > 2):
        if (sys.argv[2] == "--full"):
            print(f"File lines: {file_lines}")
            print(f"Current timestamp: {timestamp}")

    print(f"Total requests: {count_lines}")
    print(f"Unique IPs: {count_unique_lines}")

    print("Top 3 IPs:")
    for ip, count in top_ip_addresses:
        print(f"-{ip}: {count}")

    print(f"Unique IPs in last 24h: {unique_ips_in_last_day}")