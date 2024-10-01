import sys

def convert_csv_to_qif(csv_file, qif_file):
    with open(csv_file, 'r') as f_csv, open(qif_file, 'w') as f_qif:
        # Write QIF header
        f_qif.write('!Type:Bank\n')

        # Skip the header row in CSV
        next(f_csv)

        # Read CSV and convert to QIF
        for line in f_csv:
            # Split CSV line into fields
            fields = line.strip().split(',')

            # Check if the number of fields is correct (i.e., at least 4 fields)
            if len(fields) < 4:
                print(f"Skipping line due to missing fields: {line}")
                continue  # Skip lines that do not have enough fields

            # Extract data from CSV fields
            date = fields[0]  # Date in first column
            payee = fields[1] if fields[1].strip() else ''  # Handle missing payee (allow empty)
            description = fields[2]  # Description in third column
            amount = fields[3]  # Amount in fourth column

            # Format date from MM/DD/YYYY
            month, day, year = date.split('/')
            date_qif = f"{month}/{day}/{year}"

            # Write transaction to QIF, allowing empty Payee if necessary
            qif_entry = f"D{date_qif}\nT{amount}\nP{payee}\nM{description}\n^\n"
            f_qif.write(qif_entry)

if __name__ == "__main__":
    # Check if correct number of command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python csv_to_qif_converter.py input_csv_file output_qif_file")
        sys.exit(1)

    # Get input CSV file and output QIF file from command-line arguments
    input_csv_file = sys.argv[1]
    output_qif_file = sys.argv[2]

    # Call the conversion function with provided filenames
    convert_csv_to_qif(input_csv_file, output_qif_file)
