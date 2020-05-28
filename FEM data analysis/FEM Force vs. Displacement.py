# FEM Force and Displacement analysis:

import matplotlib
from math import *
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
from scipy import integrate
from smoothlists import smoothdisps,partwork

fig, ax = plt.subplots(constrained_layout=True)



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
x_axis = np.linspace(0,39.2,500)  # displacement interval
spline = interpolate.interp1d(displacement, force, kind="cubic")


# Integrate the spline to find the work done:
work = [] 
for i in range(len(x_axis)):
    U = integrate.trapz(spline(x_axis[:i]),x_axis[:i])
    work.append(U/1000)


# Find the ratio
ratio =  np.array(work[100:])/np.array(partwork[100:])


# Plot force and displacement:
plt.plot(x_axis, spline(x_axis), color='dimgrey')
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
fig, ax1 = plt.subplots()

ax1.grid()
ax1.set_ylabel("Energy [J]")
ax1.set_xlabel("Displacement [mm]")
ax1.set_xlim(0,40)
ax1.set_ylim(0,30)
ax1.tick_params(axis='y')
lns1 = ax1.plot(smoothdisps, partwork, color='dimgrey', label='Actuation energy (experiment)')
lns2 = ax1.plot(x_axis, work, color='dimgrey', linestyle='dashed', label='Strain energy (FEM)')


ax2 = ax1.twinx()

ax2.set_ylim(0,1.0)
lns3 = ax2.plot(x_axis[100:], ratio, color='dimgrey', linestyle='dotted', label='Strain energy/actuation energy')
ax2.tick_params(axis='y')
ax2.set_ylabel('Energy ratio [-]')

lns = lns1+lns2+lns3
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc=0)

fig.tight_layout()




plt.show()


print('Done')
