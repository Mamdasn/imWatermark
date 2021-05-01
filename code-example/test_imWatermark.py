import cv2, os
import numpy as np
from imWatermark import watermark

img_fullname="lotus.jpg"
img_fullname=f"assets/{img_fullname}"
img_name, img_ext = os.path.splitext(img_fullname)

img = cv2.imread(img_fullname)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
v = hsv[:, :, 2].copy()

v_watermark = watermark(v, 8)
    
hsv[:, :, 2] = v_watermark
img_out = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    
cv2.imwrite(f'{img_name}-watermark{img_ext}', img_out)
    









