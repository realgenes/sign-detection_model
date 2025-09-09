import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
from cvzone.ClassificationModule import Classifier
import math
import time
import h5py
from keras.models import load_model




#  camera opening 
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
classifier = Classifier("model/keras_model.h5","model/labels.txt")

offset = 20
imgSize=300



labels = ["A","B","C","D","E","F","G","H","I","J","K","L"]


while True:
  success, img = cap.read()
  imgOutput = img.copy()
  hands,img= detector.findHands(img)

  #cropping hands 
  if hands:
    hand = hands[0]
    x,y,w,h = hand['bbox']

    imgWhite = np.ones((imgSize,imgSize,3),np.uint8)*255


    imgCrop = img[y-offset:y+h+offset,x-offset:x+w+offset] #matrix dimensions
    if imgCrop.size==0:
      continue

    imgCropShape = imgCrop.shape


    aspectRatio = h/w

    if aspectRatio>1:
      k = imgSize/h
      wCal = math.ceil(k*w)
      imgResize = cv2.resize(imgCrop,(wCal,imgSize))
      imgResizeShape = imgResize.shape

      #width gap reducing to make it to centre
      wGap =math.ceil( (imgSize-wCal)/2)
      imgWhite[:,wGap:wCal+wGap] = imgResize
      prediction,index = classifier.getPrediction(imgWhite)
      print(prediction,index)
      

    else:
      k = imgSize/w
      hCal = math.ceil(k*h)
      imgResize = cv2.resize(imgCrop,(imgSize,hCal))
      imgResizeShape = imgResize.shape

      #width gap reducing to make it to centre
      hGap =math.ceil( (imgSize-hCal)/2)
      imgWhite[hGap:hCal+hGap,:] = imgResize
      prediction,index = classifier.getPrediction(imgWhite)




    cv2.imshow("ImageCRop",imgCrop)
    cv2.imshow("Image White",imgWhite)

    cv2.putText(imgOutput,labels[index],(x,y-20),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,255),2)


  cv2.imshow("Image",imgOutput)
        

  key = cv2.waitKey(1)

  