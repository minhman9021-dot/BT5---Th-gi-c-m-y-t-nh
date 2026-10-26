import cv2
import numpy as np
img_rgb=cv2.imread('images.jpg')  
img_gray=cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
#DOC ANH CAN SO KHOP
template=cv2.imread('images.jpg',0)
#lay chieu rong va chieu cao
w,h =template.shape[::-1]
res=cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold=0.9
loc=np.where(res>=threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb,pt,(pt[0]+w,pt[1]+h),(0,225,0),2)
cv2.namedWindow('Anh phat hien', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Anh phat hien', 1000, 650)
cv2.imshow('Anh phat hien', img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()