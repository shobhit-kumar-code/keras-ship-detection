import cv2
import os
# filename='shipcheck.jpg'
# im = cv2.imread(filename)
# im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# im2= cv2.resize(im, (100, 100))
# cv2.imwrite('shiptest.jpg',im2)
# print('changed '+filename)
for filename in os.listdir('resizedall'):
    if filename.endswith('.JPEG'):
        im = cv2.imread('resizedall/'+filename)
        im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        im2= cv2.resize(im, (100, 100))
        cv2.imwrite('resizedall/'+filename,im2)
        print('changed '+filename)