import os
import glob
from PIL import Image
import pillow_avif

for i in range(5, 14):
    path = f"img/barc{i}.jpg"
    avif_path = f"img/barc{i}.avif"
    if os.path.exists(path):
        print(f"Converting {path} to {avif_path}")
        try:
            with Image.open(path) as im:
                if im.mode in ("RGBA", "P"): 
                    im = im.convert("RGB")
                im.save(avif_path, format="AVIF", quality=50)
        except Exception as e:
            print(f"Error {path}: {e}")
print("Finished formatting barc5 to barc13")
