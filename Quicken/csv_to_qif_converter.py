import sys

def convert_csv_to_qif(csv_file, qif_file):
    with open(csv_file, 'r') as f_csv, open(qif_file, 'w') as f_qif:
        # Write QIF header
        f_qif.write('!Type:Bank\n')

        # Read CSV and convert to QIF
        for line in f_csv:
            # Split CSV line into fields
            fields = line.strip().split(',')

            # Extract data from CSV fields
            date = fields[0]  # Assuming date is in the first column
            memo = fields[1]  # Assuming memo is in the second column
            amount = fields[2]  # Assuming amount is in the third column

            # Format date to MM/DD/YYYY
            month, day, year = date.split('/')
            date_qif = f"{month}/{day}/{year}"

            # Write transaction to QIF
            qif_entry = f"D{date_qif}\nT{amount}\nP\nM{memo}\n^\n"
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
