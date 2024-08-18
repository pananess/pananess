from ofxparse import OfxParser

def convert_ofx_to_qif(ofx_file_path, qif_file_path):
    try:
        with open(ofx_file_path, 'rb') as ofx_file:
            ofx = OfxParser.parse(ofx_file)

            with open(qif_file_path, 'w') as qif_file:
                qif_file.write('!Type:Bank\n')

                for transaction in ofx.account.statement.transactions:
                    qif_file.write('D' + transaction.date.strftime('%m/%d/%Y') + '\n')
                    qif_file.write('T' + str(transaction.amount) + '\n')
                    qif_file.write('P' + transaction.payee + '\n')
                    qif_file.write('M' + transaction.memo + '\n')
                    qif_file.write('^\n')

        print(f"Conversion successful. QIF file created at {qif_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
convert_ofx_to_qif('input.ofx', 'output.qif')
