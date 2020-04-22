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


def actual_location_est(p1,p2):
    code1 = str(code_location[p1])
    code2 = str(code_location[p2])
    if p1[0] in ["A","C"]:#ascending
        n = int(data.loc[0,code1:code2].shape[0])

    else:#descnding
        n = int(data.loc[0, code2:code1].shape[0])

    if p1[0] in ["A", "B"]:  # ascending
        x0 = actual_location[p2]
        x1 = actual_location[p1]

    else:  # descnding
        x0 = actual_location[p1]
        x1 = actual_location[p2]


    return np.linspace(x0,x1,n)



#load step number    -  1  2   3   4   5
load_steps_t =      [ 1, 13, 28, 40, 55]





for t in load_steps_t:

    A_plot = []
    Ay_plot = []

    B_plot = []
    By_plot = []

    C_plot = []
    Cy_plot = []

    D_plot = []
    Dy_plot = []



    for i in range(7):
        Ca = "C" + str(i)
        Cb = "C" + str(i+1)

        Da = "D" + str(i)
        Db = "D" + str(i+1)

        strainC = data.loc[t,str(code_location[Ca]):str(code_location[Cb])]
        strainD = data.loc[t,str(code_location[Db]):str(code_location[Da])]
        #
        #do the x as a list
        xC = actual_location_est(Ca,Cb)
        xD = actual_location_est(Da, Db)

        C_plot.extend(xC)
        Cy_plot.extend(strainC)

        D_plot.extend(xD)
        Dy_plot.extend(strainD)


    #adding A and B data to plot
    for i in range(1,0,-1):
        Aa = "A"+str(i)
        Ab = "A" + str(i+1)

        Ba = "B" + str(i)
        Bb = "B" + str(i + 1)

        strainA = data.loc[t,str(code_location[Aa]):str(code_location[Ab])]
        strainB = data.loc[t,str(code_location[Bb]):str(code_location[Ba])]

        xA = actual_location_est(Aa,Ab)
        xB = actual_location_est(Ba, Bb)

        A_plot.extend(xA)
        Ay_plot.extend(strainA)

        B_plot.extend(xB)
        By_plot.extend(strainB)

    plt.plot(A_plot,Ay_plot)
    plt.plot(B_plot,By_plot)
    plt.plot(C_plot,Cy_plot)
    plt.plot(D_plot,Dy_plot)

    plt.show()