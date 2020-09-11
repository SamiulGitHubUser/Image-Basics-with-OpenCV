## Dragging with Mouse¶
import cv2
import numpy as np

##############
## Function ##
##############
drawing = False
ix, iy = -1, -1

def draw_circle(event, x, y, flags, param):
    global ix,iy,drawing
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        
    elif event == cv2.EVENT_RBUTTONDOWN:
        # Now the mouse is moving
        if drawing == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            
    elif event == cv2.EVENT_LBUTTONUP:
        # Once you lift the mouse button, drawing is False
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        


## Call function draw_circle()
cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing', draw_circle)


###############################
## SHOWING IMAGE WITH OPENCV ##
###############################
img = np.zeros((512, 512, 3))
while True:
    cv2.imshow('my_drawing', img)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break       
cv2.destroyAllWindows()


# In[ ]:




