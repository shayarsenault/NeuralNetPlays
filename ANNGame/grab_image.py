import numpy as np
import cv2
from PIL import ImageGrab


while(True):
    img = ImageGrab.grab(bbox=(100, 10, 600, 500)) #x, y, w, h
    
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    
    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break    

cv2.destroyAllWindows()