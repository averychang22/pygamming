import cv2
import numpy as np
# Capture the webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# To capture the background - take a few iterations to stabilize view
while True:
    # Get the next frame
    _, bg_frame = cap.read()
    bg_frame = cv2.flip(bg_frame, 1)
    # Update the frame in the window
    cv2.imshow("Webcam", bg_frame)
    # Check if q is pressed, terminate if so
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Processing of frames are done in gray
bg_gray = cv2.cvtColor(bg_frame, cv2.COLOR_BGR2GRAY)
# We blur it to minimize reaction to small details
bg_gray = cv2.GaussianBlur(bg_gray, (5, 5), 0)

# This is where the game loop starts
while True:
    # Get the next frame
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    # Processing of frames are done in gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # We blur it to minimize reaction to small details
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    # Get the difference from last_frame
    delta_frame = cv2.absdiff(bg_gray, gray)
    # Have some threshold on what is enough movement
    thresh = cv2.threshold(delta_frame, 100, 255, cv2.THRESH_BINARY)[1]
    # This dilates with two iterations
    thresh = cv2.dilate(thresh, None, iterations=2)
    cv2.imshow("track", thresh)
   # Update the frame in the window
    cv2.imshow("Webcam", frame)
    # Check if q is pressed, terminate if so
    if cv2.waitKey(1) == ord('q'):
        break
# Release the webcam and destroy windows
cap.release()
cv2.destroyAllWindows()