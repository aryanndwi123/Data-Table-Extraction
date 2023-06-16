from flask import Flask, render_template, request, redirect, url_for
import os
from script import extract_key_value_pairs,save_to_csv
import csv
app = Flask(__name__)

# Configure a folder to store uploaded files
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    # Rendering index paeg
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        # Save the uploaded file to the UPLOAD_FOLDER
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Extract key-value pairs from the file
        extracted_data = extract_key_value_pairs(file_path)
        if isinstance(extracted_data, str):
            return extracted_data
        
        csv_filename = 'extracted_data.csv'
        # Saving the extracted data to the CSV file
        save_to_csv(extracted_data, csv_filename)

        # Redirecting to display url
        return redirect(url_for('display', csv_file=csv_filename))
    else:
        
        return "No file uploaded"

@app.route('/display/<csv_file>')
def display(csv_file):
    data = []
    with open(csv_file, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return render_template('display.html', data=data)

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
