# Vehicle-counting-in-traffic-using-YOLO

Vehicle Tracking with YOLO and SORT Tracker + Polygon Drawing for Regions

This project combines vehicle detection and tracking using the YOLO model and the SORT tracker. The additional functionality allows you to interactively draw polygons on video frames to define areas of interest, like road lanes, where vehicle counting takes place.

FEATURES

Detect and track vehicles in video footage using YOLO.

Count vehicles in user-defined areas (left and right road lanes).

Draw polygons interactively on the video using mouse clicks for custom region marking.

Track vehicles moving through predefined road lanes and update the count accordingly.

COORDİNATE DETERMINATION

This feature allows you to mark areas on a video frame by clicking to define points, which are then connected to form a polygon.

How It Works:

Mouse Clicks: Each time you click on the video, the coordinates are saved.

Drawing the Polygon: As you click, lines are drawn between the points to form a polygon.

Visual Feedback: Each point is marked with a small circle so you can see where you clicked

Use the Points in vehicle_counting.py: After marking the polygon and getting the printed output, replace the left_road and right_road arrays in vehicle_counting.py with the new points.

Example:

![image](https://github.com/user-attachments/assets/e4c06a10-7e90-48a5-9fe7-e9bb4bf16b4c)


This way, the user-defined areas (like road lanes) will be used for vehicle counting or tracking in the script.
