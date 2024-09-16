import cv2
import numpy as np

polygon_points = []

video_path = r'video1.mp4'
cap = cv2.VideoCapture(video_path)

def mouse_callback(event, x, y, flags, param):
    global polygon_points
    if event == cv2.EVENT_LBUTTONDOWN:
        polygon_points.append((x, y))
        print(f"Point Added: (X: {x}, Y: {y})")

cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame', mouse_callback)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("The video ended or an error occurred.")
        break
    
    frame = cv2.resize(frame, (1920, 1080))

    # Draw polygon points
    if len(polygon_points) > 1:
        cv2.polylines(frame, [np.array(polygon_points)], isClosed=False, color=(0, 255, 0), thickness=2)
    
    
    for point in polygon_points:
        cv2.circle(frame, point, radius=5, color=(0, 0, 255), thickness=-1)

    cv2.imshow('Frame', frame)

    # Exit when ESC key is pressed
    key = cv2.waitKey(50) & 0xFF
    if key == 27:
        break

cv2.destroyAllWindows()
cap.release()