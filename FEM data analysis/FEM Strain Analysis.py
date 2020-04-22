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



########################################################################################################
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
########################################################################################################





########################################################################################################
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
########################################################################################################





########################################################################################################
# Get the axial strain and place in 5 new lists:
axialstr1 = []
axialstr2 = []
axialstr3 = []
axialstr4 = []
axialstr5 = []

for i in range(0,1114):
    axial1 = sqrt( (strain_x_1[i])**2 + (strain_y_1[i])**2 + (strain_z_1[i])**2 )
    axial2 = sqrt( (strain_x_2[i])**2 + (strain_y_2[i])**2 + (strain_z_2[i])**2 )
    axial3 = sqrt( (strain_x_3[i])**2 + (strain_y_3[i])**2 + (strain_z_3[i])**2 )
    axial4 = sqrt( (strain_x_4[i])**2 + (strain_y_4[i])**2 + (strain_z_4[i])**2 )
    axial5 = sqrt( (strain_x_5[i])**2 + (strain_y_5[i])**2 + (strain_z_5[i])**2 )

    axialstr1.append(axial1)
    axialstr2.append(axial2)
    axialstr3.append(axial3)
    axialstr4.append(axial4)
    axialstr5.append(axial5)
########################################################################################################





########################################################################################################
# We need a loop to separate double measurements at each node:
# NOTE: "even" and "uneven" stand for the row index i
# NOTE2.0: "even" indices are on the outside, "uneven" indices are on the inside
# First separate the nodes so plot gets inputs with the same dimensions
nodes_once = []
nodes_once = []

for i in range (0, len(node_list)):
    node = node_list[i]
    if i%2 == 0:
        nodes_once.append(node)

# Generate axial strain lists for inside and outside:
axialstr1_out = []
axialstr1_in  = []
axialstr2_out = []
axialstr2_in  = []
axialstr3_out = []
axialstr3_in  = []
axialstr4_out = []
axialstr4_in  = []
axialstr5_out = []
axialstr5_in  = []

for i in range (4, len(strain_x_1)-2):
    data1 = axialstr1[i]
    data2 = axialstr2[i]
    data3 = axialstr3[i]
    data4 = axialstr4[i]
    data5 = axialstr5[i]
    if i%2 == 0:
        axialstr1_out.append(data1)
        axialstr2_out.append(data2)
        axialstr3_out.append(data3)
        axialstr4_out.append(data4)
        axialstr5_out.append(data5)
    else:
        axialstr1_in.append(data1)
        axialstr2_in.append(data2)
        axialstr3_in.append(data3)
        axialstr4_in.append(data4)
        axialstr5_in.append(data5)
        
########################################################################################################





########################################################################################################
# Plot strains:
plt.plot(arc,axialstr1_out, label='Loadstep 1, out')
plt.plot(arc,axialstr1_in,  label='Loadstep 1, in')
plt.xlabel("Arc length [mm]")
plt.ylabel("Axial strain")
plt.title("Axial strain on the inside and outside")
plt.grid()
plt.legend()
plt.show()
########################################################################################################








########################################################################################################
# In case we have to calculate strain energy: ??

# Young's modulus of aluminium, E [Pa]
E = 71 * 10^9 

# Strain energy can be calculated: U = 0.5 * E * strain^2. E = Young's modulus
U_x1 = 0.5 * E * strain_x_1 * strain_x_1
U_x2 = 0.5 * E * strain_x_2 * strain_x_2
U_x3 = 0.5 * E * strain_x_3 * strain_x_3
U_x4 = 0.5 * E * strain_x_4 * strain_x_4
U_x5 = 0.5 * E * strain_x_5 * strain_x_5






