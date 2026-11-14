import pdfplumber
import os

os.makedirs("extracted_raw_images", exist_ok=True)
with pdfplumber.open("Space Craft Cataloge.pdf") as pdf:
    for p_num in [1, 2, 8, 9]:
        page = pdf.pages[p_num - 1]
        for i, img in enumerate(page.images):
            try:
                # pdfplumber page.images contains stream info
                stream = img['stream']
                # let's get the raw image data if available
            except Exception as e:
                pass
print("Done")
