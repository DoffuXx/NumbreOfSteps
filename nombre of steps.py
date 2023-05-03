import cv2
import mediapipe as mp
from math import sqrt
import numpy
import time
import math as m
import pandas as pd
mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
mp_drawing_styles = mp.solutions.drawing_styles

pose = mpPose.Pose()

cap = cv2.VideoCapture("park.mp4")
up = False
counter = 0
vitesse=0
dist=0
disttotal=0
fps = cap.get(cv2.CAP_PROP_FPS)
speed = 0
positionX = []
positionY = []
speeds = []

i=0

while True:
    success,img = cap.read()
    img = cv2.resize(img, (640,480))
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # print(results.pose_landmarks)
    # print("-----------------------------------------------------")
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        points = {}
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h,w,c = img.shape
            cx, cy = int(lm.x*w), int(lm.y*h)
            # print(id,lm,cx,cy)
            points[id] = (cx,cy)
                     
        x = points[28][0]
        y = points[28][1] 
        for i in range(total_frames):  
            positionX.append(x)
            positionY.append(y)

        cv2.circle(img, points[28], 15, (255,0,0), cv2.FILLED)
        cv2.circle(img, points[27], 15, (255,0,0), cv2.FILLED)
        cv2.circle(img, points[30], 15, (255,0,0), cv2.FILLED)
        cv2.circle(img, points[29], 15, (255,0,0), cv2.FILLED)
       
       
        if points[30][0] < points[31][0]:
             x1,y1=points[28]
             x2,y2=points[27]
             distance=(m.sqrt((x2-x1)**2+(y2-y1)**2))
             dist=(distance*0.2646)/100
             disttotal += dist
             print("distance parcourus au total",disttotal)
             vitesse=((dist)/(1.2))
             
       
        #myoundvitesse=(round(vitesse,2))
        #print(myroundvitesse) 
           # distance = sqrt(pow(positionX[i]-positionX[i-1],2)+pow(positionY[i]-positionY[i-1],2))
            #speed = distance / fps
            #speeds.append(speed)
            
 
        if not up and points[28][1] < points[27][1]:
            print("UP Right leg")
            up = True
            counter += 1
        if up and points[27][1] < points[28][1]:
            print("UP left leg")
            up = False
            counter += 1
                     
        # if points[30][1] == points[29][1]:
        #     print("Down")
        #     up = False 
        # print("----------------------",counter)
        
        
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    cv2.putText(img, 
                'Nombres de pas :',
                (50, 50),font, 1, 
                (0, 255, 255), 
                2, 
                cv2.LINE_4)
    cv2.putText(img,str(counter),(340,50),font,1,(0,255,255),2)
    cv2.putText(img, 
                'vitesse:',
                (50, 100),font, 1, 
                (0, 255, 255), 
                2, 
                cv2.LINE_4)
    cv2.putText(img,str(vitesse) +"m/s",(180,100),font,1,(0,255,255),2)
    cv2.putText(img, 
                'distance de pas:',
                (50, 150),font, 1, 
                (0, 255, 255), 
                2, 
                cv2.LINE_4)
    
    cv2.putText(img,str(dist) +"m",(340,150),font,1,(0,255,255),2)
  #   cv2.putText(img, str(up), (100,500),cv2.FONT_HERSHEY_PLAIN, 12, (255,150,0),12)
   #  cv2.putText(img, str(speed), (1000,500),cv2.FONT_HERSHEY_PLAIN, 12, (255,150,0),12)

    cv2.imshow("img",img)
    cv2.waitKey(1)
    




   

c




   




# print(sum(speeds) / len(speeds))




