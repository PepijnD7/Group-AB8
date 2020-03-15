import numpy as np
from wall_finder import vision
from itertools import permutations
from percentage import percentage
from copy import deepcopy
import statistics
from random import randint
import matplotlib.pyplot as plt

def best_perc_indexes(list):
    p = statistics.median(list)
    res = []
    maxidx = 0
    for idx in range(len(list)):
        if list[idx] > p:
            res.append(idx)
        if list[idx] == max(list):
            maxidx = idx

    return res,maxidx




def natural_selection(permpositions,gallery,reso,size,poss,step,steps):

    newposs = []
    percentages = []
    for moves in poss:
        guards=deepcopy(permpositions) # Resets the guard matrix
        i = 0
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
            i +=1


 
        for guard in guards:                #Updates gallery with guard positions                                         
            gallery[guard[0],guard[1]]=4


        for guard in guards:            #Applying the viewing function from wall_finder.py
            gallery=vision(guard,gallery,1/reso,200)

        percentages.append(percentage(gallery,size))            #save the percentage for this move

        
        noguards= gallery < 4       #'Resets' the gallery matrix
        novis= gallery != 2   
        gallery= gallery*noguards*novis


    best_index, maxidx = best_perc_indexes(percentages)
    for index in best_index:  #gets the best individuals
        newposs.append(poss[index])

    t = 0
    while t<len(poss)/2:                             #creates 50 new mutations
        individual = newposs[t]
        mutation = steps[randint(0,3)]
        individual [randint(0,3)] = mutation

        newposs.append(individual)
        t+=1


    return newposs , maxidx            #returns the first of the new poss list, change this so it returns only after a few runs


def repeating_selection(permpositions,gallery,reso,size,poss,step,steps):
    newposs = natural_selection(permpositions,gallery,reso,size,poss,step,steps)[0]
    newposs_2 = natural_selection(permpositions,gallery,reso,size,newposs,step,steps)[0]
    newposs_3 = natural_selection(permpositions, gallery, reso, size, newposs_2, step, steps)[0]
    newposs_4 = natural_selection(permpositions, gallery, reso, size, newposs_3, step, steps)[0]

    newposs_5,maxidx = natural_selection(permpositions, gallery, reso, size, newposs_4, step, steps)

    return newposs_4[maxidx]

