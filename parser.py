import re

def process_packet_capture(file_path, output_file_path):
    processed_lines = []

    with open(file_path, 'r') as file:
        for line in file:
            # List of line starts to skip
            skip_starts = [
                "TIME:", "PKT SRC:", "SRC IP:", "DST IP:", "PROTO:", 
                "SRC PORT:", "DST PORT:", "TCP SEQ:", "TCP ACK:", "FLOW:",
                "FLOW Start TS:", "FLOW PKTS TODST:", "FLOW PKTS TOSRC:",
                "FLOW Total Bytes:", "FLOW IPONLY SET:", "FLOW ACTION:",
                "FLOW NOINSPECTION:", "FLOW APP_LAYER", "FLOWBIT", "PACKET LEN",
                "ALERT CNT:", "ALERT MSG", "ALERT GID", "ALERT CLASS", 
                "ALERT PRIO", "ALERT FOUND IN", "ALERT IN TX", "PAYLOAD LEN", "FLOWINT", "STREAM DATA LEN"
            ]

            # Check if the line starts with any of the specified strings
            if any(line.startswith(start) for start in skip_starts):
                continue  # Skip this line
            elif line.startswith("ALERT SID") or line.startswith("ALERT REV"):
                processed_lines.append(line.strip())  # Keep these lines as is
            else:
                # Remove index numbers at the beginning of the line
                line = re.sub(r"^\s*\w{4}\s{2}", "", line)
                # Apply existing regex to the line
                processed_line = re.sub(r"\s{3,}.*$", "", line)
                processed_lines.append(processed_line.strip())

    # Join the processed lines
    processed_content = '\n'.join(processed_lines)

    # Write the processed content to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(processed_content)

# Paths for the input and output files
input_file_path = 'logs_suricata'
output_file_path = 'processed_logs_suricata'

# Process the packet capture and save the output to a file
process_packet_capture(input_file_path, output_file_path)


