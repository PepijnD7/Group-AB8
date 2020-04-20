import numpy as np
import matplotlib.pyplot as plt

current_power_source=list()
voltage_power_source=list()

voltage_power_source_calib=list()
voltage_current_sensor=list()

data_file=open("CurentVoltageReading3.txt","r")
i=0
for line in data_file.readlines():
    if i>0:
        char=line.split("\t")
        current_power_source.append(float(char[0].strip()))
        voltage_power_source.append(float(char[1].strip()))
    i=i+1
data_file.close()

data_file=open("CurrentSensorCalibration.txt","r")
i=0
for line in data_file.readlines():
    if i>0:
        char=line.split("\t")
        voltage_power_source_calib.append(float(char[1].strip()))
        voltage_current_sensor.append(float(char[2].strip()))
    i=i+1
data_file.close()

#linear regression, y=m1x+n1
current_power_source,voltage_power_source=np.array(current_power_source),np.array(voltage_power_source)
#matrix A=[x,1], p=[m1,n1]
A=np.vstack([current_power_source,np.ones(len(current_power_source))]).T
m1,n1=np.linalg.lstsq(A,voltage_power_source,rcond=None)[0]

#linear regressiom, y=m2x+n2
voltage_power_source_calib,voltage_current_sensor=np.array(voltage_power_source_calib),np.array(voltage_current_sensor)
#matrix B=[x,1], p=[m2,n2]
B=np.vstack([voltage_current_sensor,np.ones(len(voltage_current_sensor))]).T
m2,n2=np.linalg.lstsq(B,voltage_power_source_calib,rcond=None)[0]

f1=m2/m1
f2=n2-n1
f2=f2/m1

plt.grid()
plt.ylabel('Voltage current source[V]')
plt.xlabel('Current power source[A]')
plt.plot(current_power_source, voltage_power_source,'x',label='Calibration data')
plt.plot(current_power_source, m1*current_power_source+n1,'r',label='Linear regression')
plt.show()

plt.grid()
plt.ylabel('Voltage power source[V]')
plt.xlabel('Voltage current sensor[V]')
plt.plot(voltage_current_sensor,voltage_power_source_calib,'x',label='Calibration data')
plt.plot(voltage_current_sensor,voltage_current_sensor*m2+n2,'r',label='Linear regression')
plt.show()
