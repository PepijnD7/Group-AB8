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


# Create arrays that make a distinction between strain on the inside and outside:
# NOTE: "even" indices are on the outside, "uneven" indices are on the inside
list_str1_out = []
list_str2_out = []
list_str3_out = []
list_str4_out = []
list_str5_out = []
list_str1_in = []
list_str2_in = []
list_str3_in = []
list_str4_in = []
list_str5_in = []


for i in range (0, len(array_str1)):
    data1 = array_str1[i]
    data2 = array_str2[i]
    data3 = array_str3[i]
    data4 = array_str4[i]
    data5 = array_str5[i]
    if i%2 == 0:
        list_str1_out.append(data1)
        list_str2_out.append(data2)
        list_str3_out.append(data3)
        list_str4_out.append(data4)
        list_str5_out.append(data5)
    else:
        list_str1_in.append(data1)
        list_str2_in.append(data2)
        list_str3_in.append(data3)
        list_str4_in.append(data4)
        list_str5_in.append(data5)

array_str1_out = np.array(list_str1_out)
array_str2_out = np.array(list_str2_out)
array_str3_out = np.array(list_str3_out)
array_str4_out = np.array(list_str4_out)
array_str5_out = np.array(list_str5_out)

array_str1_in = np.array(list_str1_in)
array_str2_in = np.array(list_str2_in)
array_str3_in = np.array(list_str3_in)
array_str4_in = np.array(list_str4_in)
array_str5_in = np.array(list_str5_in)





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
for i in range(0,len(x)-1):
    length = length + sqrt((abs(x[i]-x[i+1]))**2 + (abs(y[i]-y[i+1]))**2 )
    arc.append(length)
    i = i+1
########################################################################################################





########################################################################################################
# Get the angles between the local coordinate systems and the global coordinate system for each node:
theta = []
for i in range(0, len(x)-1):
    T = np.arctan(abs(y[i]-y[i+1])/abs(x[i]-x[i+1]))
    theta.append(T)

print(max(theta)) # Should be around pi/2 for the tip of the leading edge
print(len(theta))

########################################################################################################





########################################################################################################
# Now, we need all the strains for each loadstep (1 till 5) and place them in a list
# Get strain on inside and outside for load step 1:
str_out_x_1  = array_str1_out[:,1]
str_in_x_1   = array_str1_in[:,1]
str_out_y_1  = array_str1_out[:,2]
str_in_y_1   = array_str1_in[:,2]
str_out_z_1  = array_str1_out[:,3]
str_in_z_1   = array_str1_in[:,3]
str_out_xy_1 = array_str1_out[:,4]
str_in_xy_1  = array_str1_in[:,4]
str_out_yz_1 = array_str1_out[:,5]
str_in_yz_1  = array_str1_in[:,5]
str_out_xz_1 = array_str1_out[:,6]
str_in_xz_1  = array_str1_in[:,6]

# Get strain on inside and outside for load step 2:
str_out_x_2  = array_str2_out[:,1]
str_in_x_2   = array_str2_in[:,1]
str_out_y_2  = array_str2_out[:,2]
str_in_y_2   = array_str2_in[:,2]
str_out_z_2  = array_str2_out[:,3]
str_in_z_2   = array_str2_in[:,3]
str_out_xy_2 = array_str2_out[:,4]
str_in_xy_2  = array_str2_in[:,4]
str_out_yz_2 = array_str2_out[:,5]
str_in_yz_2  = array_str2_in[:,5]
str_out_xz_2 = array_str2_out[:,6]
str_in_xz_2  = array_str2_in[:,6]

# Get strain on inside and outside for load step 3:
str_out_x_3  = array_str3_out[:,1]
str_in_x_3   = array_str3_in[:,1]
str_out_y_3  = array_str3_out[:,2]
str_in_y_3   = array_str3_in[:,2]
str_out_z_3  = array_str3_out[:,3]
str_in_z_3   = array_str3_in[:,3]
str_out_xy_3 = array_str3_out[:,4]
str_in_xy_3  = array_str3_in[:,4]
str_out_yz_3 = array_str3_out[:,5]
str_in_yz_3  = array_str3_in[:,5]
str_out_xz_3 = array_str3_out[:,6]
str_in_xz_3  = array_str3_in[:,6]

# Get strain on inside and outside for load step 4:
str_out_x_4  = array_str4_out[:,1]
str_in_x_4   = array_str4_in[:,1]
str_out_y_4  = array_str4_out[:,2]
str_in_y_4   = array_str4_in[:,2]
str_out_z_4  = array_str4_out[:,3]
str_in_z_4   = array_str4_in[:,3]
str_out_xy_4 = array_str4_out[:,4]
str_in_xy_4  = array_str4_in[:,4]
str_out_yz_4 = array_str4_out[:,5]
str_in_yz_4  = array_str4_in[:,5]
str_out_xz_4 = array_str4_out[:,6]
str_in_xz_4  = array_str4_in[:,6]

