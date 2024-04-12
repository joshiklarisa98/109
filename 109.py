import numpy as np
import pyautogui
import imutils
import cv2

image = pyautogui. screenshot ()
image = cv2.cvtColor(np.array(image), cv2. COLOR_RGB2BGR)
cv2.imwrite("in_memory_to_disk.png", image)

Save the screenshot directly to the disk.

pyautogui.screenshot ("straight_to_disk.png")

Finally load the image in the OpenCV format.
image = cv2.imread("straight_to_disk.png")
cv2.imshow("Screenshot", imutils.resize(image, width=600))