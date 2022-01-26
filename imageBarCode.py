import cv2
import numpy as np
from pyzbar.pyzbar import decode

def getQRcodeData(img, propertyNames, COLOR):
    
    myColor= (63,12,144)

    for barcode in decode(img):
        strData = barcode.data.decode('utf-8')
        tmp = strData.split("\n")
        data = {}

        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,myColor,5)
        pts2 = barcode.rect
        
        x = pts2[0]
        y = pts2[1]-5
        if ":" not in strData:
            cv2.putText(img, strData, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.9,COLOR, 2)
        else:
            for item in tmp:
                if ":" not in item:
                    continue
                prop, value = item.split(':')
                data[prop] = value
            print(data)

            for k, v in data.items():
                if k in propertyNames:
                    cv2.putText(img, v, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.9,COLOR, 2)
                    y = y + 50
    return img, data

def resizeImgPercent(img, scale_percent = 100):
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    output = cv2.resize(img, (width, height))
    return output

def resizeImgDim(img, sizeTuple):
    output = cv2.resize(img, size)
    return output


if __name__ == "__main__":

    img = cv2.imread('test3.jpg')
    img = resizeImgPercent(img, scale_percent = 50)

    img, data = getQRcodeData(img,['FN','TEL'], (255,0,0))
    cv2.imshow('Result',img)
    cv2.waitKey(0)
