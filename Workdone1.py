from matplotlib import pyplot as plt
import numpy as np
import scipy as sp
from scipy.integrate import simps
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
            disp.append(columns_1[0])
            force.append(columns_1[1])

new_disp = []
for item in disp:
    new_disp.append(float(item))

new_force = []
for item in force:
    new_force.append(float(item))

convert = np.asarray(new_force)
convert1 = np.asarray(new_disp)


work = trapz(convert,convert1)
work1 = trapz(convert1,convert)

print(work)
print(work1)
