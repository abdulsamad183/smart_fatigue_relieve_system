# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 11:58:49 2022

@author: Samad
"""

import cv2
import numpy as np
#import matplotlib.pyplot as plt
import time

from pygame import mixer
import os 
import random

#Arduino Libraries
import serial


net = cv2.dnn.readNetFromDarknet("yolov3_custom.cfg","yolov3_custom_4000.weights")

classes = ['tired','not_tired']
ans=[]

arduino=serial.Serial(port='COM10')


def playsong():
    songs_list=os.listdir('Songs')
    song=random.choice(songs_list)
    mixer.init()
    mixer.music.load("Songs/"+song)
    print('Playing Song for Relaxing.Please Enjoy ')
    mixer.music.play()
    time.sleep(30)  #Set number of seconds to play song
    mixer.music.stop()
    print('Playing Stopped')

def watertip():
    mixer.init()
    mixer.music.load('water.mp3')
    mixer.music.play()

def relaxing():
    mixer.init()
    mixer.music.load('relax.mp3')
    mixer.music.play()

def breathtip():
    mixer.init()
    mixer.music.load('breathtip.mp3')
    mixer.music.play()
    
    
############################################################
"""                      Detection                       """
############################################################
capture_duration = 20

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
start_time = time.time()
while ( int(time.time() - start_time) < capture_duration ):
    _, img = cap.read()
    img = cv2.resize(img,(1280,720))
    hight,width,_ = img.shape
    blob = cv2.dnn.blobFromImage(img, 1/255,(416,416),(0,0,0),swapRB = True,crop= False)
    net.setInput(blob)
    output_layers_name = net.getUnconnectedOutLayersNames()
    layerOutputs = net.forward(output_layers_name)
    boxes =[]
    confidences = []
    class_ids = []

    for output in layerOutputs:
        for detection in output:
            score = detection[5:]
            class_id = np.argmax(score)
            confidence = score[class_id]
            if confidence > 0.7:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * hight)
                w = int(detection[2] * width)
                h = int(detection[3]* hight)
                x = int(center_x - w/2)
                y = int(center_y - h/2)
                boxes.append([x,y,w,h])
                confidences.append((float(confidence)))
                class_ids.append(class_id)


    indexes = cv2.dnn.NMSBoxes(boxes,confidences,.5,.4)
    boxes =[]
    confidences = []
    class_ids = []
    for output in layerOutputs:
        for detection in output:
            score = detection[5:]
            class_id = np.argmax(score)
            confidence = score[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * hight)
                w = int(detection[2] * width)
                h = int(detection[3]* hight)
                x = int(center_x - w/2)
                y = int(center_y - h/2)
                boxes.append([x,y,w,h])
                confidences.append((float(confidence)))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes,confidences,.8,.4)
    font = cv2.FONT_HERSHEY_PLAIN
    colors = np.random.uniform(0,255,size =(len(boxes),3))
    if  len(indexes)>0:
        for i in indexes.flatten():
            x,y,w,h = boxes[i]
            label = str(classes[class_ids[i]])
            #print(label)
            ans.append(classes.index(label))
            confidence = str(round(confidences[i],2))
            color = colors[i]
            cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
            cv2.putText(img,label + " " + confidence, (x,y+400),font,2,color,2)
    cv2.imshow('img',img)
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
###############################################################################

 

#
total_count=len(ans)
not_tired_values=sum(ans)
tired_values=total_count-not_tired_values



if tired_values>=not_tired_values:
    print('AC ON')
    arduino.write(bytes('H','utf-8'))
    
    #Water tip
    time.sleep(2)
    watertip()
    time.sleep(3)
    watertip()
    time.sleep(2)
    
    #Song
    relaxing()
    time.sleep(4)
    playsong()
    time.sleep(2)
    
    #Breath Tips
    breathtip()
    time.sleep(3)
    breathtip()
    time.sleep(3)
    
    print('Done')
    
else:
    #arduino=serial.Serial(port='COM12')
    arduino.write(bytes('L','utf-8'))
    print('You are not Tired')