import pypdfium2 as pdfium

pdf = pdfium.PdfDocument("Space Craft Cataloge.pdf")
page = pdf[1]
for i, obj in enumerate(page.get_objects()):
    if isinstance(obj, pdfium.PdfImage):
        bounds = obj.get_bounds()
        px_size = obj.get_px_size()
        bitmap = obj.get_bitmap()
        pil_img = bitmap.to_pil()
        print(f"Image obj {i}: bounds={bounds}, px_size={px_size}, pil_size={pil_img.size}, mode={pil_img.mode}")
        pil_img.save(f"test_crops/obj_{i}.png")
