#make a matrix with dimension of the room
#0 is a point with no visibility
#1 is a wall
#at the end 2 should be a place where the guards can see
# 4 is the position of the guard
#-1 is the position of a table

#the room is 157mm x 29mm
#------------------------------------------------------------------------------
#                           SETUP
#------------------------------------------------------------------------------

import numpy as np
from random import *
import matplotlib.pyplot as plt
from wall_finder import vision
from itertools import permutations
width= int(160/5)
height= int(30/5)
tabley_start= int(10/5)
tabley_end= int(20/5)
tablespc=int(47/5)
reso=5
totalsteps=2
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

#------------------------------------------------------------------------------
#                           First Guard Placement
#------------------------------------------------------------------------------

guard1=[randint(0,size[0]-1),randint(0,size[1]-1)]
guard2=[randint(0,size[0]-1),randint(0,size[1]-1)]
guard3=[randint(0,size[0]-1),randint(0,size[1]-1)]
guard4=[randint(0,size[0]-1),randint(0,size[1]-1)]

guards=[guard1,guard2,guard3,guard4]

index2 = 0
for guard in guards:
    value=gallery[guard[0],guard[1]]
    while value==1 or value==-1:
        guard=[randint(0,size[0]),randint(0,size[1])]
        print("Can't place guard on wall or table")
        value=gallery[guard[0],guard[1]]
    gallery[guard[0],guard[1]]=4
    guards[index2] = guard
    index2+=1
    

#print(guards)
#plt.imshow(gallery)
#plt.show()

#------------------------------------------------------------------------------
#                           Placement iteration 
#------------------------------------------------------------------------------
itercount=0
while itercount <= totalsteps:
 
    for guard in guards:            #Applying the viewing function from wall_finder.py                             
        gallery=vision(guard,gallery,1/reso)
        print()
        print(guard)
    plt.imshow(gallery)
    plt.show()
    

    viewedarea= gallery!=0          #Here a Boolean matrix is returned where "True" means visible, wall, table or guard
    viewedblocks=sum(sum(viewedarea))  #Sums the amount of visible 'blocks'
    perc= viewedblocks/(size[0]*size[1])*100    #calculates % of viewed blocks
    print(perc,"%"," of the room is visible.")


    
    noguards= gallery < 4
    novis= gallery != 2   #'Resets' the gallery matrix
    gallery= gallery*noguards*novis   

    if itercount <totalsteps:
        steps=['00','01','11','01']
        poss=list(permutations(steps))
        moves=poss[randint(0,len(poss)-1)]
        walkingcode1='01010101'
        walkingcode2='00000000'
        # n=2
        # if itercount==0:        #This splits the walking code into the different steps for the different guards
        #     moves=[walkingcode1[i:i+n] for i in range(0,len(walkingcode1),n)]
        # elif itercount==1:
        #     moves=[walkingcode2[i:i+n] for i in range(0,len(walkingcode2),n)]
        print(moves)
        i=0
        step=1*reso
        for move in moves:
            if move=='01': #move left
                a=guards[i][1]
                a-=step
                if a<0:
                  a=1  
                value= gallery[guards[i][0],a]
                if value !=1 and value !=-1:
                    guards[i][1]=a
                else:
                    print("Can't walk into a wall")

            elif move== '10': #move right
                a=guards[i][1]
                a+=step
                if a>(size[1]-1):
                    a=size[1]-2
                value= gallery[guards[i][0],a]
                if value !=1 and value !=-1:
                    guards[i][1]=a
                else:
                    print("Can't walk into a wall")
                
            elif move=='00':#move forward
                a=guards[i][0]
                a+=step
                if a>(size[0]-1):
                    a=size[0]-2
                value= gallery[a,guards[i][1]]
                if value !=1 and value !=-1:
                    guards[i][0]=a
                else:
                    print("Can't walk into a wall")
                
            elif move=='11': #move backwards
                a=guards[i][0]
                a-=step
                if a<0:
                  a=1  
                value= gallery[a,guards[i][1]]
                if value !=1 and value !=-1:
                    guards[i][0]=a
                else:
                    print("Can't walk into a wall")
            i+=1
            
    i=0
    for guard in guards:                    #Checking if the new guard placement doesn't place guards on walls or tables                                         
        gallery[guard[0],guard[1]]=4
        guards[i] = guard
        i+=1
    itercount+=1
    print("New positions")
    print(guards)





