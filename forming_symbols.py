import cv2
import numpy as np
from matplotlib import pyplot as plt

symbol_x = np.zeros((100,100,3),np.uint8)

cv2.rectangle(symbol_x,(10,10),(90,90),(0,0,50),-1)

cv2.line(symbol_x,(20,20),(80,80),(0,0,255),2)
cv2.line(symbol_x,(80,20),(20,80),(0,0,255),2)

cv2.imshow('image',symbol_x)
cv2.waitKey(0)

symbol_o = np.zeros((100,100,3),np.uint8)

cv2.rectangle(symbol_o,(10,10),(90,90),(0,30,0),-1)

cv2.circle(symbol_o,(50,50),35,(0,255,0),2)

cv2.imshow('image1',symbol_o)
cv2.waitKey(0)

cv2.imwrite('symbol_x.jpg',symbol_x)
cv2.imwrite('symbol_o.jpg',symbol_o)

p1_box = np.zeros((56,280,3),np.uint8)
cv2.putText(p1_box,'player 1\'s turn',(10,46),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
cv2.imwrite('p1_box.jpg',p1_box)

p2_box = np.zeros((56,280,3),np.uint8)
cv2.putText(p1_box,'player 2\'s turn',(10,46),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
cv2.imwrite('p2_box.jpg',p2_box)

cv2.destroyAllWindows()