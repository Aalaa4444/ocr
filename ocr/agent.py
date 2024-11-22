import re
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)

class InvoiceAgent:
    def __init__(self):
        self.patterns = {
            "invoice_number": r".{1,7}",
            "date": r"\b(\d{2}[/-]\d{2}[/-]\d{4})\b",  # 12-11-2024 or 12/11/2024
        }
    
    def validate_invoice_details(self, details):
        refined_details = {}
        for field, value in details.items():
            if field in self.patterns:
                match = re.search(self.patterns[field], value) if value else None
                refined_details[field] = match.group(0) if match else "Invalid"
            else:
                refined_details[field] = value
            if field == "second_product_cost":
                refined_details[field] = value[3:]

        logging.info("Validation completed for invoice details.")
        return refined_details
