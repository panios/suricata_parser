import csv
import re

def parse_text_to_csv(input_file, output_csv):
    with open(input_file, 'r') as file:
        input_text = file.read()

    # Split the text into sections
    sections = re.split(r'\+\=+\n', input_text)

    # Prepare CSV file
    with open(output_csv, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write the header
        csv_writer.writerow(['Packet Data', 'Alert SID', 'Alert REV', 'Payload Data'])

        for section in sections:
            if "PACKET:" in section:
                # Extract Packet Data
                packet_data = re.findall(r'PACKET:\n([\s\S]*?)ALERT', section)[0].strip().replace('\n', ' ')
                
                # Extract Alert SID and REV
                alert_sid = re.findall(r'ALERT SID \[\d+\]:\s+(\d+)', section)[0].strip()
                alert_rev = re.findall(r'ALERT REV \[\d+\]:\s+(\d+)', section)[0].strip()
                
                # Extract Payload Data if available
                payload_data = ''
                payload_match = re.search(r'PAYLOAD:\n([\s\S]*?)(?:\+\=+|$)', section)
                if payload_match:
                    payload_data = payload_match.group(1).strip().replace('\n', ' ')
                
                # Write to CSV
                csv_writer.writerow([packet_data, alert_sid, alert_rev, payload_data])

# Usage
input_file = "processed_logs_suricata"  # Replace with your file name
output_csv = "output.csv"
parse_text_to_csv(input_file, output_csv)
