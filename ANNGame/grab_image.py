import numpy as np
import cv2
from PIL import ImageGrab
while True:
    img = ImageGrab.grab(bbox=(100, 10, 600, 500)) #x, y, w, h
   
    #frame = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    #cframe = cv2.Canny(frame, 100, 200)
    cv2.imshow("frame", np.array(img))
    key = cv2.waitKey(1)
    if key == 27:
        break    

cv2.destroyAllWindows()