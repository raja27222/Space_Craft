import json

with open("pages_detailed.json", "r", encoding="utf-8") as f:
    pages = json.load(f)

for p in pages:
    page_num = p["page"]
    text = p["text"].replace("\n", " | ")
    prod_imgs = []
    for img in p["images"]:
        px = img["px_size"]
        bounds = img["bounds"]
        # Filter out tiny logos/icons (w < 150 or h < 100) or pure background watermarks if any
        prod_imgs.append(f"{px[0]}x{px[1]}@({bounds[0]:.0f},{bounds[1]:.0f})")
    print(f"P{page_num:02d} [{text}]: {', '.join(prod_imgs)}")
