import numpy as np
from imhist import imhist, imcdf

def watermark(img, levels=8):
    CDF = imcdf(img)
    locs = []
    for i in range(levels-1):
        P = (i+1)/levels
        loc = np.argmin(np.abs(CDF-P))
        if loc.size > 1 :
            loc = loc[0]
        if loc not in locs:
            locs.append(loc)
    locs.insert(0, 0)
    imgcopy = img.copy()
    for i in range(len(locs)-1):
        loc = locs[i+1]
        preloc = locs[i]
        imgcopy = np.where( np.invert((img>=preloc) & (img<loc)), imgcopy, preloc*np.ones_like(img))
    return imgcopy
