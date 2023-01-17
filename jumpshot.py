import cv2
import numpy as np
import tkinter as tk

# prompt the user to enter the file path of the video
video_file = input("Enter the file path of the video: ")

# load video of player's jump shot
video = cv2.VideoCapture(video_file)

# initialize suggestions list
suggestions = []

# loop through each frame of the video
while True:
    # read frame from video
    ret, frame = video.read()

    # if we have reached the end of the video, break out of loop
    if not ret:
        break

    # convert frame to grayscale and apply Gaussian blur
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # detect edges in the frame using Canny edge detection
    edges = cv2.Canny(blur, 100, 200)

    # find contours in the frame
    contours,  = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # loop through each contour
    for contour in contours:
        # approximate the contour as a polygon
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

        # if the approximated contour has 4 points, it is likely a basketball hoop
        if len(approx) == 4:
            # compute the center of the contour
            M = cv2.moments(contour)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

            # draw a circle at the center of the contour
            cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

            # find the position of the player's hand in the frame
            hand_y = 0
            for y in range(frame.shape[0]):
                if frame[y, cx] > 100:
                    hand_y = y
                    break
            # compute the distance from the player's hand to the center of the hoop
            hand_distance = abs(hand_y - cy)

            # if the distance is too large, add a suggestion to the list
            if hand_distance > 50:
                suggestions.append("Consider adjusting your release point to get a cleaner shot")

    # display the frame
    cv2.imshow("Frame", frame)
    cv2.waitKey(1)

# release the video capture object and close all windows
video.release()
cv2.destroyAllWindows()

# print out the suggestions
print("Suggestions for improving your jump shot:")
for suggestion in suggestions:
    print(suggestion)

# Create the main window
root = tk.Tk()
root.title("Jump Shot Analysis")

# Create a label for the suggestions
label = tk.Label(root, text="Suggestions for improving your jump shot:")
label.pack()

# Create a scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a text widget to display the suggestions
text = tk.Text(root, yscrollcommand=scrollbar.set)
text.pack()

# Attach the scrollbar to the text widget
scrollbar.config(command=text.yview)

# Insert the suggestions into the text widget
for suggestion in suggestions:
    text.insert(tk.END, suggestion + "\n")

# Run the main loop
root.mainloop()
