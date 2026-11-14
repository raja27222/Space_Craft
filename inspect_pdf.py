import pdfplumber
import pypdfium2 as pdfium
import os
from PIL import Image

pdf = pdfium.PdfDocument("Space Craft Cataloge.pdf")
print("Total pages in pdfium:", len(pdf))

os.makedirs("extracted_previews", exist_ok=True)
for i in [0, 1, 7, 8, 17, 34, 49, 54]:
    page = pdf[i]
    image = page.render(scale=2.0).to_pil()
    image.save(f"extracted_previews/page_{i+1:02d}.jpg", quality=85)

print("Saved preview renders of pages 1, 2, 8, 9, 18, 35, 50, 55")
