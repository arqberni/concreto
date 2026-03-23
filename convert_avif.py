import os
import glob
from PIL import Image
import pillow_avif

img_dir = "img"
patterns = ["*.jpg", "*.jpeg", "*.png", "*.JPG", "*.JPEG", "*.PNG"]

count = 0
for pattern in patterns:
    for path in glob.glob(os.path.join(img_dir, pattern)):
        base_name = os.path.splitext(path)[0]
        avif_path = base_name + ".avif"
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
