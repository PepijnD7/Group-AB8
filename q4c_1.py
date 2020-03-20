import numpy as np
import scipy as sp
from numpy.linalg import inv
import matplotlib.pyplot as plt

#training data of ten aircraft with ten different specifications
sn = np.array([[268,60.30,58.37,17.40,880,8800,233000,180000,168000,7],
               [292,60.3,63.69,16.8,880,8200,233000,182000,173000,8],
               [142,35.8,33.62,12.6,850,3500,65317,58604,37648,3],
               [188,35.8,42.12,12.6,850,4300,76900,66361,42493,3],
               [408,64.44,70.67,19.4,920,11500,390100,295743,184567,9],
               [320,60.9,63.8,18.5,900,11800,297500,201800,134800,5],
               [408,64.8,73.86,18.5,920,12000,351543,237680,159570,7],
               [294,60.1,62.8,16.3,920,11500,252650,192776,110677,6],
               [344,60.1,68.3,17.02,903,12000,254100,202000,118000,8],
               [88,26,31.68,9.86,850,3300,36500,34000,21810,2]])
               
aircraft = np.array(["Airbus A330-200","Airbus A330-300",
               "Boeing 737-700","Boeing 737-900",
               "Boeing 747-400","Boeing 777-200ER",
               "Boeing 777-300ER","Boeing 787-9",
               "Boeing 787-10","Embraer 175"])
'''
specs = np.array([Max.passengers,Wingspan,
                  Length,Height,
                  Cruising speed,Max.range,
                  Max.take-off weight,Max. landing weight,
                  Empty weight,Amount of toilets])
'''


on = np.array([0,1,2,3,4,5,6,7,8,9])
#find the factors using least-squares method
fn = inv(np.transpose(sn) @ sn) @ np.transpose(sn) @ on

specs = sn[9]
output=fn @ specs

print(output)
print
output=int(np.round(output))
print("Aircraft is most likely a", aircraft[output])
