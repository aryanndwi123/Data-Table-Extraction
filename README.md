## PDF Data Extraction and Rapid Prototyping
This project aims to extract key-value pairs from PDF files and images (such as JPG, JPEG, PNG, GIF, BMP, and WebP) using Optical Character Recognition (OCR). The extracted data is then saved to a CSV file for further analysis and processing. The project provides a web interface for users to upload files and view the extracted data.

### Prerequisites
Before running the project, make sure you have the following dependencies installed:

- Python (version 3.x)
- Flask
- pytesseract
- pdf2image
- pdfplumber
- Pillow
You also need to have Tesseract OCR installed on your system. Tesseract is an open-source OCR engine used for text recognition. You can download and install Tesseract from the following link:


- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

Make sure to install the appropriate version of Tesseract for your operating system.

Once you have installed Tesseract, you may need to set the Tesseract path in the `script.py` file if it's not in the default system path. Locate the following line in `script.py`:

```
pytesseract.pytesseract.tesseract_cmd = 'tesseract'
```
Replace `tesseract` with the actual path to the Tesseract executable.

You can install the required Python packages by running the following command:

```
pip install flask pytesseract pdf2image pdfplumber Pillow
```
### Project Structure
The project consists of the following files:

- `app.py`: This file contains the Flask application code, including the routes for handling file uploads and displaying the extracted data.
- `script.py`: This file contains the functions for extracting key-value pairs from PDF files and images using OCR. It also includes a function to save the extracted data to a CSV file.
- `index.html`: This HTML template defines the file upload form for users to submit their files.
- `display.html`: This HTML template displays the extracted data in a table format.
### Usage

1. Run the Flask application by executing the following command:
```
python app.py
```
2. Open a web browser and navigate to `http://localhost:5000` to access the file upload page.

3. Click on the "Choose File" button and select the PDF file or image file you want to extract data from.

4. Click the "Upload" button to submit the file. The application will extract the key-value pairs and save them to a CSV file.

5. After the extraction is complete, you will be redirected to the data display page, where you can view the extracted data in a table format.

* Note: The extracted data will be saved in the extracted_data.csv file in the project directory.

