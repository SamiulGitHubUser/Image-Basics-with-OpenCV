#!/usr/bin/env python
# coding: utf-8

# # Direct Drawing with Mouse

# ### SCRIPT 1: Connecting a Function for Drawing

# In[1]:


import cv2
import numpy as np

##############
## Function ##
##############
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(img=img, 
                   center=(x,y), 
                   radius=50, 
                   color=(0,255,0), 
                   thickness=-1)


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




