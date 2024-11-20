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
pip install flask google-api-python-client pillow
