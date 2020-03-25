# FEM displacement analysis


# Discription from README.txt:
# ------------------------------------------------------------------------------------------------
# shell_loadstepX_disp.out and shell_loadstepX_str.out contain the displacement and strain data
# from the finite element model for load step X, respectively. The displacement data
# contains a counter number, the node number, the x,y,z coordinates,
# and displacements in x,y,z direction of the nodes of the FEM. 
# The strain data contains the node number and the x,y,z,xy,yz,xz engineering strain data
# of the nodes of the FEM in a global reference frame. This data needs to be modified such
# that it can be compared to the strain measured with the optical fiber.
# ------------------------------------------------------------------------------------------------

# There are different files for each applied force. This is indicated by the loadsteps 1 till 5



from math import *
import matplotlib.pyplot as plt
import numpy as np


# Open five files (for each different loadstep):
shell_loadstep1_disp = open("shell_loadstep1_disp.out")
lines1_disp = shell_loadstep1_disp.readlines()
shell_loadstep1_disp.close()

shell_loadstep2_disp = open("shell_loadstep2_disp.out")
lines2_disp = shell_loadstep2_disp.readlines()
shell_loadstep2_disp.close()

shell_loadstep3_disp = open("shell_loadstep3_disp.out")
lines3_disp = shell_loadstep3_disp.readlines()
shell_loadstep3_disp.close()

shell_loadstep4_disp = open("shell_loadstep4_disp.out")
lines4_disp = shell_loadstep4_disp.readlines()
shell_loadstep4_disp.close()

shell_loadstep5_disp = open("shell_loadstep5_disp.out")
lines5_disp = shell_loadstep5_disp.readlines()
shell_loadstep5_disp.close()


# Create five arrays:
array_disp1 = np.genfromtxt("shell_loadstep1_disp.out", skip_header=1)
array_disp2 = np.genfromtxt("shell_loadstep2_disp.out", skip_header=1)
array_disp3 = np.genfromtxt("shell_loadstep3_disp.out", skip_header=1)
array_disp4 = np.genfromtxt("shell_loadstep4_disp.out", skip_header=1)
array_disp5 = np.genfromtxt("shell_loadstep5_disp.out", skip_header=1)


# Create lists of node locations:
node_list = array_disp1[:,1]
x_list    = array_disp1[:,2]
y_list    = array_disp1[:,3]
z_list    = array_disp1[:,4]

# Create lists of displacements in x-direction:
dx_list1 = array_disp1[:,5]
dx_list2 = array_disp2[:,5]
dx_list3 = array_disp3[:,5]
dx_list4 = array_disp4[:,5]
dx_list5 = array_disp5[:,5]

# Create lists of displacements in y-direction:
dy_list1 = array_disp1[:,6]
dy_list2 = array_disp2[:,6]
dy_list3 = array_disp3[:,6]
dy_list4 = array_disp4[:,6]
dy_list5 = array_disp5[:,6]

# Create lists of displacements in z-direction:
dz_list1 = array_disp1[:,7]
dz_list2 = array_disp2[:,7]
dz_list3 = array_disp3[:,7]
dz_list4 = array_disp4[:,7]
dz_list5 = array_disp5[:,7]


# Plot leading edge demonstrator contours:
plt.plot(x_list,y_list,'b', linestyle='solid')
plt.grid()
plt.show()


# Plot x-direction displacements for each loadstep:
plt.plot(node_list, dx_list1, 'b', linestyle='solid', label='loadstep 1')
plt.plot(node_list, dx_list2, 'r', linestyle='solid', label='loadstep 2')
plt.plot(node_list, dx_list3, 'g', linestyle='solid', label='loadstep 3')
plt.plot(node_list, dx_list4, 'y', linestyle='solid', label='loadstep 4')
plt.plot(node_list, dx_list5, 'c', linestyle='solid', label='loadstep 5')
plt.title("Displacement in x-direction for each loadstep")
plt.xlabel("node number [-]")
plt.ylabel("dx [?]")
plt.grid()
plt.legend()
plt.show()


# Plot y-direction displacements for each loadstep:
plt.plot(node_list, dy_list1, 'b', linestyle='solid', label='loadstep 1')
plt.plot(node_list, dy_list2, 'r', linestyle='solid', label='loadstep 2')
plt.plot(node_list, dy_list3, 'g', linestyle='solid', label='loadstep 3')
plt.plot(node_list, dy_list4, 'y', linestyle='solid', label='loadstep 4')
plt.plot(node_list, dy_list5, 'c', linestyle='solid', label='loadstep 5')
plt.title("Displacement in y-direction for each loadstep")
plt.xlabel("node number [-]")
plt.ylabel("dy [?]")
plt.grid()
plt.legend()
plt.show()

# Plot z-direction displacements for each loadstep:
plt.plot(node_list, dz_list1, 'b', linestyle='solid', label='loadstep 1')
plt.plot(node_list, dz_list2, 'r', linestyle='solid', label='loadstep 2')
plt.plot(node_list, dz_list3, 'g', linestyle='solid', label='loadstep 3')
plt.plot(node_list, dz_list4, 'y', linestyle='solid', label='loadstep 4')
plt.plot(node_list, dz_list5, 'c', linestyle='solid', label='loadstep 5')
plt.title("Displacement in z-direction for each loadstep")
plt.xlabel("node number [-]")
plt.ylabel("dz [?]")
plt.grid()
plt.legend()
plt.show()
