import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
from tracker import*
import time
from math import dist

def alarmWarning():
    import pygame


    pygame.mixer.init()
    pygame.mixer.music.load("Alarm.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue


model=YOLO('yolov8s.pt')

Close=0
Open=1
door=int(input("For Close Door:0\nFor Open Door:1\n"))

SPEED=0
if door==1:
    


    def RGB(event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE :  
            colorsBGR = [x, y]
           
            

    cv2.namedWindow('RGB')
    cv2.setMouseCallback('RGB', RGB)

    cap=cv2.VideoCapture('veh2.mp4')


    my_file = open("read.txt", "r")
    data = my_file.read()
    class_list = data.split("\n") 
    

    count=0

    tracker=Tracker()

    cy1=322
    cy2=368

    offset=6

    vh_down={}
    counter=[]


    vh_up={}
    counter1=[]

    while True:    
        ret,frame = cap.read()
        if not ret:
            break
        count += 1
        if count % 3 != 0:
            continue
        frame=cv2.resize(frame,(1020,500))
    

        results=model.predict(frame)
   
        a=results[0].boxes.data
        px=pd.DataFrame(a).astype("float")
    
        list=[]
                
        for index,row in px.iterrows():
    
    
            x1=int(row[0])
            y1=int(row[1])
            x2=int(row[2])
            y2=int(row[3])
            d=int(row[5])
            c=class_list[d]
            if 'car' in c:
                list.append([x1,y1,x2,y2])
        bbox_id=tracker.update(list)
        for bbox in bbox_id:
            x3,y3,x4,y4,id=bbox
            cx=int(x3+x4)//2
            cy=int(y3+y4)//2
            
            cv2.rectangle(frame,(x3,y3),(x4,y4),(0,0,255),2)
            


            if cy1<(cy+offset) and cy1 > (cy-offset):
                vh_down[id]=time.time()
            if id in vh_down:
            
                if cy2<(cy+offset) and cy2 > (cy-offset):
                    elapsed_time=time.time() - vh_down[id]
                    if counter.count(id)==0:
                        counter.append(id)
                        distance = 10 # meters
                        a_speed_ms = distance / elapsed_time
                        a_speed_kh = a_speed_ms * 3.6
                        cv2.circle(frame,(cx,cy),4,(0,0,255),-1)
                        cv2.putText(frame,str(id),(x3,y3),cv2.FONT_HERSHEY_COMPLEX,0.6,(255,255,255),1)
                        cv2.putText(frame,str(int(a_speed_kh))+'Km/h',(x4,y4 ),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,255),2)
                        SPEED=a_speed_kh
            
                            
                    
            #####going UP#####     
            if cy2<(cy+offset) and cy2 > (cy-offset):
                vh_up[id]=time.time()
            if id in vh_up:

                if cy1<(cy+offset) and cy1 > (cy-offset):
                    elapsed1_time=time.time() - vh_up[id]

    


                    if counter1.count(id)==0:
                        counter1.append(id)      
                        distance1 = 10 # meters
                        a_speed_ms1 = distance1 / elapsed1_time
                        a_speed_kh1 = a_speed_ms1 * 3.6
                        cv2.circle(frame,(cx,cy),4,(0,0,255),-1)
                       
                        
        

      


        cv2.line(frame,(550,cy2),(927,cy2),(0,255,0),2)
    
        cv2.putText(frame,('Predefined Threshold'),(785,400),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,255),1)
        d=(len(counter))
        u=(len(counter1))
       
        cv2.putText(frame,('Guardian Gate'),(400,25),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),2)
       
        cv2.imshow("Data Wizards", frame)
       
        if cv2.waitKey(1)&0xFF==27:
            break
        if SPEED >10:
            alarmWarning()
            break   
  
    cap.release()
    cv2.destroyAllWindows()


else: 
    print("Door is closed")