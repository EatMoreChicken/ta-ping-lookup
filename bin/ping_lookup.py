#!/usr/bin/env python
import csv
import sys
import subprocess
import platform
from datetime import datetime

"""
An external lookup script for Splunk that performs a ping to check if a host is reachable.
This script works on both Windows and Unix-based systems (Linux, macOS).

Usage in Splunk: | lookup ping_lookup host
"""

def ping(host):
    """Ping the specified host and return the result."""
    operating_system = platform.system().lower()
    if operating_system == "windows": # Windows
        ping_cmd = ["ping", "-n", "1", "-w", "2000", host]
    else:  # Unix-based systems (Linux, macOS)
        ping_cmd = ["ping", "-c", "1", "-W", "2", host]
    try:
        subprocess.check_output(ping_cmd, stderr=subprocess.STDOUT, universal_newlines=True)
        return "Reachable"
    except subprocess.CalledProcessError:
        return "Unreachable"

def main():
    infile = sys.stdin
    outfile = sys.stdout

    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ['ping_status', 'timestamp']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        host = row.get('host')
        if host:
            row['ping_status'] = ping(host)
        else:
            row['ping_status'] = 'No host provided'
        row['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow(row)

if __name__ == "__main__":
    main()