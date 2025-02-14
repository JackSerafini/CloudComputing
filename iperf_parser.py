import re
import csv

def parse_iperf_output(log_filename, output_csv):
    with open(log_filename, 'r') as log_file:
        lines = log_file.readlines()

    csv_data = []
    # Define a header appropriate for iperf3 output
    csv_data.append(["run", "start", "end", "transfer", "bitrate", "retr", "cwnd"])
    run_id = None
    # Regex to capture interval data from iperf3
    interval_regex = re.compile(r"\[\s*\d+\]\s+(\d+\.\d+)-(\d+\.\d+)\s+sec\s+([\d\.]+\s+\w+)\s+([\d\.]+\s+\w+)(?:\s+(\d+))?(?:\s+([\d\.]+\s+\w+))?")

    for line in lines:
        line = line.strip()
        # Detect run marker
        run_match = re.match(r">> -- \[ RUN (\d+) \]", line)
        if run_match:
            run_id = run_match.group(1)
            continue

        # Skip header or non-data lines
        if "Interval" in line and "Transfer" in line:
            continue

        m = interval_regex.search(line)
        if m:
            start, end, transfer, bitrate, retr, cwnd = m.groups()
            csv_data.append([run_id, start, end, transfer, bitrate, retr if retr else "", cwnd if cwnd else ""])

    with open(output_csv, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(csv_data)
