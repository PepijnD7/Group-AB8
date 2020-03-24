from matplotlib import pyplot as plt
import numpy as np
import scipy as sp
from scipy.integrate import simps
from scipy import signal
from numpy import trapz

#Work done for the first displacement

file = open("data2.txt")
lines = file.readlines()
file.close()

disp = []
force = []

for line in lines:
    if len(line.strip())>0:
        columns_0 = line.split("\t")

        columns_1 = list(filter(None, columns_0))

        for i in range(len(columns_1)):
            columns_1[i] = columns_1[i].strip()


        if columns_1[0].isalpha() == False and columns_1[1].isalpha() == False:
            disp.append(float(columns_1[0]))
            force.append(float(columns_1[1]))



force = np.array(force)
disp = np.array(disp)
window=int(len(force)/10)
smoothforce= signal.savgol_filter(force,73,7)

work = trapz(force,disp)
smoothwork=trapz(smoothforce,disp)
work1 = trapz(disp,force)

plt.scatter(disp,force)
plt.plot(disp,smoothforce,color='r')
plt.show()

print(work)
print(smoothwork)
print(work1)
