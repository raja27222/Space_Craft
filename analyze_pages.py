import pypdfium2 as pdfium
import pdfplumber
import json
import os
from PIL import Image

pdf = pdfium.PdfDocument("Space Craft Cataloge.pdf")
os.makedirs("extracted_products", exist_ok=True)

page_summary = []

with pdfplumber.open("Space Craft Cataloge.pdf") as plumb_pdf:
    for page_num in range(1, len(pdf) + 1):
        p_idx = page_num - 1
        page_pdfium = pdf[p_idx]
        page_plumb = plumb_pdf.pages[p_idx]
        
        text = page_plumb.extract_text() or ""
        
        img_objs = []
        for i, obj in enumerate(page_pdfium.get_objects()):
            if isinstance(obj, pdfium.PdfImage):
                bounds = obj.get_bounds()
                px = obj.get_px_size()
                # width and height in points
                w_pt = bounds[2] - bounds[0]
                h_pt = bounds[3] - bounds[1]
                img_objs.append({
                    "idx": i,
                    "bounds": bounds,
                    "px_size": px,
                    "w_pt": round(w_pt, 1),
                    "h_pt": round(h_pt, 1)
                })
        
        page_summary.append({
            "page": page_num,
            "text": text.strip(),
            "images": img_objs
        })

with open("pages_detailed.json", "w", encoding="utf-8") as f:
    json.dump(page_summary, f, indent=2)

print("Saved pages_detailed.json")
