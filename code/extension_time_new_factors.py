import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from scipy import interpolate

'''4 measurements for displacement
Dis1 - 10mm
Dis2 - 20mm
Dis3 - 30mm
Dis4 - 39mm (maximum extension)
'''

tl_1=list()
tl_2=list()
tl_3=list()
tl_4=list()

vpsl_1=list()
vpsl_2=list()
vpsl_3=list()
vpsl_4=list()

vcsl_1=list()
vcsl_2=list()
vcsl_3=list()
vcsl_4=list()

data_file=open("Dis1.txt","r")
i=0
for line in data_file.readlines():
    if i>0:
        char=line.split("\t")
        tl_1.append(float(char[0].strip()))
        vpsl_1.append(float(char[1].strip()))
        vcsl_1.append(float(char[2].strip()))
    i=i+1
data_file.close()

data_file=open("Dis2.txt","r")
i=0
for line in data_file.readlines():
    if i>0:
        char=line.split("\t")
        tl_2.append(float(char[0].strip()))
        vpsl_2.append(float(char[1].strip()))
        vcsl_2.append(float(char[2].strip()))
    i=i+1
data_file.close()

data_file=open("Dis3.txt","r")
i=0
for line in data_file.readlines():
    if i>0:
        char=line.split("\t")
        tl_3.append(float(char[0].strip()))
        vpsl_3.append(float(char[1].strip()))
        vcsl_3.append(float(char[2].strip()))
    i=i+1
data_file.close()

data_file=open("Dis4.txt","r")
i=0
for line in data_file.readlines():
    if i>0:
        char=line.split("\t")
        tl_4.append(float(char[0].strip()))
        vpsl_4.append(float(char[1].strip()))
        vcsl_4.append(float(char[2].strip()))
    i=i+1
data_file.close()

t1=np.array(tl_1)
t2=np.array(tl_2)
t3=np.array(tl_3)
t4=np.array(tl_4)

vps_1=np.array(vpsl_1)
vps_2=np.array(vpsl_2)
vps_3=np.array(vpsl_3)
vps_4=np.array(vpsl_4)

vcs_1=np.array(vcsl_1)
vcs_2=np.array(vcsl_2)
vcs_3=np.array(vcsl_3)
vcs_4=np.array(vcsl_4)

dis1=10*vps_1/2
dis2=10*vps_2/2
dis3=10*vps_3/2
dis4=10*vps_4/2

#calculate the current from vcs using the relation
#found in calibration_reading.py
#current=f1*vcs+f1
f1=-4.78935172112945
f2=11.975657507913853

c1=f1*vcs_1+f2
c2=f1*vcs_2+f2
c3=f1*vcs_3+f2
c4=f1*vcs_4+f2

#use data sheet to get force
dy_dx=0.00058
n=0.3

f1=(c1-n)/dy_dx
f2=(c2-n)/dy_dx
f3=(c3-n)/dy_dx
f4=(c4-n)/dy_dx

#subtract error
#find the force and displacement values corresponding to t=-1
i=0
fsum=0
dissum=0
while t1[i] == -1:
    dissum += dis1[i]
    fsum += f1[i]
    i += 1
error1 = fsum/i
errordis1 = dissum/i
t1=np.delete(t1,np.s_[:i])
f1=np.delete(f1,np.s_[:i])
dis1=np.delete(dis1,np.s_[:i])

i=0
fsum=0
dissum=0
while t2[i]==-1: 
    dissum += dis2[i]
    fsum+=f2[i]
    i+=1
error2=fsum/i
errordis2 = dissum/i
t2=np.delete(t2,np.s_[:i])
f2=np.delete(f2,np.s_[:i])
dis2=np.delete(dis2,np.s_[:i])

i=0
fsum=0
dissum=0
while t3[i]==-1:
    dissum += dis3[i]
    fsum+=f3[i]
    i+=1
error3=fsum/i
errordis3 = dissum/i
t3=np.delete(t3,np.s_[:i])
f3=np.delete(f3,np.s_[:i])
dis3=np.delete(dis3,np.s_[:i])

i=0
fsum=0
dissum=0
while t4[i]==-1:
    dissum += dis4[i]
    fsum+=f4[i]
    i+=1
error4=fsum/i
errordis4 = dissum/i
t4=np.delete(t4,np.s_[:i])
f4=np.delete(f4,np.s_[:i])
dis4=np.delete(dis4,np.s_[:i])

error=np.array([[error1,error2,error3,error4],
               [errordis1,errordis2,errordis3,errordis4]])
#subtract error
f1=f1-error[0,0]
f2=f2-error[0,1]
f3=f3-error[0,2]
f4=f4-error[0,3]

dis1=dis1-error[1,0]
dis2=dis2-error[1,1]
dis3=dis3-error[1,2]
dis4=dis4-error[1,3]

#set time to zero
t1=t1-t1[0]
t2=t2-t2[0]
t3=t3-t3[0]
t4=t4-t4[0]
'''
plt.grid()
plt.ylabel('Actuator extension [mm]')
plt.xlabel('Time [s]')
plt.plot(t1,dis1,':',label='10mm')
plt.plot(t2,dis2,'-.',label='20mm')
plt.plot(t3,dis3,'--',label='30mm')
plt.plot(t4,dis4,'-',label='39mm')
plt.legend(title='Maximum extension:')
plt.show()
'''
# plt.grid()
# plt.ylabel('Actuation force [N]')
# plt.xlabel('Time [s]')
# plt.plot(t1,f1,':',label='10mm')
# plt.plot(t2,f2,'-.',label='20mm')
# plt.plot(t3,f3,'--',label='30mm')
# plt.plot(t4,f4,'-',label='39mm')
# plt.legend(title='Maximum extension:', loc='upper right')
# plt.show()

sf1=gaussian_filter(f1,4)
sf2=gaussian_filter(f2,4)
sf3=gaussian_filter(f3,4)
sf4=gaussian_filter(f4,3)

interf=interpolate.interp1d(t1,f1)
intert1=np.arange(0,10,0.1)
interf1=interf(intert1)

##plt.grid()
##plt.ylabel('Actuation force [N]')
##plt.xlabel('Time [s]')
##plt.plot(t1,f1,'bo',label='10mm',fillstyle='none')
##plt.plot(t2,f2,'gx',label='20mm')
##plt.plot(t3,f3,'r+',label='30mm')
##plt.plot(t4,f4,'gx',label='39mm',fillstyle='none')
##plt.plot(t1,sf1,'r-',label='10mm')
##plt.plot(t2,sf2,'g:',label='20mm')
##plt.plot(t3,sf3,'b-.',label='30mm')
##plt.plot(t4,sf4,'y--',label='39mm')
##plt.plot(intert1,interf1)
##plt.legend(title='Maximum extension:', loc='upper right')
##plt.show()
