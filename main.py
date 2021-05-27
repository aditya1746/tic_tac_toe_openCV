import cv2
import numpy as np
from matplotlib import pyplot as plt
font = cv2.FONT_HERSHEY_COMPLEX

player1 = 0
player2 = 0
symbolSelected = 0
winner = 0
curr_player = 0
cnt = 0

rows, cols = (5, 5)
arr = [[0]*cols]*rows

symbol_x = cv2.imread('symbol_x.jpg')
symbol_o = cv2.imread('symbol_o.jpg')
p1_box = cv2.imread('p1_box.jpg')
p2_box = cv2.imread('p2_box.jpg')

def whichArea(x,y):

    global curr_player,cnt

    if((arr[0][0] == 0) and (x>=101 and x<=201) and (y>=101 and y<=201)):
        
        if(curr_player==1):
            img[101:201,101:201] = symbol_x
        else:
            img[101:201,101:201] = symbol_o

        cnt = cnt+1
        arr[0][0] = curr_player

    if((arr[0][1] == 0) and (x>=206 and x<=306) and (y>=101 and y<=201)):
        
        if(curr_player==1):
            img[101:201,206:306] = symbol_x
        else:
            img[101:201,206:306] = symbol_o
        
        cnt = cnt+1
        arr[0][1] = curr_player

    if((arr[0][2] == 0) and (x>=311 and x<=411) and (y>=101 and y<=201)):
        
        if(curr_player==1):
            img[101:201,311:411] = symbol_x
        else:
            img[101:201,311:411] = symbol_o

        cnt = cnt+1
        arr[0][2] = curr_player

    if((arr[1][0] == 0) and (x>=101 and x<=201) and (y>=206 and y<=306)):
        
        if(curr_player==1):
            img[206:306,101:201] = symbol_x
        else:
            img[206:306,101:201] = symbol_o

        cnt = cnt+1
        arr[1][0] = curr_player

    if((arr[1][1] == 0) and (x>=206 and x<=306) and (y>=206 and y<=306)):
        
        if(curr_player==1):
            img[206:306,206:306] = symbol_x
        else:
            img[206:306,206:306] = symbol_o

        cnt = cnt+1
        arr[1][1] = curr_player

    if((arr[1][2] == 0) and (x>=311 and x<=411) and (y>=206 and y<=306)):
        
        if(curr_player==1):
            img[206:306,311:411] = symbol_x
        else:
            img[206:306,311:411] = symbol_o

        cnt = cnt+1
        arr[1][2] = curr_player

    if((arr[2][0] == 0) and (x>=101 and x<=201) and (y>=311 and y<=411)):
        
        if(curr_player==1):
            img[311:411,101:201] = symbol_x
        else:
            img[311:411,101:201] = symbol_o

        cnt = cnt+1
        arr[2][0] = curr_player

    if((arr[2][1] == 0) and (x>=206 and x<=306) and (y>=311 and y<=411)):
        
        if(curr_player==1):
            img[311:411,206:306] = symbol_x
        else:
            img[311:411,206:306] = symbol_o

        cnt = cnt+1
        arr[2][1] = curr_player

    if((arr[2][2] == 0) and (x>=311 and x<=411) and (y>=311 and y<=411)):
        
        if(curr_player==1):
            img[311:411,311:411] = symbol_x
        else:
            img[311:411,311:411] = symbol_o

        cnt = cnt+1
        arr[2][2] = curr_player

def startCallback(event,x,y,flags,param):

    global player1,player2,symbolSelected

    if(event==cv2.EVENT_LBUTTONDBLCLK):

        if((x>=130 and x<=230) and (y>=280 and y<=380)):

            player1 = 1
            player2 = 2
            symbolSelected = 1

        elif((x>=282 and x<=382) and (y>=280 and y<=380)):

            player1 = 2
            player2 = 1
            symbolSelected = 1


def playgroundCallback(event,x,y,flags,param):

    global winner,cnt

    if(event==cv2.EVENT_LBUTTONDBLCLK):

        whichArea(x,y)
    
    


startPage = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('start_page')
cv2.setMouseCallback('start_page',startCallback)

cv2.putText(startPage,'let\'s play',(180,100),font,1,(0,255,0),2,cv2.LINE_AA)

cv2.putText(startPage,'player 1 choose your symbol',(130,250),font,0.5,(255,255,255),1,cv2.LINE_AA)

startPage[280:380,130:230] = symbol_x
startPage[280:380,282:382] = symbol_o

while(symbolSelected==0):
    cv2.imshow('start_page',startPage)
    cv2.waitKey(1)

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('playground')
cv2.setMouseCallback('playground',playgroundCallback)

cv2.rectangle(img,(96,96),(416,416),(255,255,255),5)
cv2.rectangle(img,(201,96),(311,416),(255,255,255),5)
cv2.rectangle(img,(96,201),(416,311),(255,255,255),5)

while(winner==0):

    if(cnt%2==0):
        curr_player = player1
        img[455:511,0:280] = p1_box
    else:
        curr_player = player2
        img[455:511,0:280] = p2_box

    cv2.imshow('playground',img)

    if(cv2.waitKey(10) & 0xFF == 27):
        break
    
#cv2.waitKey(0)
cv2.destroyAllWindows()