# Get strain on inside and outside for load step 5:
str_out_x_5  = array_str5_out[:,1]
str_in_x_5   = array_str5_in[:,1]
str_out_y_5  = array_str5_out[:,2]
str_in_y_5   = array_str5_in[:,2]
str_out_z_5  = array_str5_out[:,3]
str_in_z_5   = array_str5_in[:,3]
str_out_xy_5 = array_str5_out[:,4]
str_in_xy_5  = array_str5_in[:,4]
str_out_yz_5 = array_str5_out[:,5]
str_in_yz_5  = array_str5_in[:,5]
str_out_xz_5 = array_str5_out[:,6]
str_in_xz_5  = array_str5_in[:,6]

########################################################################################################





########################################################################################################
# Get the transformed strain and place them in lists for xprime and yprime, both on the inside and outside:
str_xprime1_out = []
str_xprime2_out = []
str_xprime3_out = []
str_xprime4_out = []
str_xprime5_out = []

str_xprime1_in = []
str_xprime2_in = []
str_xprime3_in = []
str_xprime4_in = []
str_xprime5_in = []

str_yprime1_out = []
str_yprime2_out = []
str_yprime3_out = []
str_yprime4_out = []
str_yprime5_out = []

str_yprime1_in = []
str_yprime2_in = []
str_yprime3_in = []
str_yprime4_in = []
str_yprime5_in = []


for i in range(0,len(theta)):
    xprime1_out = str_out_x_1[i]*(np.cos(theta[i]))**2 + str_out_y_1[i]*(np.sin(theta[i]))**2 + 2*str_out_xy_1[i]*np.sin(theta[i])*np.cos(theta[i])
    xprime2_out = str_out_x_2[i]*(np.cos(theta[i]))**2 + str_out_y_2[i]*(np.sin(theta[i]))**2 + 2*str_out_xy_2[i]*np.sin(theta[i])*np.cos(theta[i])
    xprime3_out = str_out_x_3[i]*(np.cos(theta[i]))**2 + str_out_y_3[i]*(np.sin(theta[i]))**2 + 2*str_out_xy_3[i]*np.sin(theta[i])*np.cos(theta[i])
    xprime4_out = str_out_x_4[i]*(np.cos(theta[i]))**2 + str_out_y_4[i]*(np.sin(theta[i]))**2 + 2*str_out_xy_4[i]*np.sin(theta[i])*np.cos(theta[i])
    xprime5_out = str_out_x_5[i]*(np.cos(theta[i]))**2 + str_out_y_5[i]*(np.sin(theta[i]))**2 + 2*str_out_xy_5[i]*np.sin(theta[i])*np.cos(theta[i])

    xprime1_in = str_in_x_1[i]*(np.cos(theta[i]))**2 + str_in_y_1[i]*(np.sin(theta[i]))**2 + 2*str_in_xy_1[i]*np.sin(theta[i])*np.cos(theta[i])
    xprime2_in = str_in_x_2[i]*(np.cos(theta[i]))**2 + str_in_y_2[i]*(np.sin(theta[i]))**2 + 2*str_in_xy_2[i]*np.sin(theta[i])*np.cos(theta[i])
    xprime3_in = str_in_x_3[i]*(np.cos(theta[i]))**2 + str_in_y_3[i]*(np.sin(theta[i]))**2 + 2*str_in_xy_3[i]*np.sin(theta[i])*np.cos(theta[i])
    xprime4_in = str_in_x_4[i]*(np.cos(theta[i]))**2 + str_in_y_4[i]*(np.sin(theta[i]))**2 + 2*str_in_xy_4[i]*np.sin(theta[i])*np.cos(theta[i])
    xprime5_in = str_in_x_5[i]*(np.cos(theta[i]))**2 + str_in_y_5[i]*(np.sin(theta[i]))**2 + 2*str_in_xy_5[i]*np.sin(theta[i])*np.cos(theta[i])
    
    yprime1_out = str_out_x_1[i]*(np.sin(theta[i]))**2 + str_out_y_1[i]*(np.cos(theta[i]))**2 - 2*str_out_xy_1[i]*np.sin(theta[i])*np.cos(theta[i])
    yprime2_out = str_out_x_2[i]*(np.sin(theta[i]))**2 + str_out_y_2[i]*(np.cos(theta[i]))**2 - 2*str_out_xy_2[i]*np.sin(theta[i])*np.cos(theta[i])
    yprime3_out = str_out_x_3[i]*(np.sin(theta[i]))**2 + str_out_y_3[i]*(np.cos(theta[i]))**2 - 2*str_out_xy_3[i]*np.sin(theta[i])*np.cos(theta[i])
    yprime4_out = str_out_x_4[i]*(np.sin(theta[i]))**2 + str_out_y_4[i]*(np.cos(theta[i]))**2 - 2*str_out_xy_4[i]*np.sin(theta[i])*np.cos(theta[i])
    yprime5_out = str_out_x_5[i]*(np.sin(theta[i]))**2 + str_out_y_5[i]*(np.cos(theta[i]))**2 - 2*str_out_xy_5[i]*np.sin(theta[i])*np.cos(theta[i])
    
    yprime1_in = str_in_x_1[i]*(np.sin(theta[i]))**2 + str_in_y_1[i]*(np.cos(theta[i]))**2 - 2*str_in_xy_1[i]*np.sin(theta[i])*np.cos(theta[i])
    yprime2_in = str_in_x_2[i]*(np.sin(theta[i]))**2 + str_in_y_2[i]*(np.cos(theta[i]))**2 - 2*str_in_xy_2[i]*np.sin(theta[i])*np.cos(theta[i])
    yprime3_in = str_in_x_3[i]*(np.sin(theta[i]))**2 + str_in_y_3[i]*(np.cos(theta[i]))**2 - 2*str_in_xy_3[i]*np.sin(theta[i])*np.cos(theta[i])
    yprime4_in = str_in_x_4[i]*(np.sin(theta[i]))**2 + str_in_y_4[i]*(np.cos(theta[i]))**2 - 2*str_in_xy_4[i]*np.sin(theta[i])*np.cos(theta[i])
    yprime5_in = str_in_x_5[i]*(np.sin(theta[i]))**2 + str_in_y_5[i]*(np.cos(theta[i]))**2 - 2*str_in_xy_5[i]*np.sin(theta[i])*np.cos(theta[i])
    

    # append all the values to lists:
    str_xprime1_out.append(xprime1_out)
    str_xprime2_out.append(xprime2_out)
    str_xprime3_out.append(xprime3_out)
    str_xprime4_out.append(xprime4_out)
    str_xprime5_out.append(xprime5_out)
    
    str_xprime1_in.append(xprime1_in)
    str_xprime2_in.append(xprime2_in)
    str_xprime3_in.append(xprime3_in)
    str_xprime4_in.append(xprime4_in)
    str_xprime5_in.append(xprime5_in)
    
    str_yprime1_out.append(yprime1_out)
    str_yprime2_out.append(yprime2_out)
    str_yprime3_out.append(yprime3_out)
    str_yprime4_out.append(yprime4_out)
    str_yprime5_out.append(yprime5_out)
    
    str_yprime1_in.append(yprime1_in)
    str_yprime2_in.append(yprime2_in)
    str_yprime3_in.append(yprime3_in)
    str_yprime4_in.append(yprime4_in)
    str_yprime5_in.append(yprime5_in)


