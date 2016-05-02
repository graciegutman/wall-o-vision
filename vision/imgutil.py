import numpy as np
import cv2

def open_gui(img, winname='image'):
    cv2.imshow(winname,img)
    k = cv2.waitKey(0) & 0xFF
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite(save_path,img)
        cv2.destroyAllWindows()
