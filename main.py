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

arr = [[0,0,0],[0,0,0],[0,0,0]]

symbol_x = cv2.imread('symbol_x.jpg')
symbol_o = cv2.imread('symbol_o.jpg')
p1_box = cv2.imread('p1_box.jpg')
p2_box = cv2.imread('p2_box.jpg')
p1_win = cv2.imread('p1_win.jpg')
p2_win = cv2.imread('p2_win.jpg')
draw = cv2.imread('draw.jpg')

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

def checkWinner():

    global winner

    for row in arr:

        if(row[0]!=0 and row.count(row[0])==3):
            winner = row[0]
            
            if(row[0]==arr[0][0]):
                cv2.line(img,(111,151),(401,151),(255,0,0),3)
            elif(row[0]==arr[1][0]):
                cv2.line(img,(111,256),(401,256),(255,0,0),3)
            else:
                cv2.line(img,(111,361),(401,361),(255,0,0),3)
            break
    
    if(arr[0][0]!=0 and arr[0][0]==arr[1][0] and arr[0][0]==arr[2][0]):
        winner = arr[0][0]
        cv2.line(img,(151,111),(151,401),(255,0,0),3)
    
    if(arr[0][1]!=0 and arr[0][1]==arr[1][1] and arr[0][1]==arr[2][1]):
        winner = arr[0][1]
        cv2.line(img,(256,111),(256,401),(255,0,0),3)

    if(arr[0][2]!=0 and arr[0][2]==arr[1][2] and arr[0][2]==arr[2][2]):
        winner = arr[0][2]
        cv2.line(img,(361,111),(361,401),(255,0,0),3)

    if(arr[0][0]!=0 and arr[0][0]==arr[1][1] and arr[0][0]==arr[2][2]):
        winner = arr[0][0]
        cv2.line(img,(111,111),(401,401),(255,0,0),3)

    if(arr[2][0]!=0 and arr[2][0]==arr[1][1] and arr[2][0]==arr[0][2]):
        winner = arr[1][1]
        cv2.line(img,(111,401),(401,111),(255,0,0),3)

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

        checkWinner()
    
    
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

cv2.destroyWindow('start_page')

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('playground')
cv2.setMouseCallback('playground',playgroundCallback)

cv2.rectangle(img,(96,96),(416,416),(255,255,255),5)
cv2.rectangle(img,(201,96),(311,416),(255,255,255),5)
cv2.rectangle(img,(96,201),(416,311),(255,255,255),5)

while(winner==0 and cnt<9):

    if(cnt%2==0):
        curr_player = player1
        img[455:511,0:280] = p1_box
    else:
        curr_player = player2
        img[455:511,0:280] = p2_box

    cv2.imshow('playground',img)

    if(cv2.waitKey(10) & 0xFF == 27):
        break

cv2.putText(img,'Game Over !!',(136,60),font,1,(255,0,0),1,cv2.LINE_AA)

if(cnt==9):
    img[455:511,0:280] = draw
elif(curr_player==player1):
    img[455:511,0:280] = p1_win
else:
    img[455:511,0:280] = p2_win

cv2.imshow('playground',img)

cv2.waitKey(0)
cv2.destroyAllWindows()