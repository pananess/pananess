import pandas as pd

def parse_qif(file_path):
    transactions = []
    with open(file_path, 'r') as file:
        transaction = {}
        for line in file:
            line = line.strip()
            if line.startswith('D'):
                transaction['Date'] = line[1:]
            elif line.startswith('T'):
                transaction['Amount'] = line[1:]
            elif line.startswith('P'):
                transaction['Payee'] = line[1:]
            elif line.startswith('M'):
                transaction['Memo'] = line[1:]
            elif line.startswith('L'):
                transaction['Category'] = line[1:]
            elif line == '^':
                transactions.append(transaction)
                transaction = {}
    return transactions

def qif_to_excel(qif_file, excel_file):
    transactions = parse_qif(qif_file)
    df = pd.DataFrame(transactions)
    df.to_excel(excel_file, index=False)

# Example usage
qif_file = 'file.qif'
excel_file = 'file.xlsx'
qif_to_excel(qif_file, excel_file)