import cv2
from pyzbar.pyzbar import decode
import numpy as np

img=cv2.imread('qrcode.png')
data=decode(img)
for qrcode in decode(img):
    data=qrcode.data.decode('utf-8')
    print(data)