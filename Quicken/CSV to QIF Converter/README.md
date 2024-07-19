
# OFX to QIF and CSV to QIF Converter Documentation

## Overview

This project contains two scripts to convert financial data from different formats into QIF (Quicken Interchange Format). 

1. **app.py** - A Flask web application to convert OFX files to QIF.
2. **csv_to_qif_converter.py** - A command-line script to convert CSV files to QIF.

## Requirements

Before running the scripts, make sure to install the required packages. You can do this using `pip`:

```sh
pip install Flask ofxparse
```

## 1. app.py - OFX to QIF Converter

This is a Flask web application that provides an interface to upload an OFX file and convert it to a QIF file.

### How to Run

1. Save the `app.py` script to your project directory.
2. Create a folder named `templates` in the same directory.
3. Inside the `templates` folder, create an `index.html` file with the following content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>OFX to QIF Converter</title>
</head>
<body>
    <h1>OFX to QIF Converter</h1>
    <form action="/convert" method="post" enctype="multipart/form-data">
        <label for="ofx_file">Upload OFX file:</label>
        <input type="file" name="ofx_file" id="ofx_file">
        <button type="submit">Convert</button>
    </form>
</body>
</html>
```

4. Run the Flask application:

```sh
python app.py
```

5. Open your web browser and go to `http://127.0.0.1:5000/`. You will see an interface to upload an OFX file and convert it to QIF.

### File Structure

- **app.py** - Main Flask application script.
- **templates/index.html** - HTML template for the upload form.

### How It Works

- The user uploads an OFX file using the form on the homepage.
- The `/convert` endpoint handles the file upload and conversion using the `ofxparse` library.
- The converted QIF file is saved to the server.
- The user can download the QIF file from the `/download` endpoint.

### Error Handling

If an error occurs during the conversion, an error message is displayed on the webpage.

## 2. csv_to_qif_converter.py - CSV to QIF Converter

This is a command-line script that converts CSV files to QIF format.

### How to Run

1. Save the `csv_to_qif_converter.py` script to your project directory.
2. Run the script from the command line with the following arguments:

```sh
python csv_to_qif_converter.py input_csv_file output_qif_file
```

### Arguments

- **input_csv_file**: Path to the input CSV file.
- **output_qif_file**: Path to the output QIF file.

### Example

```sh
python csv_to_qif_converter.py transactions.csv transactions.qif
```

### How It Works

- The script reads the CSV file line by line.
- Each line is split into fields, and the date, memo, and amount are extracted.
- The date is formatted to `MM/DD/YYYY`.
- Each transaction is written to the QIF file in the appropriate format.

### CSV Format

The CSV file should have the following columns in order:
1. **Date** (MM/DD/YYYY)
2. **Memo** (Description of the transaction)
3. **Amount** (Transaction amount)

## Conclusion

These scripts provide a simple way to convert financial data from OFX and CSV formats to QIF, making it easier to import into financial software like Quicken.

Feel free to contribute to the project or suggest improvements.
