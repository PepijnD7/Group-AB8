#make a matrix with dimension of the room
#0 is a point with no visibility
#1 is a wall
#at the end 2 should be a place where the guards can see
# 4 is the position of the guard
#-1 is the position of a table

#the room is 157mm x 29mm
import numpy as np
from random import *
import matplotlib.pyplot as plt
from wall_finder import vision
width= int(160/5)
height= int(30/5)
tabley_start= int(10/5)
tabley_end= int(20/5)
tablespc=int(47/5)
reso=5
size=(height*reso,width*reso)  #resolution= 10 cm

gallery=np.zeros(size)   
#Placing the walls
gallery[0,:]=1       
gallery[-1,:]=1
gallery[:,0]=1
gallery[:,-1]=1
gallery[round(48/10*reso),0:round(43/10*reso)]=1
gallery[round(48/10*reso),round(-38/10*reso):-1]=1
gallery[round(10/10*reso),round(90/10*reso):round(230/10*reso)]=1

#Placing the tables
gallery[round(tabley_start*reso):round(tabley_end*reso),round(21/5*reso):round(45/5*reso)]=-1       
gallery[round(tabley_start*reso):round(tabley_end*reso),round((21/5+tablespc)*reso):round((45/5+tablespc)*reso)]=-1
gallery[round(tabley_start*reso):round(tabley_end*reso),round((21/5+2*tablespc)*reso):round((45/5+2*tablespc)*reso)]=-1


guard1=[randint(0,size[0]-1),randint(0,size[1]-1)]
guard2=[randint(0,size[0]-1),randint(0,size[1]-1)]
guard3=[randint(0,size[0]-1),randint(0,size[1]-1)]
guard4=[randint(0,size[0]-1),randint(0,size[1]-1)]

guards=[guard1,guard2,guard3,guard4]

index2 = 0
for guard in guards:
    value=gallery[guard[0],guard[1]]
    while value==1 or value==-1:
        guard=(randint(0,size[0]),randint(0,size[1]))
        print("Can't place guard on wall or table")
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
viewedarea= gallery!=0
viewedblocks=sum(sum(viewedarea))
print(viewedblocks)
perc= viewedblocks/(size[0]*size[1])*100
print(perc,"%"," of the room is visible.")

walkingcode='01010101'
n=2
moves=[walkingcode[i:i+n] for i in range(0,len(walkingcode),n)]
print(moves)
i=0
step=1*reso
guards=np.array(guards)
for move in moves:
    if move=='01': #move left
        a=guards[i][1]
       
        a-=step
        guards[i][1]=a
        i+=1
    elif move=='00':#move forward
        a=guards[i][0]
        a+=step
        guards[i][0]=a
        i+=1
    elif move== '10': #move right
        a=guards[i][1]
       
        a+=step
        guards[i][1]=a
        i+=1
    elif move=='11': #move backwards
        a=guards[i][0]
        a-=step
        guards[i][0]=a
        i+=1


print(guards)





