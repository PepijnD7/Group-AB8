# FEM Force and Displacement analysis:

from math import *
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
from scipy import integrate
from smoothlists import smoothdisps,partwork

# Open Force and Displacement file:
ForceDisp = open("femForceDisplacement.txt")
lines = ForceDisp.readlines()
ForceDisp.close()


# Create arrays from data:
array = np.genfromtxt("femForceDisplacement.txt",skip_header=1)


# Create arrays to plot:
displacement = array[:,0]
force        = array[:,1]

displacement1 = [array[1,0]]
displacement2 = [array[2,0]]
displacement3 = [array[3,0]]
displacement4 = [array[4,0]]
force1 = [array[1,1]]
force2 = [array[2,1]]
force3 = [array[3,1]]
force4 = [array[4,1]]

# Create spline to fit a curve through the force-displacement data:
x_axis = np.linspace(0,39.2,50)  # displacement interval
spline = interpolate.interp1d(displacement, force, kind="cubic")


# Integrate the spline to find the work done:
work = [] 
for i in range(len(x_axis)):
    U = integrate.trapz(spline(x_axis[:i]),x_axis[:i])
    work.append(U/1000)
    

print(work)

# Plot force and displacement:
plt.plot(x_axis, spline(x_axis), color='dimgrey')
#plt.plot(0 , 0 , 'b' , marker='o')
plt.plot(displacement1, force1, color='dimgrey', marker='o')
plt.plot(displacement2, force2, color='dimgrey', marker='o')
plt.plot(displacement3, force3, color='dimgrey', marker='o')
plt.plot(displacement4, force4, color='dimgrey', marker='o')
plt.ylabel("Actuation force [N]")
plt.xlabel("Displacement [mm]")
plt.xlim(0,40)
plt.ylim(0,1300)
plt.grid()
plt.show()


# Plot work and displacement:
plt.plot(x_axis, work, color='dimgrey', linestyle='dashed', label='Strain energy (FEM)')
plt.plot(smoothdisps, partwork, color='dimgrey', label='Actuation energy (experiment)')
plt.ylabel("Work [J]")
plt.xlabel("Displacement [mm]")
plt.grid()
plt.legend()
plt.xlim(0,40)
plt.ylim(0,30)
plt.show()


print('Done')
