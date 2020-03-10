#make a matrix with dimension of the room
#0 is a point with no visibility
#1 is a wall
#at the end 2 should be a place where the guards can see
# 3 is the position of the guard

#the room is 157mm x 29mm
import numpy as np
from random import *
import matplotlib.pyplot as plt
from wall_finder import vision
width= int(160/5)
height= int(30/5)
reso=5
size=(height*reso,width*reso)  #resolution= 10 cm

gallery=np.zeros(size)
gallery[0,:]=1          #walls
gallery[-1,:]=1
gallery[:,0]=1
gallery[:,-1]=1
gallery[round(48/10*reso),0:round(43/10*reso)]=1
gallery[round(48/10*reso),round(-38/10*reso):-1]=1
gallery[round(10/10*reso),round(90/10*reso):round(230/10*reso)]=1

print(gallery)

guard1=(randint(0,size[0]-1),randint(0,size[1]-1))
guard2=(randint(0,size[0]-1),randint(0,size[1]-1))
guard3=(randint(0,size[0]-1),randint(0,size[1]-1))
guard4=(randint(0,size[0]-1),randint(0,size[1]-1))

guards=[guard1,guard2,guard3,guard4]

index2 = 0
for guard in guards:
    value=gallery[guard[0],guard[1]]
    while value==1:
        guard=(randint(0,size[0]),randint(0,size[1]))
        print("Can't place guard on wall")
        value=gallery[guard[0],guard[1]]
    gallery[guard[0],guard[1]]=4
    guards[index2] = guard
    index2+=1
    

#print(guards)
#plt.imshow(gallery)
#plt.show()

for guard in guards:
    gallery=vision(guard,gallery,1/reso)
    print()
    print(guard)
    plt.imshow(gallery)
    plt.show()




