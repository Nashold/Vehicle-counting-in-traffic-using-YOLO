import cv2
import cvzone
import math
import numpy as np
from ultralytics import YOLO
from sort import *

video_path = 'video1.mp4'
cap = cv2.VideoCapture(video_path)
model = YOLO('yolov9c.pt')

classnames = []
with open('classes.txt', 'r') as f:
    classnames = f.read().splitlines()

left_road = np.array([[286, 711], [1097, 692],], np.int32)
right_road = np.array([[1077, 446], [1422, 362],], np.int32)


leftroad_area = np.array([left_road[0],left_road[1]]).reshape(-1)
rightroad_area = np.array([right_road[0],right_road[1]]).reshape(-1) 

tracker = Sort()
leftCounter = []
rightCounter = []

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1920,1080))
    results = model(frame)
    current_detections = np.empty([0,5])

    for info in results:
        parameters = info.boxes
        for box in parameters:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1 
            confidence = box.conf[0]
            class_detect = box.cls[0]
            class_detect = int(class_detect)
            class_detect = classnames[class_detect]
            conf = math.ceil(confidence * 100)
            cvzone.putTextRect(frame, f'{class_detect}', [x1 + 8, y1 - 12], thickness=2, scale=1)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            if class_detect == 'car' or class_detect == 'truck' or class_detect == 'bus'\
                    and conf > 30:
                detections = np.array([x1,y1,x2,y2,conf])
                current_detections = np.vstack([current_detections,detections]) 


    cv2.polylines(frame,[left_road], isClosed=False, color=(0, 0, 255), thickness=8)
    cv2.polylines(frame, [right_road], isClosed=False, color=(255,0, 0), thickness=8)

    track_result = tracker.update(current_detections) 
    for result in track_result:
        x1,y1,x2,y2,id = result
        x1,y1,x2,y2,id = int(x1),int(y1),int(x2),int(y2),int(id)
        w, h = x2 - x1, y2 - y1
        cx, cy = x1 + w // 2, y1 + h // 2 -40 

      
        if leftroad_area[0] < cx < leftroad_area[2] and leftroad_area[1] - 20 < cy < leftroad_area[1] + 20:
            if leftCounter.count(id) == 0:
                leftCounter.append(id)


        if rightroad_area[0] < cx < rightroad_area[2] and rightroad_area[1] - 20 < cy < rightroad_area[1] + 20:
            if rightCounter.count(id) == 0:
                rightCounter.append(id)

        cv2.circle(frame,(70,90),15,(0,0,255),-1)
        cv2.circle(frame,(970,90),15,(255,0,0),-1)
        cvzone.putTextRect(frame, f'Left lane vehicles ={len(leftCounter)}', [100, 99], thickness=4, scale=2.3, border=2)
        cvzone.putTextRect(frame, f'Right lane vehicles ={len(rightCounter)}', [1000, 99], thickness=4, scale=2.3, border=2)

    cv2.imshow('Track Results', frame)
    cv2.waitKey(1)

    # End process when pressing q

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()