# -*- coding: utf-8 -*-
# Author : Peter Wu

import sys
import numpy as np
import cv2
samples = np.loadtxt('generalsamples.data',np.float32)
responses = np.loadtxt('generalresponses.data',np.float32)
responses = responses.reshape((responses.size,1))
model = cv2.ml.KNearest_create()
model.train(samples,cv2.ml.ROW_SAMPLE,responses)
im = cv2.imread('number5.png')
out = np.zeros(im.shape,np.uint8)
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray,255,1,1,11,2)
_,contours,_ = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
count = 0
num_str = 10 * ['0']
for cnt in contours:
    if cv2.contourArea(cnt)>50:
        [x,y,w,h] = cv2.boundingRect(cnt)
        if h > 36:
            cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
            roi = thresh[y:y+h,x:x+w]
            roismall = cv2.resize(roi,(10,10))
            roismall = roismall.reshape((1,100))
            roismall = np.float32(roismall)
            retval,results,neigh_resp,dists = model.findNearest(roismall,k=1)
            string = str(int((results[0][0])))
            num_str[count] = string
            count += 1
            cv2.putText(out,string,(x,y+h),0,1,(0,255,0))
number = map(int,num_str)
cv2.imshow('im',im)
cv2.imshow('out',out)
temp = []
for i in num_str:
    temp.append(i)
temp.reverse()
temp_str = ''
num_data = temp_str.join(temp)
print(num_data)
file = open('data_txt','a')
file.write(num_data + ';')
file.close()
cv2.waitKey(0)