import cv2
import numpy as np

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)

# Define color ranges in HSV and their corresponding BGR colors for drawing
colors = {
    'red': [(0, 120, 70), (10, 255, 255), (0, 0, 255)],       # Red
    'green': [(36, 100, 100), (86, 255, 255), (0, 255, 0)],   # Green
    'blue': [(94, 80, 2), (126, 255, 255), (255, 0, 0)],      # Blue
    'yellow': [(22, 93, 100), (45, 255, 255), (0, 255, 255)], # Yellow
    'orange': [(10, 100, 20), (25, 255, 255), (0, 165, 255)], # Orange
    'purple': [(129, 50, 70), (158, 255, 255), (255, 0, 255)],# Purple
    'pink': [(160, 100, 100), (179, 255, 255), (255, 20, 147)],# Pink
    'black': [(0, 0, 0), (180, 255, 30), (0, 0, 0)]           # Black
}

while True:
    # Capture the video frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Iterate over the colors dictionary to detect multiple colors
    for color_name, (lower_hsv, upper_hsv, bgr_color) in colors.items():
        lower_bound = np.array(lower_hsv)
        upper_bound = np.array(upper_hsv)

        # Create a mask for the color
        mask = cv2.inRange(hsv, lower_bound, upper_bound)

        # Find contours for the masked areas
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Draw the contours
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 500:  # Filter small contours by area
                # Get the bounding box for each contour
                x, y, w, h = cv2.boundingRect(contour)

                # Draw the rectangle with the color corresponding to the detected color
                cv2.rectangle(frame, (x, y), (x + w, y + h), bgr_color, 2)

                # Put the text (color name) with matching color
                cv2.putText(frame, color_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, bgr_color, 2)

    # Display the original frame with contours
    cv2.imshow('Frame', frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()