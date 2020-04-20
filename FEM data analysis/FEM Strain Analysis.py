# FEM strain analysis


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
strain1 = open("FEMstrain1.txt")
lines1 = strain1.readlines()
strain1.close()

strain2 = open("FEMstrain2.txt")
lines2 = strain2.readlines()
strain2.close()

strain3 = open("FEMstrain3.txt")
lines3 = strain3.readlines()
strain3.close()

strain4 = open("FEMstrain4.txt")
lines4 = strain4.readlines()
strain4.close()

strain5 = open("FEMstrain5.txt")
lines5_str = strain5.readlines()
strain5.close()


# Create five arrays:
array_str1 = np.genfromtxt("FEMstrain1.txt",skip_header=1)
array_str2 = np.genfromtxt("FEMstrain2.txt",skip_header=1)
array_str3 = np.genfromtxt("FEMstrain3.txt",skip_header=1)
array_str4 = np.genfromtxt("FEMstrain4.txt",skip_header=1)
array_str5 = np.genfromtxt("FEMstrain5.txt",skip_header=1)

# Get node numbers:
node_list = array_str1[:,0]


# Now, we need all the (shear) strains for each loadstep (1 till 5) and place them in a list
# Get strain in x-direction:
strain_x_1 = array_str1[:,1]
strain_x_2 = array_str2[:,1]
strain_x_3 = array_str3[:,1]
strain_x_4 = array_str4[:,1]
strain_x_5 = array_str5[:,1]
# Get strain in y-direction:
strain_y_1 = array_str1[:,2]
strain_y_2 = array_str2[:,2]
strain_y_3 = array_str3[:,2]
strain_y_4 = array_str4[:,2]
strain_y_5 = array_str5[:,2]
# Get strain in z-direction:
strain_z_1 = array_str1[:,3]
strain_z_2 = array_str2[:,3]
strain_z_3 = array_str3[:,3]
strain_z_4 = array_str4[:,3]
strain_z_5 = array_str5[:,3]
# Get (shear) strain in xy-direction:
strain_xy_1 = array_str1[:,4]
strain_xy_2 = array_str2[:,4]
strain_xy_3 = array_str3[:,4]
strain_xy_4 = array_str4[:,4]
strain_xy_5 = array_str5[:,4]
# Get (shear) strain in yz-direction:
strain_yz_1 = array_str1[:,5]
strain_yz_2 = array_str2[:,5]
strain_yz_3 = array_str3[:,5]
strain_yz_4 = array_str4[:,5]
strain_yz_5 = array_str5[:,5]
# Get (shear) strain in xz-direction:
strain_xz_1 = array_str1[:,6]
strain_xz_2 = array_str2[:,6]
strain_xz_3 = array_str3[:,6]
strain_xz_4 = array_str4[:,6]
strain_xz_5 = array_str5[:,6]



# loop meant to separate double measurements at each node
# NOTE: "even" and "uneven" stand for the row index i

# first separate the nodes so plot gets inputs with the same dimensions
nodes_once = []
nodes_once = []

for i in range (0, len(node_list)):
    node = node_list[i]
    if i%2 == 0:
        nodes_once.append(node)

# for strain in x-direction
strain_x_1_even = []
strain_x_1_uneven = []
for i in range (0, len(strain_x_1)):
    data = strain_x_1[i]
    if i%2 == 0:
        strain_x_1_even.append(data)
    else:
        strain_x_1_uneven.append(data)
        


# plot the graphs
plt.plot(nodes_once,strain_x_1_even, label='x1_even')
plt.plot(nodes_once,strain_x_1_uneven, label='x1_uneven')
plt.xlabel("Node number")
plt.ylabel("")
plt.title("Strain in x-direction")
plt.grid()
plt.legend()
plt.show()



