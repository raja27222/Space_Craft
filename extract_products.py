import pypdfium2 as pdfium
import json
import os
import re
from PIL import Image

pdf = pdfium.PdfDocument("Space Craft Cataloge.pdf")
out_img_dir = "public/images/products"
out_pages_dir = "public/images/catalog_pages"
os.makedirs(out_img_dir, exist_ok=True)
os.makedirs(out_pages_dir, exist_ok=True)

# Also save high-res full page slides to public/images/catalog_pages
for i in range(len(pdf)):
    page_img = pdf[i].render(scale=2.0).to_pil()
    page_img.save(f"{out_pages_dir}/page_{i+1:02d}.jpg", quality=88)

print("Saved catalog page slides to", out_pages_dir)

# Now inspect and extract individual product photos
extracted_items = []

# List of ignore signatures:
# background decor: bounds around (0,0) or (0,1) with size ~477x496
# corner icons: width < 150 and height < 120, or position y < 70 and x > 600

with open("pages_detailed.json", "r", encoding="utf-8") as f:
    pages_data = json.load(f)

for p_data in pages_data:
    page_num = p_data["page"]
    text = p_data["text"]
    p_idx = page_num - 1
    page = pdf[p_idx]
    
    # We will extract valid product images from this page
    page_prod_imgs = []
    
    # Get all image objects
    for i, obj in enumerate(page.get_objects()):
        if isinstance(obj, pdfium.PdfImage):
            bounds = obj.get_bounds()
            px = obj.get_px_size()
            w_pt = bounds[2] - bounds[0]
            h_pt = bounds[3] - bounds[1]
            
            # Filter decorative elements:
            # 1. tiny corner icons/page numbers:
            if px[0] < 120 or px[1] < 100:
                continue
            # 2. Page number small stamps or icons:
            if w_pt < 40 and h_pt < 40:
                continue
            # 3. Known background decorative overlay at (0,0) or (0,1)
            if bounds[0] < 5 and bounds[1] < 5 and px[0] in [477] and px[1] in [495, 496]:
                continue
            # 4. Small side watermark (180x280 at x=0, y=126):
            if bounds[0] < 5 and bounds[1] > 100 and px[0] == 180 and px[1] == 280:
                continue
            # 5. Small stamp at bottom right (190x135 at x=630, y=450):
            if bounds[0] > 600 and bounds[1] > 400 and px[0] == 190 and px[1] == 135:
                continue
            
            # This is a genuine product image!
            try:
                bitmap = obj.get_bitmap()
                pil_img = bitmap.to_pil()
                img_name = f"product_p{page_num:02d}_img{len(page_prod_imgs)+1}.png"
                img_path = f"{out_img_dir}/{img_name}"
                pil_img.save(img_path)
                
                page_prod_imgs.append({
                    "filename": img_name,
                    "web_path": f"/images/products/{img_name}",
                    "width": pil_img.width,
                    "height": pil_img.height,
                    "bounds": bounds
                })
            except Exception as e:
                print(f"Error extracting image on page {page_num}: {e}")
                
    extracted_items.append({
        "page": page_num,
        "text": text,
        "product_images": page_prod_imgs
    })

print(f"Processed {len(extracted_items)} pages.")
total_prod_images = sum(len(x["product_images"]) for x in extracted_items)
print(f"Total authentic product images extracted: {total_prod_images}")
