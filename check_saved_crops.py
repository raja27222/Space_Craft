from PIL import Image

for name in ["obj_0.png", "obj_15.png", "obj_17.png", "obj_13.png", "obj_16.png"]:
    img = Image.open(f"test_crops/{name}")
    print(f"{name}: size={img.size}, mode={img.mode}, bbox={img.getbbox()}")
