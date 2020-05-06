import numpy as np
import cv2
import matplotlib.pyplot as plt

img =cv2.imread('G19_edited.jpg')

cv2.namedWindow('G19', cv2.WINDOW_NORMAL)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower_bound=np.array([5,190, 190])
upper_bound=np.array([25,255,255])
mask=cv2.inRange(hsv,lower_bound,upper_bound)
res=cv2.bitwise_and(img,img,mask= mask)
coord=np.nonzero(mask)
coord=np.array([coord[0],coord[1]])

rotate=
x=np.array([0])
y=np.array([0])


j=0
prevj=0
for i in range(len(coord[0])-1):
    if coord[0,i]==coord[0,i+1]:
        j=j+1
    else:
        n=int(prevj+np.round(j/2))
        x=np.append(x,coord[0,n])
        y=np.append(y,coord[1,n])
        prevj = i
        j = 0

clean=np.append(x,y)

cv2.imshow('G19',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.plot(coord[0],coord[1],'yx')
#plt.plot(x,y,'ro')
plt.show()

f = open("raw.txt","w") # Open file for writing
for i in range(len(coord[0])):
    line = str(coord[0,i])+','+str(coord[1,i])+'\n'
    f.write(line)
f.close()

f = open("clean.txt","w") # Open file for writing
for i in range(len(x)):
    line = str(x[i])+','+str(y[i])+'\n'
    f.write(line)
f.close()