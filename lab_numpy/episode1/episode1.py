import numpy as np
from PIL import Image

image_paths = [f"lunar_images/lunar0{i}_raw.jpg" for i in range(1, 4)]
for image_path in image_paths:
    img = Image.open(image_path)
    data = np.array(img)
    data = data - data.min()
    data = data * int(255 / data.max())

    res_img = Image.fromarray(data)
    res_img.save(image_path.replace("raw", "raw_new"))
