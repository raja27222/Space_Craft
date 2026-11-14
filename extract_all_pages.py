import pypdfium2 as pdfium
import json
import os
from PIL import Image

pdf = pdfium.PdfDocument("Space Craft Cataloge.pdf")
print("Total pages in PDF:", len(pdf))

os.makedirs("extracted_products", exist_ok=True)
os.makedirs("extracted_pages", exist_ok=True)

# First, render all 56 pages at 2x resolution (1920x1080) for high-definition slide views
for i in range(len(pdf)):
    page = pdf[i]
    rendered = page.render(scale=2.0).to_pil()
    rendered.save(f"extracted_pages/page_{i+1:02d}.jpg", quality=90)

print("All 56 pages rendered to extracted_pages/")
