import pytesseract
from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt
from pytesseract import *
import cv2
from ocr.prerocess import *
#pytesseract.tesseract_cmd = r'D:\blackboard\AI_online\cloudilic\tesseract.exe'
def extract_invoice_details(image):

    pytesseract.tesseract_cmd = r'D:\blackboard\AI_online\cloudilic\tesseract.exe'

    from PIL import Image

    #image = Image.open('WhatsApp Image 2024-11-14 at 8.41.26 PM (1).jpeg')
    gray_image = ImageOps.grayscale(image)

    gray_array = np.array(gray_image)

    # Detect row lines by finding rows with significant changes in pixel values
    row_lines = []
    threshold = 75  # Threshold for detecting significant changes

    for y in range(1, gray_array.shape[0]):
        if np.abs(np.mean(gray_array[y]) - np.mean(gray_array[y - 1])) > threshold:
            row_lines.append(y)

    # Add the last row as the end of the last segment
    row_lines.append(gray_array.shape[0])

    # Cut the image based on detected row lines
    cut_images = []
    start_row = 0

    for end_row in row_lines:
        cut_image = image.crop((0, start_row, image.width, end_row))
        cut_images.append(cut_image)
        start_row = end_row
    #*****************************************************************************first place
    selected_image = cut_images[6]

    img1 = np.array(selected_image)
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    res = pytesseract.image_to_string(gray1, lang="ara_num_lolo").split()
    if not res[2]:
        invoice_num="invalid"
    else:
        invoice_num=res[2]
    res = pytesseract.image_to_string(gray1, lang='eng').split()
    if not res[0]:
        date="invalid"
    else:
        date=res[0]
    print(invoice_num)
    print(date)
    #*****************************************************************************second place
    selected_image = cut_images[12]

    img = np.array(selected_image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    space1 = gray[:, 290:290+45]
    t=threshold_eng_num(space1)
    t=detect_digit_only(t).split()
    if not t[0]:
        total_amount="invalid"
    else:
        total_amount=t[0]
    print(total_amount)
    #*****************************************************************************third place
    selected_image = cut_images[10]
    img = np.array(selected_image)
    cut=img[:,340:420]
    denoised_image = cv2.bilateralFilter(cut, 9, 75, 75)

    gray = cv2.cvtColor(denoised_image, cv2.COLOR_BGR2GRAY)

    enhanced_image = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    # Sharpen the image
    kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])
    sharpened_image = cv2.filter2D(enhanced_image, -1, kernel)
    res=pytesseract.image_to_string(enhanced_image, lang="ara_num_lolo").split()
    if not res[1]:
        second_prod_cost="invalid"
    else:
        second_prod_cost=res[1]
    print(second_prod_cost)
    #*****************************************************************************Add
    selected_image = cut_images[16]

    img = np.array(selected_image)
    cut=img[:20,115:155]
    res=pytesseract.image_to_string(cut, lang="ara_num_lolo").split()
    if not res[0]:
        discount="invalid"
    else:
        discount=res[0]
    cut=img[20:50,110:155]
    res=pytesseract.image_to_string(cut, lang="ara_num_lolo").split()
    if not res[0]:
        final_cost="invalid"
    else:
        final_cost=res[0]
    print(discount)
    print(final_cost)
    

    invoice_details = {
    "invoice_number": invoice_num,
    "date":date,
    "second_product_cost":second_prod_cost,
    "total_amount":total_amount,
    "discount": discount,
    "final_cost":final_cost
    }
    
    
    return invoice_details