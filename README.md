
# Guardian Gate

The guardian gate system is designed to detect nearby vehicles and pedestrians, continuously evaluating their speed, distance, and proximity to the vehicle with the help of a camera.
It provides real-time information to the driver and vehicle systems, enhancing safety during vehicle entry and exit.
The technology serves as a proactive safety measure by alerting the driver to approaching vehicles or pedestrians, reducing the risk of door collisions and ensuring safer exits.
The system processes live video data, identifies vehicles and calculates their speed and proximity to the vehicle.
An auditory feedback mechanism, usually a warning beep, enhances safety during vehicle egress by alerting occupants to potential collision risks.
By combining advanced computer vision, real-time data analysis, and audible warnings, this solution significantly improves safety in scenarios involving vehicle-pedestrian interactions, such as busy urban streets and parking lots.


## Authors

- [Harsh Tripathi](https://github.com/Hrsh404)


## Installation and working

1. Clone the project with git clone command
2. python -m venv pilot-env (create a virtual          environment)
3. pip install -r requirements.txt (install the dependencies)
4. pip install yolov8 (to install the yolov8)
5. pip install opencv (to install cv2)
6. pip install pygame (to install pygame)

7. https://drive.google.com/file/d/1KsWTKuMD6S6H0zvdB8qSC6I_KU8aD_wo/view download this video
8. https://pixabay.com/sound-effects/search/buzzer/ download the "buzzer2" by Pixabay 
9. paste the video and buzzer2 in the same directory
10. Rename buzzer2 as Alarm.mp3
11. paste the video in the same directory 
12. Run main.py file to start the project
13. To open car door Press 1 
14. If any object (bike/car/human) crosses the predicted threshold the buzzer will start beeping.  
    
