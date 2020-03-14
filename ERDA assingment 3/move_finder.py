import numpy as np
from wall_finder import vision
from itertools import permutations
from percentage import percentage
from copy import deepcopy
import matplotlib.pyplot as plt

def best_move(permpositions,gallery,reso,size,poss,step):
    movenbr=0
    bestmove=[0,0]
    for moves in poss:
        i=0
        guards=deepcopy(permpositions) # Resets the guard matrix        
        for move in moves:
            if move=='01': #move left
                a=guards[i][1]
                a-=step
                if a<0:
                    a=1
                value= gallery[guards[i][0],a]
                if value !=1 and value !=-1:
                    guards[i][1]=a



            elif move== '10': #move right
                a=guards[i][1]
                a+=step
                if a>(size[1]-1):
                    a=size[1]-2
                value= gallery[guards[i][0],a]
                if value !=1 and value !=-1:
                    guards[i][1]=a



            elif move=='00':#move forward
                a=guards[i][0]
                a+=step
                if a>(size[0]-1):
                    a=size[0]-2
                value= gallery[a,guards[i][1]]
                if value !=1 and value !=-1:
                    guards[i][0]=a



            elif move=='11': #move backwards
                a=guards[i][0]
                a-=step
                if a<0:
                    a=1
                value= gallery[a,guards[i][1]]
                if value !=1 and value !=-1:
                    guards[i][0]=a


            i+=1  
 
        for guard in guards:                #Updates gallery with guard positions                                         
            gallery[guard[0],guard[1]]=4


        for guard in guards:            #Applying the viewing function from wall_finder.py
            gallery=vision(guard,gallery,1/reso,100)

            

        newperc= percentage(gallery,size)
        if newperc> bestmove[0]:
            perc=newperc
            bestmove[0]=perc
            bestmove[1]=movenbr
            print(perc,poss[movenbr])

        
        noguards= gallery < 4       #'Resets' the gallery matrix
        novis= gallery != 2   
        gallery= gallery*noguards*novis
        movenbr+=1


    nextmove=poss[bestmove[1]]
    print("The best move is:", nextmove)
    print("Viewing percentage is:", bestmove[0])
    return nextmove

        
    