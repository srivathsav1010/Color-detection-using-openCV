# Color-detection-using-openCV

This project leverages OpenCV to capture video from the webcam and detects various colors in real-time. It uses the HSV (Hue, Saturation, Value) color space to identify specific color ranges and then draws bounding boxes around detected color regions in the video feed. The program also labels each detected color with its respective name, providing a clear visual cue for real-time color detection.

Features
Color Detection: The program is capable of detecting multiple colors including red, green, blue, yellow, orange, purple, pink, and black.
Real-Time Visualization: Once a color is detected, a bounding box is drawn around the object, and the color name is displayed near it.
Contour Detection: Using OpenCV's contour detection algorithm, the program identifies areas of interest where colors are detected.
Filter Small Contours: The program filters out small contours to focus on significant objects (those with an area larger than 500 pixels).
Real-Time Video Feed: The program captures live video from the webcam, processes it frame by frame, and displays the result on the screen.
Dependencies
This project requires the following Python libraries:

opencv-python for computer vision functions
numpy for array handling


RUN THE CODE using COMMAND PROMPT
	
  --Install the Required Libraries:
	--------------------------------
	pip install opencv-python numpy
	--------------------------------

  --Create a Python Script:

	Create a .py file

  --Run the Script:

	python <FILE_NAME>.py

  --Permissions:

	Ensure that your webcam is available for access by the Python script
  
  --Exit the Program:
	
	To stop the program, press the "q" key when the video window is open.
