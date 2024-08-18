import csv
from datetime import datetime

def convert_csv_to_qif(csv_file, qif_file):
    # Open the CSV file for reading
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        # Open the QIF file for writing
        with open(qif_file, 'w') as qiffile:
            qiffile.write('!Type:Bank\n')  # Set the QIF type to Bank account
            
            for row in reader:
                # Convert the date to the format required by QIF
                date = datetime.strptime(row['Date'], '%m/%d/%Y').strftime('%m/%d/%Y')

                # Write the transaction data to the QIF file
                qiffile.write(f'D{date}\n')
                qiffile.write(f'P{row["Payee"]}\n')
                if row["Memo"]:  # Only write memo if it's not empty
                    qiffile.write(f'M{row["Memo"]}\n')
                qiffile.write(f'L{row["Category"]}\n')
                qiffile.write(f'T{row["Amount"]}\n')
                qiffile.write('^\n')  # End of transaction

# Example usage
csv_file = 'transactions.csv'
qif_file = 'transactions.qif'
convert_csv_to_qif(csv_file, qif_file)
