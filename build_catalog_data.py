import json
import os
import re

# Load pages data
with open("pages_detailed.json", "r", encoding="utf-8") as f:
    pages_data = json.load(f)

# Inspect extracted files per page
extracted_files = {}
for fname in os.listdir("public/images/products"):
    # filename pattern: product_p{page:02d}_img{idx}.png
    m = re.match(r"product_p(\d+)_img(\d+)\.png", fname)
    if m:
        p_num = int(m.group(1))
        if p_num not in extracted_files:
            extracted_files[p_num] = []
        extracted_files[p_num].append(f"/images/products/{fname}")

# Let's map each page to products
# Page 1 is cover
# Pages 2-5: Single Sofa VIP
# Page 6: Chair
# Page 7: VIP Chair (9)
# Page 8: VIP Chair (H=90 W=65 SIDE=67)
# Page 9: VIP Bentley Chair (Quantity Available: 500)
# Page 10: VIP Chair
# Page 11: VIP Chair (W=72 H=93)
# Page 12: VIP Chair (W=55 H=93)
# Page 13: VIP Chair (W=55 H=93)
# Page 14: VIP Chair (W=55 H=93)
# Page 15: VIP Chair
# Page 16: Chair (W=50 H=96)
# Page 17: Conference Chair (W=70 H=75)
# Page 18: VIP Leather Sofa (W=70 H=70)
# Page 19: VIP Leather Sofa
# Page 20: Dinner Chair (W=60 H=95)
# Page 21: Dinner Chair (W=50 H=80)
# Page 22: Dinner Chair (QTY=1000)
# Page 23: Dinner Chair (W=60 H=60)
# Page 24: Fabric Cover Chair (W=70 H=90, QTY=1500)
# Page 25: Chair (W=43 H=80)
# Page 26: Chair (W=45 H=80)
# Page 27: Dining Chair
# Page 28: Plastic Chair
# Page 29: VIP Single Sofa (W=75 H=90)
# Page 30: Chair
# Page 31: Office Chair
# Page 32: Conference Chair and Table
# Page 33: Office Chair
# Page 34: Bean Bag
# Page 35: Outdoor Items
# Page 36: Outdoor Items
# Page 37: High Chair / High Table
# Page 38: High Chair / High Table
# Page 39: High Chair / High Table
# Page 40: High Chair / High Table
# Page 41: High Chair / High Table
# Page 42: Outdoor (+966 57 177 9065)
# Page 43: High Table
# Page 44: Table
# Page 45: Table
# Page 46: Table
# Page 47: Table
# Page 48: Table
# Page 49: AC and Heater
# Page 50: Wedding Curtains
# Page 51: Curtain
# Page 52: Wedding Curtains
# Page 53: Wedding Curtain
# Page 54: Screen
# Page 55: Crowd Control
# Page 56: VIP Entrance

print(f"Extracted files map has {len(extracted_files)} pages with product photos.")