########################################################################################################

'''
# Get bending strain
    
bendstr1 = []
bendstr2 = []
bendstr3 = []
bendstr4 = []
bendstr5 = []

for j in range(0, len(str_xprime1_out)):
    str_out_1 = np.sqrt(str_xprime1_out[j]**2 + str_yprime1_out[j]**2 + str_out_z_1[j]**2)
    str_out_2 = np.sqrt(str_xprime2_out[j]**2 + str_yprime2_out[j]**2 + str_out_z_2[j]**2)
    str_out_3 = np.sqrt(str_xprime3_out[j]**2 + str_yprime3_out[j]**2 + str_out_z_3[j]**2)
    str_out_4 = np.sqrt(str_xprime4_out[j]**2 + str_yprime4_out[j]**2 + str_out_z_4[j]**2)
    str_out_5 = np.sqrt(str_xprime5_out[j]**2 + str_yprime5_out[j]**2 + str_out_z_5[j]**2)
    
    str_in_1 = np.sqrt(str_xprime1_in[j]**2 + str_yprime1_in[j]**2 + str_in_z_1[j]**2)
    str_in_2 = np.sqrt(str_xprime2_in[j]**2 + str_yprime2_in[j]**2 + str_in_z_2[j]**2)
    str_in_3 = np.sqrt(str_xprime3_in[j]**2 + str_yprime3_in[j]**2 + str_in_z_3[j]**2)
    str_in_4 = np.sqrt(str_xprime4_in[j]**2 + str_yprime4_in[j]**2 + str_in_z_4[j]**2)
    str_in_5 = np.sqrt(str_xprime5_in[j]**2 + str_yprime5_in[j]**2 + str_in_z_5[j]**2)
    
    str_bend_1 = (str_out_1 - str_in_1) / 2
    str_bend_2 = (str_out_2 - str_in_2) / 2
    str_bend_3 = (str_out_3 - str_in_3) / 2
    str_bend_4 = (str_out_4 - str_in_4) / 2
    str_bend_5 = (str_out_5 - str_in_5) / 2
    
    bendstr1.append(str_bend_1)
    bendstr2.append(str_bend_2)
    bendstr3.append(str_bend_3)
    bendstr4.append(str_bend_4)
    bendstr5.append(str_bend_5)
'''

########################################################################################################
# Plot strains:
plt.plot(arc,axialstr3_out, label='Loadstep 3, out')
plt.plot(arc,axialstr3_in,  label='Loadstep 3, in')
plt.xlabel("Arc length [mm]")
plt.ylabel("Axial strain")
plt.title("Axial strain on the inside and outside (actuator extension 20 [mm])")
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






