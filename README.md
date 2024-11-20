# OCR 
This repository contains a Flask-based API for processing invoices using OCR (Optical Character Recognition). The API provides endpoints for uploading images of invoices and monitoring a Google Drive folder for new files.

## Features
* Upload Invoice: Accepts an invoice image and extracts details using OCR.
* Monitor Google Drive Folder: Monitors a specified Google Drive folder for new files and processes them.
## Requirements
Ensure the following dependencies are installed before running the application:

* Python 3.7+
* Flask
* Google API Client (google-api-python-client)
* Pillow (PIL)
```bash
pip install flask google-api-python-client pillow
```
## Setup and Usage
1. Clone this repository:
```bash
git clone https://github.com/Aalaa4444/ocr.git

cd ocr
```
2. Configure Google Drive API:

Set up Google Drive API credentials.
Save the client_secret.json file in the ocr sub-directory.
3. Run the Flask app:

```bash
python app.py
```
python app.py
4. Access the endpoints:

* Upload Invoice: Use a tool like Postman to send a POST request to /upload.
* Monitor Folder: Send a GET request to /monitor-folder.
