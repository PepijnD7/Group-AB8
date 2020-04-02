from matplotlib import pyplot as plt
import numpy as np
import scipy as sp
from scipy.integrate import simps
from scipy import signal
from numpy import trapz


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
disp1 = []
force1 = []
disp2 = []
force2 = []
disp3 = []
force3 = []
disp4 = []
force4 = []

#read the files
for line in lines1:
    if len(line.strip())>0:
        columns_0 = line.split("\t")

        columns_1 = list(filter(None, columns_0))

        for i in range(len(columns_1)):
            columns_1[i] = columns_1[i].strip()


        if columns_1[0].isalpha() == False and columns_1[1].isalpha() == False:
            disp1.append(float(columns_1[1]))
            force1.append(float(columns_1[0]))

for dog in lines2:
  if len(dog.strip())>0:
        columns_0 = dog.split("\t")

        columns_1 = list(filter(None, columns_0))

        for i in range(len(columns_1)):
            columns_1[i] = columns_1[i].strip()


        if columns_1[0].isalpha() == False and columns_1[1].isalpha() == False:
            disp2.append(float(columns_1[1]))
            force2.append(float(columns_1[0]))

for cat in lines3:
  if len(cat.strip())>0:
        columns_0 = cat.split("\t")

        columns_1 = list(filter(None, columns_0))

        for i in range(len(columns_1)):
            columns_1[i] = columns_1[i].strip()


        if columns_1[0].isalpha() == False and columns_1[1].isalpha() == False:
            disp3.append(float(columns_1[1]))
            force3.append(float(columns_1[0]))

for giraffe in lines4:
  if len(giraffe.strip())>0:
        columns_0 = giraffe.split("\t")

        columns_1 = list(filter(None, columns_0))

        for i in range(len(columns_1)):
            columns_1[i] = columns_1[i].strip()


        if columns_1[0].isalpha() == False and columns_1[1].isalpha() == False:
            disp4.append(float(columns_1[1]))
            force4.append(float(columns_1[0]))


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

#adding a smoothing filter to the data
N= 30
smoothforces=[0,0,0,0]
smoothdisps=[0,0,0,0]


for i in range(len(smoothforces)):
 smoothforces[i]=sp.ndimage.gaussian_filter(forces[i],3)
 smoothdisps[i]=sp.ndimage.gaussian_filter(disps[i],3)
#   smoothforces[i]=sp.signal.savgol_filter(forces[i],41,4)
#   smoothdisps[i]=sp.signal.savgol_filter(disps[i],41,4)



#work done
work1 = trapz(force1,disp1)
work2 = trapz(force2,disp2)
work3 = trapz(force3,disp3)
work4 = trapz(force4,disp4)



#plots for force vs displacement
plt.scatter(disps[0],forces[0],color='r',marker='.')
# plt.scatter(disps[1],forces[1],color='g',marker='.')
# plt.scatter(disps[2],forces[2],color='b',marker='.')
# plt.scatter(disps[3],forces[3],color='y',marker='.')
plt.plot(smoothdisps[0],smoothforces[0],color='brown')
# plt.plot(smoothdisps[1],smoothforces[1],color='darkolivegreen')
# plt.plot(smoothdisps[2],smoothforces[2],color='darkblue')
# plt.plot(smoothdisps[3],smoothforces[3],color='orange')
plt.show()

#prints results

print(work1)
print(work3)
print(work2)
print(work4)