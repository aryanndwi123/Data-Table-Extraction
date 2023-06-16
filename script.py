# Importing required modules
import pytesseract
from PIL import Image
import pdf2image
import os
import csv
import pdfplumber

# Function to extract key value pair from pdf and image files
def extract_key_value_pairs(filename):
    # Extracting file extension
    file_extension = os.path.splitext(filename)[1].lower()
    extracted_data = []

    # Checking if file is pdf
    if file_extension==".pdf":
        with pdfplumber.open(filename) as pdf:
            for page in pdf.pages:

                # Converting pdf to image
                images = pdf2image.convert_from_path(filename)
                text = ""

                # Extracting text from images
                for page in images:
                    text += pytesseract.image_to_string(page)
                    lines = text.split("\n")

                    # Extracting key-value pairs from text
                    for line in lines:
                        if ":" in line:
                            key, value = line.split(":", 1)
                            extracted_data.append({"Key": key, "Value": value})
                return extracted_data
            
    # Checking if file is image
    elif file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp','.webp']:
        image = Image.open(filename)
        image_text = pytesseract.image_to_string(image)
        table_data = [row.split("\t") for row in image_text.split("\n")]
        lines = table_data

        # Extracting key-value pairs from table data
        for line in lines:
            if ":" in line[0]:
                key, value = line[0].split(":",1)
                extracted_data.append({"Key": key.strip(), "Value": value.strip()})
        return extracted_data
    else:
        return "File not found"


def save_to_csv(data, filename):
    # Retrieving keys from the data
    keys = data[0].keys() if data else []

    # Saving Key-Value pairs to csv file
    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)