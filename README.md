[![PyPI Latest Release](https://img.shields.io/pypi/v/imWatermark.svg)](https://pypi.org/project/imWatermark/)
[![Package Status](https://img.shields.io/pypi/status/imWatermark.svg)](https://pypi.org/project/imWatermark/)
[![Downloads](https://pepy.tech/badge/imWatermark)](https://pepy.tech/project/imWatermark)
[![License](https://img.shields.io/pypi/l/imWatermark.svg)](https://github.com/Mamdasn/imWatermark/blob/main/LICENSE)
![Repository Size](https://img.shields.io/github/repo-size/mamdasn/imWatermark)

# imWatermark
This snippet of code attempts to watermark images.


## Installation

Run the following to install:

```python
pip install imWatermark
```

## Usage
```python
import cv2 
import numpy as np
from imWatermark import watermark

img_fullname="assets/lotus.jpg"

img = cv2.imread(img_fullname)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
v = hsv[:, :, 2].copy()

v_watermark = watermark(v, 8)
    
hsv[:, :, 2] = v_watermark
img_out = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    
cv2.imwrite('assets/lotus-watermark.jpg', img_out)
```
## Output
This is a sample image:  
!["Sample Image"](https://raw.githubusercontent.com/Mamdasn/imWatermark/main/assets/lotus.jpg "Sample Image")  
This is the sample image watermarked:  
![Watermarked Sample Image](https://raw.githubusercontent.com/Mamdasn/imWatermark/main/assets/lotus-watermark.jpg "Watermarked Sample Image")
