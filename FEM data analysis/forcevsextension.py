from matplotlib import pyplot as plt
import numpy as np
import scipy as sp
from scipy.integrate import simps
from scipy import signal
from numpy import trapz
import statistics as st
from extension_time_new_factors import t1,t2,t3,t4,f1,f2,f3,f4,dis1,dis2,dis3,dis4



#open the files

file1 = open("data1.txt")
lines1 = file1.readlines()
file1.close()
file2 = open("data2.txt")
lines2 = file2.readlines()
file2.close()
file3 = open("data3.txt")
lines3 = file3.readlines()
file3.close()
file4 = open("data4.txt")
lines4 = file4.readlines()
file4.close()

#store the data
disp1 = dis1
force1 = f1
disp2 = dis2
force2 = f2
disp3 = dis3
force3 = f3
disp4 = dis4
force4 = f4




#read the files (not used anymore)
"""
for line in lines1:
    if len(line.strip())>0:
        columns_0 = line.split("\t")

        columns_1 = list(filter(None, columns_0))

        for i in range(len(columns_1)):
            columns_1[i] = columns_1[i].strip()


        if columns_1[0].isalpha() == False and columns_1[1].isalpha() == False:
            disp1.append(float(columns_1[1]))
            #force1.append(float(columns_1[0]))

for dog in lines2:
  if len(dog.strip())>0:
        columns_0 = dog.split("\t")

        columns_1 = list(filter(None, columns_0))

        for i in range(len(columns_1)):
            columns_1[i] = columns_1[i].strip()


        if columns_1[0].isalpha() == False and columns_1[1].isalpha() == False:
            disp2.append(float(columns_1[1]))
            #force2.append(float(columns_1[0]))

for cat in lines3:
  if len(cat.strip())>0:
        columns_0 = cat.split("\t")

        columns_1 = list(filter(None, columns_0))

        for i in range(len(columns_1)):
            columns_1[i] = columns_1[i].strip()


        if columns_1[0].isalpha() == False and columns_1[1].isalpha() == False:
            disp3.append(float(columns_1[1]))
            #force3.append(float(columns_1[0]))

for giraffe in lines4:
  if len(giraffe.strip())>0:
        columns_0 = giraffe.split("\t")

        columns_1 = list(filter(None, columns_0))

        for i in range(len(columns_1)):
            columns_1[i] = columns_1[i].strip()


        if columns_1[0].isalpha() == False and columns_1[1].isalpha() == False:
            disp4.append(float(columns_1[1]))
            #force4.append(float(columns_1[0]))
"""


#make the tabs arrays cause the trapz function only works with arrays
forces=[0,0,0,0]
disps=[0,0,0,0]

force1 = np.array(force1)
disp1 = np.array(disp1)
force2 = np.array(force2)
disp2 = np.array(disp2)
force3 = np.array(force3)
disp3 = np.array(disp3)
force4 = np.array(force4)
disp4 = np.array(disp4)

forces[0],forces[1],forces[2],forces[3]=force1,force2,force3,force4
disps[0],disps[1],disps[2],disps[3]=disp1,disp2,disp3,disp4

#adding a smoothing filter to the data, gaussian 
stdev=4 
smoothforces=[0,0,0,0]
smoothdisps=[0,0,0,0]


for i in range(len(smoothforces)):
    smoothforces[i]=list(sp.ndimage.gaussian_filter(forces[i],stdev))
    smoothdisps[i]=list(sp.ndimage.gaussian_filter(disps[i],stdev))




partwork=[np.zeros(len(smoothforces[0])),np.zeros(len(smoothforces[1])),np.zeros(len(smoothforces[2])),np.zeros(len(smoothforces[3]))]
#Work over time
for j in range(len(smoothforces)):
    for i in range(len(smoothforces[j][:])):
        partwork[j][i]=trapz(smoothforces[j][:i],(np.array(smoothdisps[j][:i]))/1000)

# plots the work done vs time
#plt.grid(True)
#plt.xlabel("Time [s]")
#plt.ylabel("Energy [J]")
#plt.ylim(0,30)
#plt.xlim(0,40)
#plt.xticks(np.arange(0,42.5,2.5))
#plt.yticks(range(0,32,))
#plt.plot(smoothdisps[0],partwork[0],color='r',label='10mm')
#plt.plot(smoothdisps[1],partwork[1],color='g',label='20 mm')
#plt.plot(smoothdisps[2],partwork[2],color='b',label='30 mm')
#plt.plot(smoothdisps[3],partwork[3],color='y',label='39 mm')
#plt.legend()
#plt.show()




#Total work done
work1 = trapz(force1,disp1)
work2 = trapz(force2,disp2)
work3 = trapz(force3,disp3)
work4 = trapz(force4,disp4)





#plots for force vs displacement
# plt.grid(True)
# plt.xlabel("Extension [mm]")
# plt.ylabel("Force [N]")
# plt.xticks(np.arange(-2,42,2))
# plt.yticks(np.arange(-100,1300,100))
# plt.xlim(-2,40)
# plt.ylim(-100,1200)
# plt.scatter(disps[0],forces[0],color='r',marker='.',s=7)
# plt.scatter(disps[1],forces[1],color='g',marker='.',s=7)
# plt.scatter(disps[2],forces[2],color='b',marker='.',s=7)
# plt.scatter(disps[3],forces[3],color='y',marker='.',s=7)
# plt.plot(smoothdisps[0],smoothforces[0],color='brown',label='10 mm')
# plt.plot(smoothdisps[1],smoothforces[1],color='darkolivegreen', label='20 mm')
# plt.plot(smoothdisps[2],smoothforces[2],color='darkblue', label='30 mm')
# plt.plot(smoothdisps[3],smoothforces[3],color='orange', label='39 mm')


# plt.legend()
# plt.show()

#prints results

# print(work1)
# print(work3)
# print(work2)
# print(work4)


print(smoothdisps[3])
print()
print(partwork[3])
