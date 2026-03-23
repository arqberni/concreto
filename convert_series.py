import os
import glob
from PIL import Image
import pillow_avif

base_dir = r"D:\CONTENIDO PARA WEB\concreto\antigrav\concreto-favicon"
img_dir = os.path.join(base_dir, "img")
patterns = ["a*.jpg", "a*.jpeg", "a*.png",
            "b*.jpg", "b*.jpeg", "b*.png",
            "d*.jpg", "d*.jpeg", "d*.png",
            "l*.jpg", "l*.jpeg", "l*.png",
            "r*.jpg", "r*.jpeg", "r*.png"]

count = 0
for pattern in patterns:
    for path in glob.glob(os.path.join(img_dir, pattern)):
        base_name = os.path.splitext(path)[0]
        avif_path = base_name + ".avif"
        if os.path.exists(avif_path):
            print(f"Skipping {path}, {avif_path} already exists")
            continue
        print(f"Converting {path} to {avif_path}")
        try:
            with Image.open(path) as im:
                if im.mode in ("RGBA", "P"): 
                    im = im.convert("RGB")
                im.save(avif_path, format="AVIF", quality=50)
                count += 1
        except Exception as e:
            print(f"Error {path}: {e}")

print(f"Converted {count} successful files.")
