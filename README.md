# OCR 
This project uses Optical Character Recognition (OCR) with Tesseract and image processing techniques to extract invoice details from invoice image. The extracted details include the invoice number, date, total amount, product costs, discount, and final cost. The Flask API provides endpoints for uploading images of invoices and monitoring a Google Drive folder for new files.
## Features
* Tesseract OCR Fine-Tune: Extracts arabic (with fine-tuned traindata) and english numbers from image.
* Image Preprocessing.
* Upload Invoice: Accepts an invoice image and extracts details using OCR.
* Monitor Google Drive Folder: Monitors a specified Google Drive folder for new files and processes them.
## Requirements
Ensure the following dependencies are installed before running the application:

* Python 3.7+
* Flask
* Google API Client (google-api-python-client)
* Pillow (PIL)
```bash
pip install flask google-api-python-client google-auth-httplib2 google-auth-oauthlib pillow pytesseract numpy opencv-python matplotlib
```
* Install Tesseract and ensure the executable path is correctly configured
```bash
pytesseract.tesseract_cmd = r'D:\blackboard\AI_online\cloudilic\tesseract.exe'
```
* ara_num_lolo.traindata
custom OCR model ara_num_lolo is still being fine-tuned, and I will release it soon for public use.
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

## Google Drive API Setup
1. Google Drive API Credentials:

Enable the Google Drive API in your Google Cloud project.
Download the client_secret.json file and place it in the project directory.
2. Token File:

The script generates a token.json file during authentication. Keep this file secure.
