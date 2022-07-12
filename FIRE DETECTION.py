import cv2
import numpy as np
import matplotlib.pyplot as plt
live_camera = cv2.VideoCapture(0)
while (live_camera.isOpened()):
    ret, frame = live_camera.read()
    cv2.imshow("Fire Detection", frame)
    if cv2.waitKey(10) == 27:
        break
    img_RGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    img_cap = plt.imshow(img_RGB)
    plt.show()
live_camera.release()
cv2.destroyAllWindows 
