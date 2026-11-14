import pypdfium2 as pdfium
from PIL import Image
import os

pdf = pdfium.PdfDocument("Space Craft Cataloge.pdf")
os.makedirs("test_crops", exist_ok=True)

# Let's see page 2 (Single sofa vip)
page = pdf[1]
# render high resolution (e.g. 3x or 4x scale: 960x3 = 2880 x 1620)
rendered = page.render(scale=3.0).to_pil()
rendered.save("test_crops/page_02_full.jpg", quality=92)
print("Rendered page 2 size:", rendered.size)

# From our check_images.py on page 2:
# img 3: x0=21.5, y0=54.2, x1=296.8, y1=329.4
# img 0: x0=342.2, y0=54.0, x1=618.6, y1=330.3
# img 5: x0=663.0, y0=54.2, x1=938.3, y1=329.5
# Note: in PDF coordinates (0,0) is bottom-left or top-left depending on convention.
# Let's check how pdfplumber y0/y1 maps to rendered PIL image (which has (0,0) top-left).
w_scale = rendered.width / 960.0
h_scale = rendered.height / 540.0

crop1 = rendered.crop((21.5 * w_scale, 54.2 * h_scale, 296.8 * w_scale, 329.4 * h_scale))
crop1.save("test_crops/page_02_sofa1.jpg", quality=92)

crop2 = rendered.crop((342.2 * w_scale, 54.0 * h_scale, 618.6 * w_scale, 330.3 * h_scale))
crop2.save("test_crops/page_02_sofa2.jpg", quality=92)

crop3 = rendered.crop((663.0 * w_scale, 54.2 * h_scale, 938.3 * w_scale, 329.5 * h_scale))
crop3.save("test_crops/page_02_sofa3.jpg", quality=92)

print("Saved 3 crops from page 2")
