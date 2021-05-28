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
cv2.imshow('image1',p1_box)
cv2.waitKey(0)

p2_box = np.zeros((56,280,3),np.uint8)
cv2.putText(p2_box,'player 2\'s turn',(10,46),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
cv2.imwrite('p2_box.jpg',p2_box)
cv2.imshow('image1',p2_box)
cv2.waitKey(0)

p1_win = np.zeros((56,280,3),np.uint8)
cv2.putText(p1_win,'player 1 won',(10,46),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1,cv2.LINE_AA)
cv2.imwrite('p1_win.jpg',p1_win)
cv2.imshow('image1',p1_win)
cv2.waitKey(0)

p2_win = np.zeros((56,280,3),np.uint8)
cv2.putText(p2_win,'player 2 won',(10,46),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1,cv2.LINE_AA)
cv2.imwrite('p2_win.jpg',p2_win)
cv2.imshow('image1',p2_win)
cv2.waitKey(0)

draw = np.zeros((56,280,3),np.uint8)
cv2.putText(draw,'it\'s a draw',(10,46),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1,cv2.LINE_AA)
cv2.imwrite('draw.jpg',draw)
cv2.imshow('image1',draw)
cv2.waitKey(0)

cv2.destroyAllWindows()