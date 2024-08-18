def convert_csv_to_qif(csv_file, qif_file):
    with open(csv_file, 'r') as f_csv, open(qif_file, 'w') as f_qif:
        # Write QIF header
        f_qif.write('!Type:Bank\n')

        # Read CSV and convert to QIF
        for line in f_csv:
            # Split CSV line into fields
            fields = line.strip().split(',')

            # Ensure there are enough fields
            if len(fields) < 3 or not fields[0]:
                print(f"Skipping line due to invalid format: {line}")
                continue

            # Extract data from CSV fields
            date = fields[0]
            memo = fields[1]
            amount = fields[2]

            try:
                # Split the date by "/"
                parts = date.split('/')
                
                # Ensure the date has month, day, and year
                if len(parts) == 3:
                    month, day, year = parts
                else:
                    raise ValueError("Incorrect date format")
                    
                # Pad month and day with leading zeros if necessary
                month = month.zfill(2)
                day = day.zfill(2)

            except ValueError as e:
                print(f"Skipping line due to incorrect date format: {date} ({e})")
                continue

            # Write transaction to QIF
            date_qif = f"{month}/{day}/{year}"
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
