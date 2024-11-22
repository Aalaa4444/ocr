from flask import Flask, request, jsonify
from ocr.ocr_model import *
from ocr.google_drive import *
from PIL import Image
from ocr.prerocess import *
from ocr.agent import *
app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_invoice():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    print(f"File received: {file.filename}") 

    file.save("uploaded_invoice.png")
    print("File saved as 'uploaded_invoice.png'") 

    try:
        from PIL import Image
        img = Image.open("uploaded_invoice.png")
        print("Image opened successfully") 
        j=extract_invoice_details(img)
        jsonify({"message": "File uploaded successfully"})
        agent = InvoiceAgent()
        validated_details = agent.validate_invoice_details(j)
        
        
    except Exception as e:
        print(f"Error opening image: {e}")
        return jsonify({"error": "Failed to process image"}), 500

    return jsonify(j,"validated_details",validated_details), 200

@app.route('/monitor-folder', methods=['GET'])
def monitor_folder():
    service = authenticate_drive()
    folder_id = '1sHTeNQX_QTP-EooQkXiVV2VtZfttoX8f'
    
    downloaded_files = load_downloaded_files() 
    jsonify({"message": "Monitoring folder triggered."}),200
    
    try:
        while True:
            jj= monitor(service, folder_id, downloaded_files)
            print(jj)
            save_downloaded_files(downloaded_files)
            time.sleep(60)  # Poll every minute
            jj= monitor(service, folder_id, downloaded_files)
            agent = InvoiceAgent()
            validated_details = agent.validate_invoice_details(jj)
            save_downloaded_files(downloaded_files)
            return jsonify(jj,"validated_details",validated_details),200
    except KeyboardInterrupt:
        print("Stopping monitoring.")
        save_downloaded_files(downloaded_files)
        return jsonify(jj,"validated_details",validated_details),200

if __name__ == "__main__":
    app.run(debug=True)
