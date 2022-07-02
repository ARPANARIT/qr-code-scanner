from tkinter.tix import Tree
import cv2
from pyzbar.pyzbar import decode
import numpy as np

capture= cv2.VideoCapture(0)
received_data=None

while True:
    _,frame=capture.read()
    for qrcode in decode(frame):
        data=qrcode.data.decode('utf-8')
        if data!=received_data:
            print(data)
            received_data=data
        points=np.array([qrcode.polygon],np.int32)
        points=points.reshape((-1,1,2))
        cv2.polylines(frame,[points],True,(0,255,0),5)
        points2=qrcode.rect
        cv2.putText(frame,data,(points2[0],points2[1]),cv2.FONT_HERSHEY_COMPLEX,0.9,(255,255,0))

     
    cv2.imshow('QR Code Scanner',frame)
    key=cv2.waitKey(1)
    if key==ord('q'): 
        break
