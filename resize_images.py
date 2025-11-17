# resize_images.py
from PIL import Image
import os

folders = ['static/shirts', 'static/hats', 'static/sneakers']
max_width = 1200
quality = 80

for folder in folders:
    if not os.path.isdir(folder):
        print("Skip, folder not found:", folder)
        continue
    for fname in os.listdir(folder):
        path = os.path.join(folder, fname)
        if not (fname.lower().endswith('.jpg') or fname.lower().endswith('.jpeg') or fname.lower().endswith('.png')):
            continue
        try:
            img = Image.open(path)
            w,h = img.size
            if w > max_width:
                new_h = int(max_width * h / w)
                img = img.resize((max_width, new_h), Image.LANCZOS)
            # re-save as JPEG to reduce size if PNG -> JPG conversion
            rgb = img.convert('RGB')
            rgb.save(path, 'JPEG', quality=quality, optimize=True)
            print("Saved:", path)
        except Exception as e:
            print("Error:", path, e)
