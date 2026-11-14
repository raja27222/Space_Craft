import pdfplumber

with pdfplumber.open("Space Craft Cataloge.pdf") as pdf:
    for p_num in [1, 2, 8, 9, 18, 35, 50, 55]:
        page = pdf.pages[p_num - 1]
        print(f"=== Page {p_num} ===")
        print("Page bbox:", page.bbox)
        for i, img in enumerate(page.images):
            print(f"  img {i}: x0={img['x0']:.1f}, y0={img['y0']:.1f}, x1={img['x1']:.1f}, y1={img['y1']:.1f}, w={img['width']:.1f}, h={img['height']:.1f}")
