from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        from ofxparse import OfxParser

        # Get the paths of uploaded files from the form
        ofx_file = request.files['ofx_file']
        ofx_file_path = 'uploads/input.ofx'
        ofx_file.save(ofx_file_path)

        qif_file_path = 'output.qif'

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

        return f"Conversion successful. <a href='/download'>Download QIF file</a>"
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/download')
def download():
    return send_file('output.qif', as_attachment=True)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
