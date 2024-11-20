import time
from datetime import datetime
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
import io
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials 
import json
from ocr.ocr_model import *
# Scope required for accessing Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive']

def authenticate_drive():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)  
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret2.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    service = build('drive', 'v3', credentials=creds)
    return service

def download_file(service, file_id, file_name):
    file = service.files().get(fileId=file_id).execute()
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(file_name, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
        print(f"Download {int(status.progress() * 100)}%.")
    
    print(f"File {file_name} downloaded successfully!")

def load_downloaded_files():
    if os.path.exists("downloaded_files.json"):
        with open("downloaded_files.json", "r") as f:
            return set(json.load(f))
    return set()

def save_downloaded_files(downloaded_files):
    with open("downloaded_files.json", "w") as f:
        json.dump(list(downloaded_files), f)
def is_image(file_name):
    image_extensions = {'.jpeg', '.jpg', '.png', '.gif', '.bmp', '.webp', '.tiff', '.tif'}
    _, file_extension = os.path.splitext(file_name.lower()) 
    return file_extension in image_extensions

def monitor(service, folder_id, downloaded_files):
    query = f"'{folder_id}' in parents" 
    json_files = []
    
    try:
        results = service.files().list(q=query).execute()
        items = results.get('files', [])
        
        if items:
            print(f"Found {len(items)} file(s) in the folder.")
            for item in items:
                file_id = item['id']
                file_name = item['name']
                if file_id not in downloaded_files:
                    print(f"- Downloading new file: {file_name} (ID: {file_id})")
                    download_file(service, file_id, file_name)
                    downloaded_files.add(file_id)
                    if is_image(file_name):
                        from PIL import Image
                        image = Image.open(file_name)
                        j=extract_invoice_details(image)
                        json_files.append(j)
                        
                    elif not is_image(file_name):
                        print(f"- Skipping non-image file: {file_name}")


        else:
            print("No files found in the folder.")
    except HttpError as error:
        print(f"An error occurred: {error}")
    return json_files

if __name__ == "__main__":
    service = authenticate_drive()
    folder_id = '1sHTeNQX_QTP-EooQkXiVV2VtZfttoX8f'
    
    downloaded_files = load_downloaded_files() 
    
    try:
        while True:
            jj=monitor(service, folder_id, downloaded_files)
            print(jj)
            save_downloaded_files(downloaded_files)
            time.sleep(60)  # Poll every minute
    except KeyboardInterrupt:
        print("Stopping monitoring.")
        save_downloaded_files(downloaded_files)