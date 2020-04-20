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


# There are different files for each applied force. This is indicated by the loadsteps 1 till 5:
# Loadstep 1 => strain measurement 1 => extension 0 [mm]
# Loadstep 2 => strain measurement 13 => extension 10 [mm]
# Loadstep 3 => strain measurement 28 => extension 20 [mm]
# Loadstep 4 => strain measurement 40 => extension 30 [mm]
# Loadstep 5 => strain measurement 55 => extension 39.2 [mm]
# ------------------------------------------------------------------------------------------------

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


# Create five arrays (with all strains for each load step):
array_str1 = np.genfromtxt("FEMstrain1.txt",skip_header=1)
array_str2 = np.genfromtxt("FEMstrain2.txt",skip_header=1)
array_str3 = np.genfromtxt("FEMstrain3.txt",skip_header=1)
array_str4 = np.genfromtxt("FEMstrain4.txt",skip_header=1)
array_str5 = np.genfromtxt("FEMstrain5.txt",skip_header=1)

# Get node numbers:
node_list = array_str1[:,0]


# Now, we need all the (shear) strains for each loadstep (1 till 5) and place them in a list
# Get strain for load step 1:
strain_x_1 = array_str1[:,1]
strain_y_1 = array_str1[:,2]
strain_z_1 = array_str1[:,3]
strain_xy_1 = array_str1[:,4]
strain_yz_1 = array_str1[:,5]
strain_xz_1 = array_str1[:,6]

# Get strain for load step 2:
strain_x_2 = array_str2[:,1]
strain_y_2 = array_str2[:,2]
strain_z_2 = array_str2[:,3]
strain_xy_2 = array_str2[:,4]
strain_yz_2 = array_str2[:,5]
strain_xz_2 = array_str2[:,6]

# Get strain for load step 3:
strain_x_3 = array_str3[:,1]
strain_y_3 = array_str3[:,2]
strain_z_3 = array_str3[:,3]
strain_xy_3 = array_str3[:,4]
strain_yz_3 = array_str3[:,5]
strain_xz_3 = array_str3[:,6]

# Get strain for load step 4:
strain_x_4 = array_str4[:,1]
strain_y_4 = array_str4[:,2]
strain_z_4 = array_str4[:,3]
strain_xy_4 = array_str4[:,4]
strain_yz_4 = array_str4[:,5]
strain_xz_4 = array_str4[:,6]

# Get strain for load step 5:
strain_x_5 = array_str5[:,1]
strain_y_5 = array_str5[:,2]
strain_z_5 = array_str5[:,3]
strain_xy_5 = array_str5[:,4]
strain_yz_5 = array_str5[:,5]
strain_xz_5 = array_str5[:,6]



# We need to find the arclenght of the demonstrator, such that we can plot the strain vs. the arclenght:
coordinatefile = open("shell_loadstep1_disp.out")
lines1 = coordinatefile.readlines()
coordinatefile.close()

array_coordinates = np.genfromtxt("shell_loadstep1_disp.out",skip_header=1)

x = array_coordinates[:,2]*1000 # x coordinates in [mm]
y = array_coordinates[:,3]*1000 # y coordinates in [mm] 

arc = []
length = 0
for i in range(2,len(x)-1):
    length = length + sqrt((abs(x[i]-x[i+1]))**2 + (abs(y[i]-y[i+1]))**2 )
    arc.append(length)
    i = i+1



# We need a loop to separate double measurements at each node:
# NOTE: "even" and "uneven" stand for the row index i

# First separate the nodes so plot gets inputs with the same dimensions
nodes_once = []
nodes_once = []

for i in range (0, len(node_list)):
    node = node_list[i]
    if i%2 == 0:
        nodes_once.append(node)

# For strain in x-direction
strain_x_1_even = []
strain_x_1_uneven = []
for i in range (5, len(strain_x_1)):
    data = strain_x_1[i]
    if i%2 == 0:
        strain_x_1_even.append(data)
    else:
        strain_x_1_uneven.append(data)





# Plot strains:
plt.plot(arc,strain_x_1_even, label='strain_x1_even')
# plt.plot(arc,strain_x_1_uneven, label='strain_x1_uneven')
plt.xlabel("Arc length [mm]")
plt.ylabel("")
plt.title("Strain in x-direction")
plt.grid()
plt.legend()
plt.show()






# In case we have to calculate strain energy: ??

# Young's modulus of aluminium, E [Pa]
E = 71 * 10^9 

# Strain energy can be calculated: U = 0.5 * E * strain^2. E = Young's modulus
U_x1 = 0.5 * E * strain_x_1 * strain_x_1
U_x2 = 0.5 * E * strain_x_2 * strain_x_2
U_x3 = 0.5 * E * strain_x_3 * strain_x_3
U_x4 = 0.5 * E * strain_x_4 * strain_x_4
U_x5 = 0.5 * E * strain_x_5 * strain_x_5






