# FEM Force and Displacement analysis:

from math import *
import matplotlib.pyplot as plt
import numpy as np



# Open Force and Displacement file:
ForceDisp = open("femForceDisplacement.txt")
lines = ForceDisp.readlines()
ForceDisp.close()


# Create arrays from data:
array = np.genfromtxt("femForceDisplacement.txt",skip_header=1)


# Create lists to plot:
displacement = array[:,0]   # Displacement
force = array[:,1]          # Actuation force


# Plot force and displacement:
plt.plot(force, displacement, 'r', linestyle='solid', marker='o')
plt.xlabel("Actuation force [N]")
plt.ylabel("Displacement [mm]")
plt.legend()
plt.title("Actuation force vs. displacement")
plt.grid()
plt.show()
