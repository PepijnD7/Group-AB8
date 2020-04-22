import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



### Opens the data
data = pd.read_csv("Measurements2014_05_22.txt", sep="\t", engine='python', header=4)
print(data.head())

code_location = {"A0": 1.58908, "A1": 2.09349, "A2": 2.59791,
                 "B0": 3.77008, "B1": 3.26436, "B2": 2.75864,
                 "C0": 0.192102, "C1": 0.414263, "C2": 0.510969, "C3": 0.673016, "C4": 0.793244, "C5": 0.848131,
                 "C6": 0.984042, "C7": 1.25324,
                 "D0": 5.17115, "D1": 4.95288, "D2": 4.83656, "D3": 4.68756, "D4": 4.55425, "D5": 4.50327,
                 "D6": 4.33205, "D7": 4.07065}
# the name was arranged so An and Bn have the same actual location, the same holds for C and D
actual_location = {"A0": 1.05, "A1": 0.55, "A2": 0.05,
                   "B0": 1.05, "B1": 0.55, "B2": 0.05,
                   "C0": 0.07, "C1": 0.296, "C2": 0.378, "C3": 0.54, "C4": 0.645, "C5": 0.70, "C6": 0.759, "C7": 1.027,
                   "D0": 0.076, "D1": 0.297, "D2": 0.388, "D3": 0.540, "D4": 0.650, "D5": 0.711, "D6": 0.764,
                   "D7": 1.024}

# data entry of column must be string

'''
def actual_location_est(p1,p2):
    code1 = code_location[p1]
    code2 = code_location[p2]
    if p1[0] in ["A","C"]:#ascending
        n = data.loc[0,code1:code2].shape[1]

    else:#descnding
        n = data.loc[0, code2:code1].shape[1]

    if p1[0] in ["A", "B"]:  # ascending
        x0 = actual_location[p2]
        x1 = actual_location[p1]

    else:  # descnding
        x0 = actual_location[p1]
        x1 = actual_location[p2]


    return np.linspace(x0,x1,n)

print(actual_location["A0"])
print(actual_location["A1"])
print(actual_location_est("A0","A1"))
'''

#load step number    -  1  2   3   4   5
load_steps_t =      [0, 1, 13, 28, 40, 55]
t = load_steps_t[1]





A_plot = []
Ay_plot = []

B_plot = []
By_plot = []

C_plot = []
Cy_plot = []

D_plot = []
Dy_plot = []



for i in range(8):
    C = "C" + str(i)
    D = "D" + str(i)

    strainC = data[str(code_location[C])].iloc[t]
    strainD = data[str(code_location[D])].iloc[t]

    C_plot.append(actual_location[C])
    Cy_plot.append(strainC)

    D_plot.append(actual_location[D])
    Dy_plot.append(strainD)


#adding A and B data to plot
for i in range(3):
    A = "A"+str(i)
    B = "B" + str(i)

    strainA = data[str(code_location[A])].iloc[t]
    strainB = data[str(code_location[B])].iloc[t]

    A_plot.append(actual_location[A])
    Ay_plot.append(strainA)

    B_plot.append(actual_location[B])
    By_plot.append(strainB)

plt.plot(A_plot,Ay_plot)
plt.plot(B_plot,By_plot)
plt.plot(C_plot,Cy_plot)
plt.plot(D_plot,Dy_plot)

plt.show()