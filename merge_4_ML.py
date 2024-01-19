import csv

def parse_suricata_rules(file_path):
    rules = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split(';')
            sid = None
            rev = None
            for part in parts:
                if part.strip().startswith('sid:'):
                    sid = part.split(':')[1].strip()
                elif part.strip().startswith('rev:'):
                    rev = part.split(':')[1].strip()
            if sid and rev:
                rules[(sid, rev)] = line.strip()
    return rules

def append_suricata_rule_to_csv(csv_file_path, txt_file_path, output_csv_file_path):
    suricata_rules = parse_suricata_rules(txt_file_path)
    with open(csv_file_path, 'r') as csv_file, open(output_csv_file_path, 'w', newline='') as output_file:
        reader = csv.DictReader(csv_file)
        fieldnames = reader.fieldnames + ['Suricata_rule']
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            sid_rev_pair = (row['Alert SID'].strip(), row['Alert REV'].strip())
            suricata_rule = suricata_rules.get(sid_rev_pair, '')
            row['Suricata_rule'] = suricata_rule
            writer.writerow(row)

# Example usage
csv_file_path = 'output.csv'
txt_file_path = 'Tpot_suricata_rules' #this is the file with the tpot suricata rules from the zip file. 
output_csv_file_path = 'mergedML.csv'
append_suricata_rule_to_csv(csv_file_path, txt_file_path, output_csv_file_path)
