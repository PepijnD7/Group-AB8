import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

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
    if i>1:
        char=line.split("\t")
        tl_1.append(float(char[0].strip()))
        vpsl_1.append(float(char[1].strip()))
        vcsl_1.append(float(char[2].strip()))
    i=i+1
data_file.close()

data_file=open("Dis2.txt","r")
i=0
for line in data_file.readlines():
    if i>1:
        char=line.split("\t")
        tl_2.append(float(char[0].strip()))
        vpsl_2.append(float(char[1].strip()))
        vcsl_2.append(float(char[2].strip()))
    i=i+1
data_file.close()

data_file=open("Dis3.txt","r")
i=0
for line in data_file.readlines():
    if i>1:
        char=line.split("\t")
        tl_3.append(float(char[0].strip()))
        vpsl_3.append(float(char[1].strip()))
        vcsl_3.append(float(char[2].strip()))
    i=i+1
data_file.close()

data_file=open("Dis4.txt","r")
i=0
for line in data_file.readlines():
    if i>1:
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

plt.plot(t1,dis1,':')
plt.plot(t2,dis2,'-.')
plt.plot(t3,dis3,'--')
plt.plot(t4,dis4,'-')
plt.show()

#calculate the current from vcs using the relation found in excel
# current=(vcs-2.521)/(-0.1457)
c1=(vcs_1-2.521)/(-0.1457)
c2=(vcs_2-2.521)/(-0.1457)
c3=(vcs_3-2.521)/(-0.1457)
c4=(vcs_4-2.521)/(-0.1457)

#use data sheet to get force
dy_dx=0.00058
n=0.3

f1=(c1-n)/dy_dx
f2=(c2-n)/dy_dx
f3=(c3-n)/dy_dx
f4=(c4-n)/dy_dx

#subtract error
i=0
fsum=0
while t1[i]==-1:
    fsum=fsum+f1[i]
    i=i+1
fsum=fsum+f1[i-1]
error1=fsum/(i+1)

i=0
fsum=0
while t2[i]==-1:
    fsum=fsum+f2[i]
    i=i+1
    print(fsum)
fsum=fsum+f2[i-1]
print(fsum)
error2=fsum/(i+1)

i=0
fsum=0
while t3[i]==-1:
    fsum=fsum+f3[i]
    i=i+1
fsum=fsum+f3[i-1]
error3=fsum/(i+1)

i=0
fsum=0
while t4[i]==-1:
    fsum=fsum+f4[i]
    i=i+1
fsum=fsum+f4[i-1]
error4=fsum/(i+1)

error=np.array([error1,error2,error3,error4])

plt.plot(t1,f1,':')
plt.plot(t2,f2,'-.')
plt.plot(t3,f3,'--')
plt.plot(t4,f4,'-')
plt.show()
